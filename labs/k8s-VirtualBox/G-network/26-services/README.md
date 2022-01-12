# 26 - Services

We'll use this lab to demonstrate services.

- [](#)

## Create a deployment

- Look at **svc-deployment.yaml** from this lab.  
It contains a deployment that run 3 replicas of an Nginx server.  
Apply it:  
**kubectl apply -f svc-deployment.yaml**
- View the pods, and exec into the first pod:  
**kubectl get pods**  
**kubectl exec -it \<pod name\> -- sh**
- Rewrite the main html file with this text:  
**echo "AAAAA" > /usr/share/nginx/html/index.html**
- Repeat this process with the 2nd and 3rd pods, but use "BBBBB" and "CCCCC" accordingly.

## Create a service

- Look at the **cluster-ip.yaml** file from this lab.  
It creates a service of the cluster-ip type.  
This service uses the pods that were created by the **svc-deployment.yaml**.  
- Create the service:  
**kubectl apply -f cluster-ip.yaml**
- Verify that the service was created and get the service IP address:  
**kubectl get services**

## Use the ClusterIP service

- Create a busybox pod to use as a client:  
**kubectl apply -f pod.yaml**
- Exec into this pod:  
**kubectl exec -it client-pod -- sh**
- Use curl repeatedly to get the main page of the service.  
Since you have changed your pods to respond with different replies, you should be able to see how the service load balancing works.  
**curl \<service-IP-address\>**





