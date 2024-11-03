# 1 - Infrastructure Lab

This lab will guide you through the process of creating a baseline environment that we'll use for out kubernetes installation.  
I have tried this on Windows-11 Pro (version 21H2).

- [VmWare](#VmWare)
- [K8S Virtual Machines](#K8S-Virtual-Machines)
- [Host Machine](#Host-Machine)
- [Host Machine](#Host-Machine)
- [End Results](#End-Results)


## VmWare
- VmWare made Workstation pro free to use for personal use.
- You'll need to register to Broadcom first
- Download and install from [here](https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware+Workstation+Pro)

## K8S Virtual Machine Template

- Download Fedora 40 (server, VmWare, vmdk file) from osboxes.org.  
    link: https://www.osboxes.org/fedora/  
    user: **osboxes**    pass: **osboxes.org**
- Unzip (I use [7z](https://www.7-zip.org/download.html)) the downloaded file - this is a virtual disk image (VDI) file.
- Create a Linux, Fedora-64 machine
- 8192 MB of RAM - 1 virtual cpu (2 for the control node later)
- Use your downloaded VMDK file as the system disk, but choose a SATA disk type.


## Host Machine

- Create another machine to be used as a host - to connect and configure.
- I'm using a local Linux (Ubuntu-20) as a host, to control the cluster.
- You can use other distributions here (Fedore Workstations for example, or even another server, so non-GUI and work with a tool like [tmux](https://linuxize.com/post/getting-started-with-tmux/)).  
A GUI based one is easier to work with.  

(goto [2-Network Lab](https://github.com/YuvalShaul/kubernetes/tree/main/labs/k8s-VMWare/A-build/2-network-lab))