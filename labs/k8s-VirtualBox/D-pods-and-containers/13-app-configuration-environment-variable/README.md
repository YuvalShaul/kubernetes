# 13 - Application Configuration

In this lab we are going to use a configmap.

- [Xreate a config map](#Create-a-config-map)

## Create a config map

- Look at the conf-map.yaml file from this lab. It defines a configmap called my-config-map.
- Type:  
**echo "hello world" | base64**  
to see how we got the base64 value attached to **binaryData**.
- Create this configmap using the following command:  
**kubectl apply -f conf-map.yaml**  
- Verify that the configmap has been created:  
**kubectl get configmaps**
- Look at the details of this configmap:  
**kubectl describe configmap m-config-map**  

## Create a secret


- Create a pod by applying the pod.yaml file in this lab:  
**kubectl apply -f pod.yaml**
- Notice the lines in the pod.yaml file that refer to the configmap
- Exec into the pod:  
**kubectl exec -it my-pod -- sh**
- Access the environment variable to see the value from the configmap:  
**echo $ENVPASS**


