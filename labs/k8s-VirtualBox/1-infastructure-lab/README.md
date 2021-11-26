# Infrastructure Lab

This lab will guide you through the process of creating a baseline environment that we'll use for out kubernetes installation. I have tried this on Windows-11 Pro (version 21H2).

- [VirtualBox](#Virtual-Box)
- [K8S Virtual Machines](#K8S-Virtual-Machines)
- [Host Machine](#Host-Machine)
- [Host Machine](#Host-Machine)
- [End Results](#End-Results)


## Virtual Box

- install (or upgrade) [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- I am using 6.1.30 for this installation
- The extension pack is not needed for the lab
- The setup program will issue a warning about an 
  interface to be installed. This is OK.
- Add the following directory into your path:
    C:\Program Files\Oracle\VirtualBox
  so that you can run cli commands.

## K8S Virtual Machines

- We are using "Stand Alone" servers for gns3, so don't look for an appliance
- Download Centos 8.4 from osboxes.org 
    link: https://www.osboxes.org/centos/
    user: osboxes pass: osboxes.org
- Unzip the downloaded file
- Create a Linux (RedHat 64G) machine
- 8192 MB of RAM
- Create a new virtual machine and use your downloaded file as the system disk.
- Leave networking as "Not Attached" (let GNS3 handle this)
- Clone it carefully in VirtualBox - to create 3 workers and 1 master:
     - **Clone when machine is not working**
     - Rename your new machine (master, worker..etc)
     - right-click clone
     - create new MAC addresses
     - Full clone !!!
  - Make sure your new machines can work

## Host Machine

- I'm using a local Linux (Ubuntu-20) as a host, to control master and nodes.
- Create in using the same method you have used with the K8S nodes.

## End Results

- You should have:
  - a GNS3 running with 2 servers
  - a VirtualBox installation
  - 3 kubernetes worker machines: K8S-A, K8S-B, K8S-C
  - 1 kubernetes master machine: K8S-Master
  - 1 host machine
  - 1 GNS3 VM server machine
- No GNS3 network, we'll build that at the next lab.
