# Infrastructure Lab

This lab will guide you through the process of creating a baseline environment that we'll use for out kubernetes installation. I have tried this on Windows-11 Pro (version 21H2).

- [VirtualBox](#Virtual-Box)
- [GNS3](#GNS3)
- [Virtual Machines](#Virtual-Machines)
- [IP addresses for nodes](#IP-addresses-for-nodes)
- [Add your machines in GNS3](#Add-your-machines-in-GNS3)
- [Connect to master and nodes](#Connect-to-master-and-nodes)

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

## Virtual Machines

- We are using "Stand Alone" servers for gns3, so don't look for an appliance
- Download Centos 8.4 from osboxes.org 
    link: https://www.osboxes.org/centos/
    user: osboxes pass: osboxes.org
- Unzip the downloaded file
- Create a Linux (RedHat 64G) machine
- 8192 MB of RAM
- use your downloaded file as the system disk.
- Leave networking as "Not Attached" (let GNS3 handle this)
- Clone it carefully - to create 3 workers and 1 master:
     - **Clone when machine is not working**
     - Rename your new machine (master, worker..etc)
     - right-click clone
     - create new MAC addresses
     - Full clone !!!
  - Make sure your new machines can work

--------------------------------------------

## IP addresses for nodes

- These are Centos nodes.
- Address range should be: 192.168.122.0/24  (I'll explain why later)
- Run from VirtualBox and configure static IP addresses for master and workers:
  - sudo vi /etc/sysconfig/network-scripts/ifcfg-ens33
  - BOOTPROTO=static
  - IPADDR=192.168.122.x (where x is 1,2,3 for workers, 10 for master)
  - NETMASK=255.255.255.0
  - GATEWAY=192.168.122.100
  - to restart networking:
    - nmcli networking off
    - nmcli networking on

## Add your machines in GNS3

- First, both "local server" and "GNS3 VM" server should run.
    They start automatocally when you run GNS3, but it may take a minute.
- Open the **GNS3:edit/preferences** window, look for the VirtualBox section and add your machines from there.
- Create a new GNS3 project and add a simple Switch
- Connect all machines to the switch
- Add a "Nat Device", and connect it to the switch.

## Connect to master and nodes

I'm using a local Linux (Ubuntu-20) as a host, to control master and nodes.

- Create a new ssh keypair: 
          ssh-keygen 
- copy the key to each machine (you may have problems with fingerprints..)
          ssh-copy-id osboxes@192.168.122.1
- Now connect like this:
          ssh osboxes@192.168.122.1
- Use [Terminator shell](https://dev.to/xeroxism/how-to-install-terminator-a-linux-terminal-emulator-on-steroids-1m3h) on your host machine.
You can then login and command all nodes at once.

## End result

- You should have a network that looks like this:
![net](https://user-images.githubusercontent.com/40225170/141266815-7a93fcb9-b0df-496f-a39a-9ed274a4670d.jpg)
