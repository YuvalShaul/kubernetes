# 2 - Network Lab

This lab assumes you have completed the [infrastructure-lab](https://github.com/YuvalShaul/kubernetes/tree/main/labs/k8s-VMWare/A-build/1-infastructure-lab), so that you now have a single machine that will be used as a template.
It is now the time to create a network, and clone it.

- [Configure NAT Networking](#Configure-NAT-Networking)
- [IP addresses](#IP-addresses)
- [Clone Machines](#Clone-Machines)
- [End Results](#End-Results)
- [Connect host to control and workers](#Connect-host-to-control-and-workers)


## Configure NAT Networking

- I am using the VmWare Workstation "Virtual Network Editor" (see under "Edit")
- Createing a new custom VMnet network, enabling NAT, disabling DHCP.
- This will create a VMNet interface on the Windows Host, with IP address that you could not use later on your guest machines.
- Now, for each of you machines, right-click -> settings, choose **Network**,  and select VMNet you have created.


## IP addresses

- Run your single machine
- Note: ifcfg-... files are not used animore, so NetworkManager and nmcli commands.
- I have create a bash script using vi, with the following content:
```
sudo nmcli connection add \
    type ethernet \
    con-name "Your Connection Name" \
    ifname YOUR_INTERFACE \
    ipv4.method manual \
    ipv4.addresses 192.168.1.10/24 \
    ipv4.gateway 192.168.1.1 \
    ipv4.dns 8.8.8.8
```
  - verify your interface name with **ip link show**
  - I was using **to-k8s** as my connection name
  - Make sure you IP address does not use the host interface address
  - You can change the default GW address when you crate the custom VMnet network
- run the script: **source <script file name>
- make sure you start you connection:
**nmcli connection ip <connection name>


## Clone Machines

- Maybe it is best to leave the template machine...well..as a template.
- Clone it carefully in VirtualBox - to create 3 or 4  workers nodes and one control node:
  - **Clone when machine is not working !**
  - right-click manage/clone (full clone)
  - Rename your new machine (k8s-control, k8s-a, k8s-b, k8s-c)
  - create new MAC addresses
  - Full clone !!!
- Configure 2 or more CPUs for your control node machine( settings/system).
- Configure networking for your machines:
192.168.122.X, where x is 10(k8s-control), 11(k8s-a), 12(k8s-b), 13(k8s-c)
- Make sure your new machines can work, ping each other and the internet

## End Results

- You should have:
  - a VmWare installation
  - 3 kubernetes worker machines: k8s-a, k8s-b, k8s-c
  - 1 kubernetes control machine: k8s-control
  - 1 host machine



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

