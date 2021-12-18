# 7 - kubectl Lab

Use this lab to get some hands-on experience with kubectl commands.

- [Preparations](#Preparations)
- [Experiment with kubectl](#Experiment-with-kubectl)
- [JSONPATH](#JSONPATH)

## Preparations

create the following deployments:
- **kubectl apply -f many-pods1.yaml**
- **kubectl apply -f many-pods2.yaml**

## Experiment with kubectl

- Get a list of pods:  
**kubectl get pods**
- Get a wider description for each pod (including the node this pod is running on):  
**kubectl get pods -o wide**
- Get a single pod:  
**kubectl get pods busybox-deployment-......**  (pick one of your pods from the last command)  
- Explore the json format you get from this pod:  
**kubectl get pods busybox-deployment-.... -o json**
- Use a jsonpath to view specific data from the json output:  
**kubectl get pods busybox-deployment-2-857d87cbc4-p8p7f -o jsonpath='{.spec.nodeName}'**  
(you should get the node name the pod is running at)
- 


## JSONPATH

The jsonpath language can be used to select parts of the json output.  
It was inspired by XPath, a similar language for 
The closest document to a standard for jsonpath can be found [here](https://goessner.net/articles/JsonPath/).  
You can use [this](https://docs.oracle.com/cd/E60058_01/PDF/8.0.8.x/8.0.8.0.0/PMF_HTML/index.htm#t=JsonPath_Expressions.htm%23Path_Examplesbc-4&rhtocid=10.2.0_4) guide as well.  

- Try:  
**kubectl get pods -o jsonpath='{$}'**  
Notice that the result is for multiple items, and you get a single json object with an "items" property.
- Try:  
**kubectl get pods -o jsonpath='{$.items}'*  
(now the result is an array)
- Try:  
**kubectl get pods -o jsonpath='{$.items[1]}'**  
(and this is a sinle pod)
- Try:  
**


**kubectl get pods -o wide --sort-by .spec.nodeName**




List the pods with the label given to the second deployment:  
**kubectl get pods --selector=app=busybox-2**

