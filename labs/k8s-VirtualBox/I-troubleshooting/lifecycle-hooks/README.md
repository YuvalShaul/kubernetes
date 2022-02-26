# Lifecycle Hooks

In this lab we are going to demonstrate container lifecycle hooks.  
We are going to create a Python image, one that has OS and shell in it, so we can exec into it.
The Python program that will run in the pod we'll create can respond to SIGINT signals, and we'll configure the pod to send this signal when it is deleted.

- [Create the Python Image](#Create-the-Python-Image)
- [Create your pod](#Create-your-pod)
- [Delete the pod](#Delete-the-pod)

## Create the Python Image

- You should create a repository called **python-exit** in your dockerhub account.
- Login manually to your dockerhub account:  
**docker login**
- Go into the **make-image** directory:  
**cd make-image**
- Edit the **makeit.sh** file, and replace **yuvalshaul** with your own dockerhub username.
- run the shell script:  
**source makeit.sh**  
It will build an image, and try to push it to **python-exit** repository in your dockerhub account.

## Create your pod

- Create a pod using the built image, using the file from this lab:  
**kubectl apply -f good-exit-pod.yaml**
- Split your screen to see logs from this pod:  
**kubectl logs good-exit-pod**  
You should see just a single line (pod has started)
- Delete the pod:  


## Delete the pod

**kubectl delete -f good-exit-pod.yaml**
- You should see some lines that verify that the Python program has received the SIGINT signal.
