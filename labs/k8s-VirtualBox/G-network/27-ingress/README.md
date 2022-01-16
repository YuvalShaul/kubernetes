# 27 - Kubernetes Ingress

We'll use this lab to demonstrate k8s ingress.

- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)


## Ingress Controller

- We'll be using the [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/)
- Install ingress controller as explained in [this section](https://kubernetes.github.io/ingress-nginx/deploy/#bare-metal-clusters).  
We are using the option that installs the ingress service as a NodePort service.  
This is the way it's going to communicate with the external world (the simplest way).  
Please verify:  
**kubectl get services -n ingress-nginx**  
(look for the service type)
- Read carefully the installation response:  
  - A new namespace called **ingress-nginx** is created
  - A new config maps is created for the controller configuration
  - Several roles, cluster roles and bindings for them
  - 2 services
  - A deployment
  - An ingressclass!!!
  etc.
- Verify that an ingress class was already created for us during the installation:  
**kubectl get ingressclasses**


