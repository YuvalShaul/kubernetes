# 5 - Safely Draining a node

In this lab you will safely drain a kubernetes node, i.e. empty it of all pods.  
You may want to do that as part of a maintenance.  S

- [Creating a pod and a deployment](#Creating-a-pod-and-a-deployment)
- [Safely drain a node](#Safely-drain-a-node)

## Creating a pod and a deployment

- Use the pod.yml and deployment.yml file from this lab.
apply both of them to your cluster:  
**kubectl apply -f pod.yml**  
**kubectl apply -f deployment.yml**
- Make sure that the pod and deployment have beed applied correctly:
**kubectl get pods -o wide**  
We use the output wide option (-o wide), so that you can see on which node each pod runs.
- We have 3 worker nodes, 3 replicas in our deployment.  
Since we added another single pods, we should have a single node with 2 pods running on it, one pod from the single pod.yml definition, and one from the deployment.yml definition.  
Thats the pod we want to drain.  

## Safely drain a node

- We'll drain the node with 2 pods on it:  
**kubectl drain \<node name\>**
- We should get some error messages here:  
  - 1 The single pod cannot be deleted.
  - 2 The drain command cannot delete those daemonSet-managed Pods (in this case these are kube-system pods).
- Let's use these two flags to overcome the error messages:  
**kubectl drain <node name> --ignore-daemonsets --force**  
The --force will DELETE the first pod.  
The --ignore-daemonsets to succeed without deleting daemonsets pods.  
- Let's look at the outcome:  
**kubectl get pods -o wide**  
- Clean everything:  
**kubectl delete -f pod.yml**  
**kubectl delete -f deployment.yml**
