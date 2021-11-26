# Network Lab

This lab assumes you have completed the infrastructure-lab, so that you now have 5 machines in your VirtualBox installation: 3 working nodes, 1 master, 1 host.
(not counting the GNS3 VM server machine)
It is now the time to create a network for them.

- [Add All Machines](#Add-All-Machines)
- [Add NAT Node](#Add-NAT-Node)
- [GNS3 Network](#GNS3-Network)
- [IP addresses](#IP-addresses)
- [Connect host to master and nodes](#Connect-host-to-master-and-nodes)

## Add All Machines

- Start GNS3, and wait until both local and virtualbox servers are running (2 green lights)
- Create a new blank project (File --> New blank project)
- Add a simple switch to it.
- Open the **GNS3:edit/preferences** window, look for the VirtualBox section and add your machines from there (except the GNS3 VM server machine)
- Connect all machines to the switch

## Add NAT Node

- Add a "[Nat Node](https://docs.gns3.com/docs/using-gns3/advanced/the-nat-node/)", and connect it to the switch.
- **"By default, the NAT node runs a DHCP server with a predefined pool in the 192.168.122.0/24 range."** We will not use the DHCP server, but we'll configure static IP addresses that use this CIDR block to all our machines.
- The IP address of the Nat Node itself is 192.168.122.1/24

## GNS3 Network

- Add machines to the network topology and connect them to the switch.
- The end reulst (when running) should look like this:
![net](https://user-images.githubusercontent.com/40225170/141266815-7a93fcb9-b0df-496f-a39a-9ed274a4670d.jpg)

## IP addresses

- These are Centos nodes. After running them (from GNS3) the network state in VirtualBox changes from "Not Attached" to "Generic Driver"--"UDPTunnel.
- We'll use address range of 192.168.122.0/24, so that the machines will be at the same network with the Nat Device.
- Run and configure static IP addresses for master and workers:
  - sudo vi /etc/sysconfig/network-scripts/ifcfg-ens33
  - BOOTPROTO=static
  - IPADDR=192.168.122.x (where x is 11,12,13 for workers, 10 for master, 100 for the host)
  - NETMASK=255.255.255.0
  - GATEWAY=192.168.122.1
  - to restart networking:
    - nmcli networking off
    - nmcli networking on

## Connect host to master and nodes

- Create a new ssh keypair:
          ssh-keygen
- copy the key to each machine (you may have problems with fingerprints..)
          ssh-copy-id osboxes@192.168.122.1
- Now connect like this:
          ssh osboxes@192.168.122.1
- Use [Terminator shell](https://dev.to/xeroxism/how-to-install-terminator-a-linux-terminal-emulator-on-steroids-1m3h) on your host machine.
You can then login and command all nodes at once.
https://terminator-gtk3.readthedocs.io/en/latest/
To install terminator:
  - **sudo add-apt-repository ppa:gnome-terminator**
  - **sudo apt-get update**
  - **sudo apt-get install terminator**
