# 1 - Infrastructure Lab

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

- Download Centos 8.4 (server) from osboxes.org 
    link: https://www.osboxes.org/centos/
    user: osboxes pass: osboxes.org
- Unzip (I use [7z](https://www.7-zip.org/download.html)) the downloaded file - this is a virtual disk image (VDI) file.
- VirtualBox: Create a Linux (RedHat 64G) machine
- 8192 MB of RAM
- Use your downloaded VDI file as the system disk.
- Clone it carefully in VirtualBox - to create 3 workers nodes and one control node:
  - **Clone when machine is not working**
  - right-click clone
  - Rename your new machine (k8s-control, k8s-a, k8s-b, k8s-b)
  - create new MAC addresses
  - Full clone !!!
- Configure 2 or more CPUs for your control node machine( settings/system).  
- Make sure your new machines can work

## Host Machine

- Create another machine to be used as a host - to connect and configure.
- I'm using a local Linux (Ubuntu-20) as a host, to control the cluster.

## End Results

- You should have:
  - a VirtualBox installation
  - 3 kubernetes worker machines: k8s-a, k8s-b, k8s-c
  - 1 kubernetes control machine: k8s-control
  - 1 host machine
- We'll handle networking at the next lab.

(goto [2-Network Lab](https://github.com/YuvalShaul/kubernetes/blob/main/labs/k8s-VirtualBox/2-network-lab/README.md))