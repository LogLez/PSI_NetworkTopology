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

Program Network‘s topology is an application that allow you to list automatically a network‘s topology from the host machine,
This program will use SNPM protocol for getting information about routers, so we will use the libraries PySNMP and Scapy.

_This is a project for PSI course !_

### How do the application work ?

Basically, the application will start from the address of the first router with DHCP. Then, it will find recursivly all connected routers
of the autonomous system area thanks to the routing tables. And so on, until it found every routers of the AS.



### How can we use this application ?

- First of all, you need to import the GNS3 project, foundable at https://home.zcu.cz/~maxmilio/PSI/psi-example-project-1.gns3project
( It can be easily imported into the GNS3 simulator using the "File/Import portable project“ function.)
- After that, you will have to activate the SNMP on the router by sending thoses commands in the console :
```shell
enable
config terminal
snmp-server community public ro
end
write
```
- Then, you just have to enter in the console of a random node. Python3 is already installed by default, but you need to install
the libraries we will use in the program. Once you are in the console you have to run some commands :
```shell
apt-get update
apt-get upgrade
apt-get install python3-pip
pip install scapy pysnmp
```
- Now, you just have to import the python code by creating a python file with nano for example or use GitHub clone.
- Then, start the python application by start the following command :
```shell
python3 run.py
```
- Wait until the information's list appears.

It is very simple !  Don't worry :)


**Versions history:**

|      Version       | Date           | Python version |        Gradle version       |
|--------------------|----------------|----------------|-----------------------------|
| **1.0.0**          | 17 / 05 / 2023 | Python 3.17 8  |        8.0                  |

-----