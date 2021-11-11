# Infrastructure Lab

This lab will guide you through the process of creating a baseline environment that we'll use for out kubernetes installation. I have tried this on Windows-11 Pro (version 21H2).

- [VirtualBox](#Virtual-Box)
- [GNS3](#GNS3)
- [Virtual Machines](#K8S-Virtual-Machines)
- [Host Machine](#Host-Machine)


## Virtual Box

- I am using VirtualBox, although GNS3 documentation says that vmware workstation is a better solution. This is because some features of vmware Workstation are not supported om the free version(Player).
- install (or upgrade) [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## GNS3
- Here's the [Windows GNS3 installation guide](https://docs.gns3.com/docs/getting-started/installation/windows).
- **To upgrade first uninstall** (win-x -> apps & features -> find gns3 -> uninstall)
- **Now for the trickiest part:**
You should somehow convince GNS3 to use VirtualBox as a server to run appliances (these are you virtual machines).
[This is explained here](https://docs.gns3.com/docs/getting-started/installation/download-gns3-vm) (increase vcpu and memory when you do so).
You should convince GNS3 to use that VM so look at: **GNS3: help-> setup wizard**
- How do you know you're good?
If all goes well, when you run GNS3 it will run both servers:

  - VirtualBox
  - the local dynamips server
  - (This may take some time...)
- You should be able to see two green lights at the right side of GNS3 window:
  - Desktop...
  - GNS VM....
- You cannot run just the VirtualBox server!!!
The local (dynamips) server must also run, although you will probably not use it at all.

## K8S Virtual Machines

- We are using "Stand Alone" servers for gns3, so don't look for an appliance
- Download Centos 8.4 from osboxes.org 
    link: https://www.osboxes.org/centos/
    user: osboxes pass: osboxes.org
- Unzip the downloaded file
- Create a Linux (RedHat 64G) machine
- 8192 MB of RAM
- use your downloaded file as the system disk.
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
