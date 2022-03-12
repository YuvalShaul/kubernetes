# 24 - DNS Pod Configuration

We'll use this lab to demonstrate DNS configuration done at the pod level.

- [Cluster DNS service address](#Cluster-DNS-service-address)
- [DNS ClusterFirst pod configuration](#DNS-ClusterFirst-pod-configuration)
- [](#)
- [](#)
- [](#)
- [](#)

## Cluster DNS service address

- Run the following command to view the cluster DNS ip address, used by the DNS service:  
**kubectl get services kube-dns -n kube-system**

## DNS ClusterFirst pod configuration

- Look at the **dns-ClusterFirst-pod.yaml** file from this lab.  
It runs a **nicolaka/netshoot** image that contains many communication tools.  
This is the real default configuration for pods.  
To understand the DNS behaviour of the pod, do the following steps.
- Apply the file to create the pod:  
**kubectl apply -f dns-ClusterFirst-pod.yaml**
- Exec into the pod:  
**kubectl exec -it dns-pod -- sh**
- Run **nslookup**, and enable debug mode:  
**nslookup**  (this will get you into nslookup interractive mode)
**set debug**
- Type **server** to see the currently used server.  
Note that this is the cluster DNS service IP address.
- Type **hslkjhslkrjh.com** (this is a dns name that does not exist).  
Note the order that the DNS query takes (here it is in my installation):  
hslkjhslkrjh.com.**default**.svc.cluster.local, type = A, class = IN  
hslkjhslkrjh.com.**svc**.cluster.local, type = A, class = IN**  
hslkjhslkrjh.com.**cluster.local**, type = A, class = IN  
hslkjhslkrjh.com, type = A, class = IN


