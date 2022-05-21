# Using Namespaces

In this lab we are going to demonstrate container lifecycle hooks.  

- [Create the Python Image](#Create-the-Python-Image)

## A container without an OS

- Go into the **make-image** directory from this lab:  
**cd make-image**
- Login into your favorite docker repository.  
If you don't specify a registry (as in this example), you will login into the docker hub.  
You need your username and password for that.
**docker login**
- Edit the **makeit.sh** file from the lab.  
It is using the string **yuvalshaul** because this is my user name for docker hub.  
Please replace that (both lines) with your own user name.  
- Run the file:  
**source makeit.sh**  
This should build an image, and push it into the **python-counter** repository in your account.


## Run the python-counter pod

- If you look at the **python-counter.py** program, you'll see that it is a very simple loop and print program.
- The pod definition should be fixed:  
Again, change **yuvalshaul** to your own dockerhub user name.
- Run the pod:  
**kubectl apply -f python-pod.yaml**
- Make sure your pod is running:  
**kubectl get pods**

## Trying to debug networking

- Let's imaging that for some reason, we want to try to:  
  - ping 8.8.8.8 from the pod
  - use **tcpdump** to capture trafic
- Try that:  
**kubectl exec -it python-pod -- sh**  
**ping**  
**tcpdump**
- As you can see, these commands are not part of the image code, as I have used a slim version of Python base image.

## Ping from above

- First, get the ip address that the pod is using:  
(you will also get the node this pod is running at)  
**kubectl get pods -o wide**
- SSH into the node:  
(in my example this was k8s-b)  
**ssh osboxes@192.168.122.12**
- List namespaces here:  
**sudo ip netns list**
- We'll run **ip address show** inside each namespace, to find the namespace that matches our pod ip address:  
**sudo ip -all netns exec ip addres show**  
Look for the long namespace name at the beginning of each listing.  
You are trying to find the correct one, the one with the IP address of the pod


## Running a command from the namespace

- Now it is easy to run networking commands from the pod networking vide.  
Here's a **ping** example:  
**sudo ip netns exec cni-e4dbf8a4-35b9-67bd-460a-e525c21ff64d   ping 8.8.8.8**
- Another example, this time with **tcpdump**:  
**sudo ip netns exec cni-e4dbf8a4-35b9-67bd-460a-e525c21ff64d   tcpdump**