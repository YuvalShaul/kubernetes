# 6 - Upgrading out cluster

In this lab you will upgrade the cluster that was created in the last labs.

- [Control plane upgrade steps](#Control-plane-upgrade-steps)
- [Worker node upgrade steps](#Worker-node-upgrade-steps)

## Control plane upgrade steps

- Our first step would be to drain the node, as theoretically pods may be running there:  
**kubectl drain k8s-control --ignore-daemonsets**
- Now, let's upgrade kubeadm - login to the control node itself first:  
**sudo yum install -y kubeadm-1.23.3-00**
- Use kubeadm version command to see that the package it has updated:  
**kubeadm version**
- Use the kubeadm plan command to see what's going to happen when you upgrade:  
**sudo kubeadm upgrade plan v1.23.3**  
  - Look at the output.  
  - Notice the packages that are going to be upgraded.  
  - Note the apply command offered to you
- Use the apply command that was offered in the last section (add sudo):  
  - **sudo kubeadm upgrade apply v1.2.......**
  - You will be prompted to see if you want to proceed.
  - The upgrade process pulls images from a registry (Dockerhub by default)
  - Wait for: **[upgrade/successful] SUCCESS! Your cluster was upgraded to "v1......". Enjoy!**  
- If you are seccessfull, you should go on to upgrade the other packages:   
**sudo yum install -y kubelet-1.23.3-00 kubectl-1.23.3-00**
- To make sure that if the kubelet service file has changed, the service is restarted, use the following commands:  
  - **sudo systemctl daemon-reload** 
  - **sudo systemctl restart kubelet**
- Last step:
Remember that you've drained your control node (you can use **kubectl get nodes** to see that).  
Uncordon it:  
**kubectl uncordon k8s-control**  
- Verify your control node has been upgraded to the new version:  
**kubectl get nodes**  

## Worker node upgrade steps

Repeat these steps for each worker node:
- GO TO THE CONTROL-PLANE NODE!!!
- Drain the node:
**kubectl drain k8s-a --ignore-daemonsets --force**  
(just in case we have a stand alone pod there).
- NOW GO TO THE WORKER NODE!!!
- In the worker node itself !!!  
We'll upgrade kubeadm:  
**sudo yum install -y  kubeadm-1.23.3-00**
- Now use **kubeadm** to upgrade the node:  
**sudo kubeadm upgrade node**  
(this is mostly changes to configuration files)  
- Now we can upgrade **kubectl** and **kubelet**:  
**sudo yum install -y kubelet-1.23.3-00 kubectl-1.23.3-00**
- To make sure that if the kubelet service file has changed, the service is restarted, use the following commands:  
  - **sudo systemctl daemon-reload** 
  - **sudo systemctl restart kubelet**
- GO BACK TO THE CONTROL-PLANE NODE:
Uncordon the worker node:  
**kubectl uncordon k8s-a**  
- Verify your control node has been upgraded to the new version:  
**kubectl get nodes**  