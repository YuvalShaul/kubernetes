# Network Lab

This lab assumes you have completed the infrastructure-lab, so that you now have 5 machines in your VirtualBox installation: 3 working nodes, 1 master, 1 host.
It is time to create a network for them.

- [GNS3 Network](#GNS3-Network)
- [Add All Machines](#Add-All-Machines)
- [Add NAT device](#Add-NAT-device)

- [IP addresses for nodes](#IP-addresses-for-nodes)
- [Add your machines in GNS3](#Add-your-machines-in-GNS3)
- [Connect to master and nodes](#Connect-to-master-and-nodes)

## GNS3 Network

- Start GNS3, and wait until both local and virtualbox servers are running (2 green lights)
- Create a new blank project
- Add a simple switch to it
- We'll now add machines and connect them to the switch.
- The end reulst should look like this:
![net](https://user-images.githubusercontent.com/40225170/141266815-7a93fcb9-b0df-496f-a39a-9ed274a4670d.jpg)

## Add All Machines

- Open the **GNS3:edit/preferences** window, look for the VirtualBox section and add your machines from there.
- Connect all machines to the switch

## Add NAT device

- Add a "[Nat Node](https://docs.gns3.com/docs/using-gns3/advanced/the-nat-node/)", and connect it to the switch.
- **"By default, the NAT node runs a DHCP server with a predefined pool in the 192.168.122.0/24 range."** We will not use the DHCP server, but we'll configure static IP addresses that use this CIDR block to all our machines.

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



## Connect to master and nodes


- Create a new ssh keypair: 
          ssh-keygen 
- copy the key to each machine (you may have problems with fingerprints..)
          ssh-copy-id osboxes@192.168.122.1
- Now connect like this:
          ssh osboxes@192.168.122.1
- Use [Terminator shell](https://dev.to/xeroxism/how-to-install-terminator-a-linux-terminal-emulator-on-steroids-1m3h) on your host machine.
You can then login and command all nodes at once.


- create 4 notes on virtualbox (controller, worker1, worker2, user)
  use Ubuntu 18.04.bionic beaver
  (I use osboxes.org ready made vdi files for that)
- use the same "bridged" networking type, and connect all to the smae
  bridge where you connect to the internet.

- Networking.
  Use "netplan" to configure static ip address.
  Choose your IP addresses to match those that your router uses, so
  that your machines can get to the internet.
  Here is an example:

  network:
    version: 2
    renderer: NetworkManager
    ethernets:
      enp0s3:
        addresses:
          - 10.0.0.10/24
        gateway4: 10.0.0.138
        nameservers:
          addresses: [8.8.8.8, 4.4.4.4]


- install openssh-server on all machines.
- create a key pair on the "user" machine, using ssh-keygen
  Copy your public key to each server using ssh-copy-id
  https://www.ssh.com/academy/ssh/copy-id

- You can use the Terminator terminal, so that you can type commands to
  all 3 nodes at the same time:

  sudo add-apt-repository ppa:gnome-terminator
  sudo apt-get update
  sudo apt-get install terminator

  https://terminator-gtk3.readthedocs.io/en/latest/

*************************************************************

- Change the names of your machines using:
   hostnamecto set-hostname <new-name>

- Edit the /etc/hosts file to refer by name to all these machines.

- Log out and log in again, so that these take effect

