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

Basically, the application will start from the address of the first router with DHCP. Then, it will find recursively all connected routers and interfaces
of the autonomous system area thanks to the routing tables. And so on, until it found every routers of the AS.

### Installation of the dependencies 

Before using this application, you will have to set up the project and install all the libraries needed.

##### Installation of the GNS3 project
- First of all, you need to import the GNS3 project, can be found at https://home.zcu.cz/~maxmilio/PSI/psi-example-project-1.gns3project
( It can be easily imported into the GNS3 simulator using the "File/Import portable project“ function).
Obviously, you can create your personal GNS3 project and use this application on it, but you will have to configure it as well.

##### Activate SNMP server on router (if its not already done)

- After downloading and installing the GNS3 project, you will have to activate the SNMP on the router by sending theses commands in the console :
```shell
enable
config terminal
snmp-server community public ro
end
write
```

##### Installation of the libraries

- Then, you will select the node you want, and install all the libraries needed. (which are nano, python3, pip, scapy, pysnmp)
(If you are using the GNS3 Example project, python3 and scapy are already installed). But sometimes, you have to update first because the installation cannot work successfully

**Installation of libraries.**
```shell
#Update the linux node
apt-get update 
apt-get upgrade

#Install the libraries on the node
apt-get install nano
apt-get install python3-pip
pip3 install scapy pysnmp
```
<br>

***Warning*** : *In the GNS3 project, there is a problem with the compatibility of SNMP , you will have to remove the v5.0.0 and replace it by 4.8.0 by using these command.*

<br>

```shell
pip3 uninstall pyasn1
pip3 install pyasn1==0.4.8
```

### How can we use this application ?

- You just have to import the python code by creating a python file with nano for example or use GitHub clone.
- By using nano,you just have to create a file by using the command :
```shell
nano run.py
```
- Paste the code you can get from the file run.py in this repository and save the file with 'CTRL + X' ad 'Y' and 'ENTER'
- Then, start the python application by start the following command:
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