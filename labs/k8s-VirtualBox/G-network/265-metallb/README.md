# 265 - MetalLB Load Balancer Services

In this lab we experience the use and configuration of MetalLB.

- [MetalLB Installation](#MetalLB-Installation)
- [MetalLB Configuration](#MetalLB-Configuration)
- [Multiple server blocks](#Multiple-server-blocks)


## MetalLB Installation

- MetalLB is installed by applying two manifest files from the metallb site.  
(See **[Installation by a manifest](https://metallb.universe.tf/installation/#installation-by-manifest)**  for more details.
- The first YAML file will create a namespace (**metallb-system**).  
Install:  
**kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.12.1/manifests/namespace.yaml**
- The second YAML will all the rest.  
Install:  
**kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.12.1/manifests/metallb.yaml**


## MetalLB Configuration

- MetalLB remains idle until configured. This is accomplished by creating and deploying a config map into the same namespace (metallb-system) as the deployment.
- We are using a layer-2 configuration, explained [here](https://metallb.universe.tf/configuration/#layer-2-configuration).
- Look at the **metallb-conf.yaml** file from this lab. It defines a range of IP addresses to be used as an external facing load balancer addresses.

## MetalLB loadbalancer Service

- First apply the deployment from this lab:  
**kubectl apply -f svc-deployment.yaml**
- Then apply the service:  
**kubectl apply -f lb-service.yaml**
- Discover the external IP address used by the service:  
**kubectl get services**
- Use curl command to make sure the service is working:  
**curl <service-external-ip-address>