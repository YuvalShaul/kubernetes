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

