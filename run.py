from pysnmp.hlapi import *
from pysnmp.smi import builder, view
from scapy.config import conf
from scapy.layers.dhcp import DHCP, BOOTP
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether
from scapy.sendrecv import srp1


def discover_topology(router_ip, community):
    # Create an SNMP engine + Oid of Routing table
    snmp_engine = SnmpEngine()
    oid_routing_table = '1.3.6.1.2.1.4.21.1' # https://bestmonitoringtools.com/mibdb/mibdb_search.php?mib=RFC1213-MIB

    # Load MIB modules for routing table
    mib_builder = builder.MibBuilder().loadModules('RFC1213-MIB')
    mib_view_controller = view.MibViewController(mib_builder)

    # Define the SNMP request to retrieve the routing table from the router
    error_indication, error_status, error_index, var_binds = next(
        getCmd(snmp_engine,
               CommunityData(community, mpModel=1), #mpModel=1 for selecting the version 2c of the community
               UdpTransportTarget((router_ip, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid_routing_table)))
    )

    # Process the response
    if error_indication:
        print(f'Error: {error_indication}')
    elif error_status:
        print(f'Error: {error_status.prettyPrint()} at {error_index}')
    else:
        # Print the topology information from the router
        print(f"This is the topology from the router : ({router_ip}):")
        for var_bind in var_binds:
            oid, value = var_bind
            table_entry = mib_view_controller.getNode(oid)
            print(f'Topology: {table_entry.getDisplayHint().clone(value)}')

            # Recursively discover other routers in the current autonomous area
            if "router" in str(table_entry):
                next_hop_ip = value.prettyPrint()
                discover_topology(next_hop_ip, community)


# DHCP Part | Retrieve the IP address of the initial router
conf.checkIPaddr = False
packet_dhcp_discover = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src="0.0.0.0", dst="255.255.255.255") / UDP(sport=68, dport=67) / BOOTP(op=1, chaddr="ff:ff:ff:ff:ff:ff") / DHCP(options=[("message-type", "discover"), "end"])
packet_dhcp_offer = srp1(packet_dhcp_discover, verbose=0)

if packet_dhcp_offer and DHCP in packet_dhcp_offer and packet_dhcp_offer[DHCP].options[0][1] == 2: #2 == type Offer packet
    router_ip = packet_dhcp_offer[BOOTP].siaddr
    print(f"Initial router IP: {router_ip}") # 0.0.0.0

    print("Offered IP address:", packet_dhcp_offer[IP].src)
    print("Offered MAC address:", packet_dhcp_offer[Ether].src)
    print("Server IP address:", packet_dhcp_offer[BOOTP].siaddr) # Only this one == 0.0.0.0
    print("Server MAC address:", packet_dhcp_offer[BOOTP].chaddr)
    print("Options:", packet_dhcp_offer[DHCP].options)

    community = 'public'  # SNMP community string
    router_ip = '10.0.1.254'  # I put this for testing the code, because DHCP return 0.0.0.0 for the router_IP
    discover_topology(router_ip, community)
else:
    print("Failed to retrieve the initial router IP via DHCP.")