# 18 - Init Containers

In this lab we are going to demonstrate init containers.

- Look at **init-containers-pod.yaml** file from this lab.
- It defines a pod with 2 init containers and 1 app container.
- Apply the file and then monitor it while the init continers are running:
  - **kubectl apply -f init-containers-pod.yaml**
  - **kubectl get pods**
  - Repeat several times, until the pod goes to a running state:
     - Wait for 10 seconds, then:  
**kubectl get pods**
