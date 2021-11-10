
Prepare:
  - install (or upgrade) VirtualBox
  - Install (or upgrade) GNS3 (requires registration)
    To upgrade first uninstall (win-x -> apps & features -> find gns3 -> uninstall)
    Check "Gns3 VM", later choose VirtualBox
  - Download the gns3 VM, extract it and import to VirtualBox.
    Then use is from gns3 (see help-> setup wizard)
    Increase vcpu and memory when you do so
  - If all goes well, you should see two green lights:
        Desktop...
        GNS VM....


 


--------------------------------------------

Virtual Machines - Run in VirtualBox
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
     - Clone when machine is not working
     - Rename your new machine (master, worker..etc)
     - right-click clone
     - create new MAC addresses
     - Full clone !!!
  - Make sure your new machines can work

--------------------------------------------

IP addresses for nodes:
- These are Centos nodes.
- Address range should be: 192.168.122.0/24  (I'll explain why later)
- Configure static IP addresses for master and workers:
   sudo vi /etc/sysconfig/network-scripts/ifcfg-ens33
   change:
	BOOTPROTO=static
	IPADDR=192.168.122.x (where x is 1,2,3 for workers, 10 for master)
	NETMASK=255.255.255.0
	GATEWAY=192.168.122.100
   to restart networking:
	nmcli networking off
	nmcli networking on

--------------------------------------------
  Add your machines in GNS3

  - First, both "local server" and "GNS3 VM" server should run.
    They start automatocally when you run GNS3, but it may take a minute.
  - Start edit/preferences, look for VirtualBox and add your machines from there.
  - Add a simple Switch
  - Connect all machines to the switch
  - Add a "Nat Device"

-------------------------------------------


Connect to master and nodes:

I'm using a local Linux (Ubuntu-20) as a host, to control master and nodes.

   - Create a new ssh keypair: 
          ssh-keygen 
   - copy the key to each machine (you may have problems with fingerprints..)
          ssh-copy-id osboxes@192.168.122.1
   - Now connect like this:
          ssh osboxes@192.168.122.1

Use Terminator (See here: https://dev.to/xeroxism/how-to-install-terminator-a-linux-terminal-emulator-on-steroids-1m3h)
You can then login and command all nodes at once.

-

     