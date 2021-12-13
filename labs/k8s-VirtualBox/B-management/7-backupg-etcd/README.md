# 6 - Backing up etcd

In this lab you will upgrade the cluster that was created in the last labs.

- [Control plane upgrade steps](#Control-plane-upgrade-steps)
- [Worker node upgrade steps](#Worker-node-upgrade-steps)

## Control plane upgrade steps

- Our first step would be to drain the node, as theoretically pods may be running there:  
**kubectl drain k8s-control --ignore-daemonsets**
