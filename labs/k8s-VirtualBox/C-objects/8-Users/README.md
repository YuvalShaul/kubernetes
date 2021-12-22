# 8 - Users

Use this lab to learn about k8s **normal** users.  
Use [this link](https://kubernetes.io/docs/reference/access-authn-authz/authentication/) to read a little about users in kubernetes.

- [Reading the admin user name](#Reading-the-admin-user-name)

## Reading the admin user name

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


## Create a new user

- First, we need to get the root certificate and key for our Kubernetes clusters. Since the private key ca.key) should not be modes, we can do the whole thing in the control node, in the pki directory.
- Here are my commands (at the control node):
  - **sudo su**
  - **cd /etc/kubernetes/pki**
  - Looking at this directory I can find:
    - **ca.crt** (the Certificate Authority certificate/public key)
    - **ca.key** (the ca private key)
  - I'm going to create the user 'dave'.  
  Create a directory called "dave" and cd into it. Also copy ca files into it:  
    - **mkdir dave**
    - **cd dave**
    - **cp ../ca.\*  .**
  - Create a private key for dave:  
  **openssl genrsa -out dave.key 2048**  
  (there should be now a file called dave.key)
  - Now create a csr (Certificate Signing Request), to prepare everything needed to the actual certificate creation.  
  Note that this is where we set the user name (and also the group name):    
  **openssl req -new -key dave.key -out dave.csr -subj "/CN=dave /O=developers"**
  - Now, to the actual signing of the certificate:  
  **openssl x509 -req -in dave.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out dave.crt -days 3540**
  - We can remove the files now not needed:  
    - **rm dave.csr**
    - **rm ca.srl**
  - Im changing the file permissions for these files (so I can copy them):  
  **chmod 777 dave.\***
  - Go into my host computer, and copy the files:  
    - **scp osboxes@192.168.122.10:/etc/kubernetes/pki/dave/dave.crt .**
    - **scp osboxes@192.168.122.10:/etc/kubernetes/pki/dave/dave.key .**
  - remove the files from the control node.
