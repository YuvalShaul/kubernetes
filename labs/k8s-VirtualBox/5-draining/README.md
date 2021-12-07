# 5 - Safely Draining a node

In this lab you will install and configure **kubectl** on your host machine.

- [Creating a pod and a deployment](#Creating-a-pod-and-a-deployment)


## Creating a pod and a deployment

- 
- Use the pod.yml and deployment.yml file from this lab.
apply both of them to your cluster:  
**kubectl apply -f pod.yml**  
**kubectl apply -f deployment.yml**
- Make sure that the pod and deployment have beed applied correctly:
**kubectl get pods -o wide**  
Use the output wide option, so that you can see on which node each pod runs.
- We have 3 worker nodes, 3 replicas in our deployment.  
Since we added another single pods, we should have a single node with 2 pods running on it, one pod from the single pod.yml definition, and one from the deployment.yml definition.
- We'll drain the pod (the one with 2 pods and different origins on it).  
**kubectl drain <node name>**  
You'll see that the single pod (that is not part of  ReplicationController, ReplicaSet, Job, DaemonSet or StatefulSet) cannot be deleted.  
The other reason is that the drain command cannot delete those DaemonSet-managed Pods (in this case these are kube-system pods).
- I'll need two flags to get rid of those error messages:  
**kubectl drain <node name> --ignore-daemonsets --force**  
The --force will DELETE the first pod.  
- Let's look at the outcome:  
**kubectl get pods -o wide**  
- Clean everything:  
**kubectl delete -f pod.yml**  
**kubectl delete -f deployment.yml**
