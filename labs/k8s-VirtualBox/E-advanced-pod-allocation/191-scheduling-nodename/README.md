# 19 - Scheduling nodeName Lab

Use this lab to demonstrate **nodeName** scheduling configuration.

- [Create a nodeName pod](#Create-a-nodeName-pod)



## Create a nodeName pod (k8s-b)

- Look at the **name-pod.yaml** file from this lab:  
It uses nodeName to directly select a specific node.  
**Change the node name to the corect name within your cluster (I have chosen k8s-b**.
- Create your pod by applying the file:  
**kubectl apply -f name-pod.yaml**
- Make sure your pod is running in the correct node:  
**kubectl get pods -o wide**
- Delete the pod


## Create a nodeName pod (k8s-control)

- Specifying the node directly is powerfull.  
What if we directly chose the control node?  
(remember that there is a taint preventing pods to run there)
- Edit the **name-pod.yaml** file to specifically name the control node.
- Apply the file again.  
Verify that the pod is running on the control node.
- Don't remember to delete the pod when you're done.

