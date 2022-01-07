# 7 - kubectl Lab

Use this lab we'll demonstrate **nodeSelector** and **nodeName** configurations.

- [Assign labels to nodes](#Assign-labels-to-nodes)
- [Create your pod](#Create-your-pod)

## Assign labels to nodes

- List your nodes:  
**kubectl get nodes**
- Label your node, by following this example:  
**kubectl label nodes k8s-b special=yep**
- You can see that label by describing the node:
**kubectl describe nodes <node-name>**

## Create your pod

- Look at the **select-pod.yaml** file from this lab:  
It uses nodeSelector to select a specific node.  
**Change the lable name and value to those you have configured to your node**.
- Create your pod by applying the file:  
**kubectl apply -f select-pod.yaml**

