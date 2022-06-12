# ShareNOW_Challenge

Goal:  Write a microservice, that evaluates the current status of a cluster, by watching all running pods in a cluster and evaluating some rules


1. Install Docker 

Intall [Docker Desktop](https://docs.docker.com/desktop/) 


2. Create a local environment where kubernetes clusters can run with [Kind](https://kind.sigs.k8s.io/docs/user/quick-start)


To install kind on MAC use the following command on a Terminal 

```
brew install kind
```
Once installed. Create a cluster along with config.yaml file. Config.yaml doesn't contain nodes

```
kind create cluster --name cluster --config config.yaml
```


Create another clusters along with config_nodes.yaml, this yaml files contains workers and control-plane.

```
kind create cluster --name cluster --config config_nodes.yaml
```

Once clusters are created, check the clusters created 
```
Kind get clusters
```

Check for running containers with the following commaned 

```
docker ps
```

Now check to validate that you have a healthy Kubernetes environment

```
kubectl get nodes
```


Get list of pods
```
kubectl get pods
```


2. Microservice deploymeent 

Microservice will be written in python and must be containerized using Docker

- Dockerize python file and create Docker image 
- 



