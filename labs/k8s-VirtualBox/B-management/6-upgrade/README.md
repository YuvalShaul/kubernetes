# 6 - Upgrading out cluster

In this lab you will upgrade the cluster that was created in the last labs.

- [Control plane upgrade steps](#Control-plane-upgrade-steps)
- [Worker node upgrade steps](#Worker-node-upgrade-steps)

## Control plane upgrade steps

- Our first step would be to drain the node, as theoretically pods may be running there:  
**kubectl drain k8s-control --ignore-daemonsets**
- Now, let's upgrade kubeadm:  
**sudo yum install -y kubeadm-1.22.2-00**
- Use **kubeadm version** to see that the package it has updated.
- Use the **kubeadm plan** to see what's going to take place:  
**sudo kubeadm upgrade plan v1.22.2**  
Look at the output.  
Notice the packages that are going to be upgraded.  
The plan command offers you the apply command you should now use.
- Now let's use that command to apply.  
You will be prompted to see if you want to proceed.
- If you got these happy success messages (SUCCESS! Your cluster was upgraded to "v1.22.2". Enjoy!), it means we can go on to upgrade the other packages:   
**sudo yum install -y kubelet-1.22.2-00 kubectl-1.22.2-00**
- To make sure that if the kubelet service file has changed, the service is restarted, use the following commands:  
**sudo systemctl daemon-reload** 
**sudo systemctl restart kubelet**
- Last step:
Remember that you've drained your control node (you can use **kubectl get nodes** to see that).  
Uncordon it:  
**kubectl uncordon k8s-control**  
- Verify your control node has been upgraded to the new version:  
**kubectl get nodes**  

## Worker node upgrade steps

- These steps should be done with each node seperatelly.
- 