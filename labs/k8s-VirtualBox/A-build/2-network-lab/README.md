# 2 - Network Lab

(back to [1-Infrastructure Lab](https://github.com/YuvalShaul/kubernetes/tree/main/labs/k8s-VirtualBox/1-infastructure-lab))  
This lab assumes you have completed the infrastructure-lab, so that you now have 5 machines in your VirtualBox installation: 3 working nodes, 1 control node, 1 host.
It is now the time to create a network for them.

- [Configure NAT Networking](#Configure-NAT-Networking)
- [IP addresses](#IP-addresses)
- [Connect host to control and workers](#Connect-host-to-control-and-workers)

## Configure NAT Networking

- "**Nat Service**" is explained [here](https://www.virtualbox.org/manual/ch06.html#network_nat_service)
- If you have completed the [first lab](https://github.com/YuvalShaul/kubernetes/tree/main/labs/k8s-VirtualBox/1-infastructure-lab), you should be able to use the VirtualBox command-line interface.
- Add a new NAT network (I name it **k8s-nat**):  
   **VBoxManage natnetwork add --netname k8s-nat --network "192.168.122.0/24" --enable --dhcp off**
- Later on, if your nat network stops working, you can start it again by typing:  
**VBoxManage natnetwork stop  --netname k8s-nat**  
**VBoxManage natnetwork start --netname k8s-nat**
- Now, for each of you machines, right-click -> settings, choose **Network**,  and select "NAT Network" from the drop-down list. Make sure that the correct NAT network appears in "Name".
- Open the "Advanced" option there, and make sure that the "Cable Connected" is checked.


## IP addresses

- Run all nodes, then configure static IP addresses for control and workers.
- (use **right-ctrl** to from the mouse capture of the virtual machine window)
  - sudo vi /etc/sysconfig/network-scripts/  (--> press tab again to see your interface configuration file)
  - BOOTPROTO=static
  - IPADDR=192.168.122.x (where x is 11,12,13 for k8s-a, k8s-b, k8s-c, 10 for k8s-control, 100 for the host)
  - NETMASK=255.255.255.0
  - GATEWAY=192.168.122.1
  - restart your machines

## Connect host to control and workers

- SSH should work out-of-the-box
- You can connect like this:
          ssh osboxes@192.168.122.10
- Use [Terminator shell](https://dev.to/xeroxism/how-to-install-terminator-a-linux-terminal-emulator-on-steroids-1m3h) on your host machine.
You can then login and command all nodes at once.  
https://terminator-gtk3.readthedocs.io/en/latest/  
To install terminator:
  - **sudo add-apt-repository ppa:gnome-terminator**
  - **sudo apt-get update**
  - **sudo apt-get install terminator**

(go to [3 - Building a K8S Cluster](https://github.com/YuvalShaul/kubernetes/tree/main/labs/k8s-VirtualBox/A-build/3-building-a-cluster))  
