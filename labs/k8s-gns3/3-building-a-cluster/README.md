# Building a K8S Cluster

This lab will guide you through the process of K8S cluster creation.
By now, you should have already done labs 1 ()

## Setting host names
It is easier to work with meaningfull hostname.
Command:
  **sudo hostnamectl set-hostname <host-name>**  (e.g: k8s-a, k8s-b, k8s-c k8s-control)
Then, logout and login, to enable the change.

## Edit /etc/hosts

Make it easier to access each host.
Update all /etc/hosts files to know each other.
Here are the lines I added to all of my master and nodes:
192.168.122.10 k8s-control
192.168.122.11 k8s-a
192.168.122.12 k8s-b
192.168.122.13 k8s-c

## Enable kernel modules for containerd

cat << EOF | sudo tee /etc/modules-load.d/containerd.conf
> overlay
> br_netfilter
> EOF

Explanation:
- The **cat** command is reading from a [here document](https://tldp.org/LDP/abs/html/here-docs.html).
To understand here docs, try them with a word different from EOF.
I have tried it with my name:
*cat << yuval
Hello
from a
here doc.
yuval*
- The **tee** command is reading the output of cat (that's because of the **|** pipeline symbol).
It will output the text to both the file in action, and the standard output.
(You can **cat** that file, and see that the commands are there).
So the kernel will load these module.






