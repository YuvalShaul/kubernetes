# 20 - Daemonsets

Use this lab we'll demonstrate the use of daemonsets.

- [Create a daemonset](#Create-a-daemonset)
- [](#)

## Create a daemonset

- Look at the **daemonset-one.yaml** file from this lab.  
It creates a daemonset that cleans up a volume each 10 seconds.
- Create the daemonset by applying the file:  
**kubectl apply -f daemonset-one.yaml**
- Verify:  
**kubectl get pods -o wide**
- You can exec into each of these pods to see that those volumes are really cleared.
