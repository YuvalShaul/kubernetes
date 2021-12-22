# 8 - Users

Use this lab to learn about k8s **normal** users.  
Use [this link](https://kubernetes.io/docs/reference/access-authn-authz/authentication/) to read a little about users in kubernetes.

- [Preparations](#Preparations)

## Reading the admin user

After creating your cluster (using **kubeadm**) you'll have this file:  
**/etc/kubernetes/admin.conf** just on your control node(s).  
This file is an exact copy of the **~/.kube/config**  config file you are using with your kubectl commands.

- Edit and copy the **client-certificate-data** part of this file.  
Make sure you copy just the base64 part, nothing else.
- Paste this into a new file called cert64
- Use the base64 tool to convert it:  
**base64 -d cert64 > cert-text**
- Now use **openssl** to read the certificate:  
**openssl x509 -in cert-text  -noout -text**
- The user name is taken from the **Subject** field:  
**Subject: O = system:masters, CN = kubernetes-admin**  
so the **CN (Common Name)** is used by kubernetes as the user name.


