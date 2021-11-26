# Network Lab

This lab assumes you have completed the infrastructure-lab, so that you now have 5 machines in your VirtualBox installation: 3 working nodes, 1 master, 1 host.
It is now the time to create a network for them.

- [Add All Machines](#Add-All-Machines)
- [Add NAT Node](#Add-NAT-Node)
- [GNS3 Network](#GNS3-Network)
- [IP addresses](#IP-addresses)
- [Connect host to master and nodes](#Connect-host-to-master-and-nodes)

## Configure NAT networking

- "**Nat Service**" is explained [here](https://www.virtualbox.org/manual/ch06.html#network_nat_service)
- If you have completed the first lab, you should be able to use the VirtualBox command-line interface.
- Add a new NAT network (I name it **k8s-nat**):
   **VBoxManage natnetwork add --netname k8s-nat --network "192.168.122.0/24" --enable --dhcp off**
- Now, for each of you machines, right-click -> settings, choose **Network**,  and select "NAT Network" from the drop-down list. Make sure that the correct NAT network appears in "Name".
- Open the "Advanced" option there, and make sure that the "Cable Connected" is checked.


## IP addresses

- Run and configure static IP addresses for master and workers:
  - sudo vi /etc/sysconfig/network-scripts/ifcfg-ens33
  - BOOTPROTO=static
  - IPADDR=192.168.122.x (where x is 11,12,13 for k8s-A, k8s-B, k8s-C, 10 for k8s-Master, 100 for the host)
  - NETMASK=255.255.255.0
  - GATEWAY=192.168.122.1
  - to restart networking:
    - nmcli networking off
    - nmcli networking on

## Connect host to master and nodes

- Create a new ssh keypair:
          ssh-keygen
- copy the key to each machine (you may have problems with fingerprints..)
          ssh-copy-id osboxes@192.168.122.10
- Now connect like this:
          ssh osboxes@192.168.122.10
- Use [Terminator shell](https://dev.to/xeroxism/how-to-install-terminator-a-linux-terminal-emulator-on-steroids-1m3h) on your host machine.
You can then login and command all nodes at once.
https://terminator-gtk3.readthedocs.io/en/latest/
To install terminator:
  - **sudo add-apt-repository ppa:gnome-terminator**
  - **sudo apt-get update**
  - **sudo apt-get install terminator**
