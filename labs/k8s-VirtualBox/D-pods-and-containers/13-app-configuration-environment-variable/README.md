# 13 - Application Configuration

In this lab we are going to use a configmap.

- [Create a config map](#Create-a-config-map)

## Create a configmap

- Look at the **my-configmap.yaml** file from this lab.  
It defines a [configmap object](https://kubernetes.io/docs/concepts/configuration/configmap/#configmap-object) called my-configmap.
- How did we get the base64 value attached to **binaryData** ?  
type:  
**echo "hello world" | base64**  
- Create this configmap using the following command:  
**kubectl apply -f my-configmap.yaml**  
- Verify that the configmap has been created:  
**kubectl get configmaps**
- Look at the details of this configmap:  
**kubectl describe configmap my-configmap**  

## Create a secret

- Look at the **my-secret.yaml** file in this lab.
- Here's how I get my secret encoded as base64:  
**echo 'mypassword' | base64**
- Create the secret:  
**kubectl apply -f my-secret.yaml**
- Verify that the secret was created:  
**kubectl get secrets**

## Use the configmap and secret in a pod using environment variables

- Create a pod by applying the pod.yaml file in this lab:  
**kubectl apply -f pod.yaml**
- Notice the lines in the pod.yaml file that refer to the configmap
- Exec into the pod:  
**kubectl exec -it my-pod -- sh**
- Access the environment variable to see the value from the **configmap**:  
**echo $CONFIGMAP_VAR**
- Access the environment variable to see the value from the **secret**:  
**echo $SECRET_VAR**

## Create 
