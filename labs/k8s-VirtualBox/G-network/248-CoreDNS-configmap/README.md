# 248 - CoreDNS server Configuration

In this lab we experience the configuration of the CoreDNS service.

- [How to configure the CoreDNS service](#How-to-configure-the-CoreDNS-service)
- [A single server block](#A-single-server-block)
- [Multiple server blocks](#Multiple-server-blocks)

## How to configure the CoreDNS service

- The CoreDNS service is configured through a configmap called **coredns** in the **kube-system** namespace (go and verify that!).
- The main part of the configuration is a "Corefile" configuration that is transferred directly to the CoreDNS configuration.
- To use this configuration you have to do the following:
  - Apply the ConfigMap file:  
  **kubectl apply -f \<yaml file\>**
  - Force CoreDNS to use it by rolling out the CoreDNS deployment:  
  **kubectl rollout restart -n kube-system deployment/coredns**

## A single server block

- Look carefully at **CoreDNS-configmap-1.yaml** from this lab.
  - There is just ONE server block there.
  - I takes care of ALL domain names.
  - Currently, if name resolution fails, it forward the request to whatever is defined in /etc/resolv.conf file (of the Node).
  - Verify that ping to **\<ip-address-of-you-pod\>.pod.cluster.loca** works.
  - Verify that ping to **google.com** works
- Remove the following line (don't forget to re-apply the configuration):  
**forward . /etc/resolv.conf**  
Now try to ping both destinations again. What's the difference?

## Multiple server blocks

- Look at the 2nd file:  **CoreDNS-configmap-2.yaml**:
  - The first block now takes care ONLY for domains with suffix **cluster.local**
  - THERE IS a forward to default server in the block..but still...
  - Try to ping **google.com**
- Since it's clear that **google.com** domain name is not taken care of this block, let's add a block for **google.com** (it is comment-out)
  - Uncomment the block and remember to reload the configuration as explained.
  - Try to ping **google.com** (or domains that suffix) again.
  - Try to ping your pod again.
  - ...AND...try to ping other domain names (cnn.com  aws.com ...)


So this is how you can create your "mini DNS servers" using CoreDNS.