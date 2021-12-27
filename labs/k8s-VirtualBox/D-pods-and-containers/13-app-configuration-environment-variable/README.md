# 13 - Application Configuration

In this lab we are going to use a configmap.



- Create a configmap using the following command:  
**kubectl apply -f conf-map.yaml**  
(the file from this lab)
- Create a pod by applying the pod.yaml file in this lab:  
**kubectl apply -f pod.yaml**
- Notice the lines in the pod.yaml file that refer to the configmap
- Exec into the pod:  
**kubectl exec -it my-pod -- sh**
- Access the environment variable to see the value from the configmap:  
**echo $ENVPASS**


