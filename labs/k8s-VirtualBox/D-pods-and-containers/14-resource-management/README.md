# 14 - Resource management

In this lab we are going to demonstrate resource requests.

- [Create a config map](#Create-a-config-map)

## Too many cpus required

- Look at **big-cpu-pod.yaml** from this lab.  
These are the requirements of this pod:
  - memory: "50M", which means 50 mega bytes (50 * 10^6 bytes)  
  We could also use: "50Mi" which means 50 **mebi** (50 * 2^20 bytes)
  - cpu: 60 cpu units (so 60 virtual cpus)  
  Of course, we only have 2 virtual cpus in the control node.
  - Try to apply this file and create the pod:  
  **kubectl apply -f big-cpu-pod.yaml**
  - Use **kubectl get pods** and **kubectl describe pods** to see what happened.
  - Learn more about prefixes used to describe these quantities:
    - [prefixes for decimal SI units](https://physics.nist.gov/cuu/Units/prefixes.html)
    - [prefixes for binary multiples](https://physics.nist.gov/cuu/Units/binary.html)
  
## Too much memory required

- Look at **big-mem-pod.yaml** from this lab.  
These are the requirements of this pod:
  - memory: "64Gi", which means 64 gibi bytes (64 * 2^30 bytes)  
  - cpu: 250m so 250 mili cpu units, or 0.25
  - Try to apply this file and create the pod:  
  **kubectl apply -f big-mem-pod.yaml**
  - Use **kubectl get pods** and **kubectl describe pods** to see what happened.