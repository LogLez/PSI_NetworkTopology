<h2 align="center">
<br>
  <img src="images/PSI.png" alt="PSI logo">
  <br>
    <br>
        An application for Network Topology
        using SNMP Protocol
  <br>
</h2>



<div align="left">

![Maven-Central](https://img.shields.io/badge/MavenCentral-8.7.6-success)
![Java](https://img.shields.io/badge/Python-3.17-red)

</div>

---

### What is this application ?

Program Network‘s topology is an application that allow you to list automatically lists a network‘s topology from the host machine,
the host machine. This program will use SNPM protocol for getting information about routers, so we will use
the libraries PySNMP and Scapy.

_This is a project for PSI course !_

### How do the application work ?

Basically, the application will start from the address of the first router with DHCP. Then, it will find recursivly all connected routers
of the autonomous system area thanks to the routing tables. And so on, until it found every routers of the AS.



### How can we use is TCP_Multithreading ?

- First of all, you need to import the GNS3 project, foundable at https://home.zcu.cz/~maxmilio/PSI/psi-example-project-1.gns3project
( It can be easily imported into the GNS3 simulator using the „File/Import portable project“ function.)
- Then, you just have to start the python application by start the following command run.py "182.0.0.1".
- Wait until the informations's list appears.

It is very simple !  Don't worry :)


**Versions history:**

|      Version       | Date           | Java version  |        Gradle version       |
|--------------------|----------------|---------------|-----------------------------|
| **1.0.0**          | 17 / 05 / 2023 | Python 3.17 8 |        8.0                  |

-----