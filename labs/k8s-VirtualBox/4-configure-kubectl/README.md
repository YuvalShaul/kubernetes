# 4 - kubectl Lab

In this lab you will install and configure **kubectl** on your host machine.

- [VirtualBox](#Virtual-Box)
- [K8S Virtual Machines](#K8S-Virtual-Machines)
- [Host Machine](#Host-Machine)
- [Host Machine](#Host-Machine)
- [End Results](#End-Results)


## kubectl installation

- Install **kubectl** on your host machine:  
**sudo yum install -y kubectl**
- After the installation, you should verify the existence of the $HOME/.kube directory.  
If it does not exist - create it.
- Use the **scp** (ssh copy) command to copy the config file from the control node.  
**cd .kube**  
**scp osboxes@192.168.122.10:.kube/config .**  
This will copy the **config** [configuration file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) into your host machine.
- Use the **kubectl cluster-info** command to see if you get the details of the cluster correctly.
- Try **kubectl get nodes** command.
