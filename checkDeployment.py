from kubernetes import client, config
from kubernetes.client.rest import ApiException


config.load_kube_config() 

def list_deployments(namespace="default"):
    api_instance = client.AppsV1Api()
    try:
        deployments = api_instance.list_namespaced_deployment(namespace=namespace)
        for deploy in deployments.items:
            print(f"Deployment: {deploy.metadata.name}")
    except ApiException as e:
        print(f"Blad podczas pobierania listy deploymentów: {e}")

def check_deployment_status(deployment_name="my-app-deployment", namespace="default"):
    api_instance = client.AppsV1Api()
    try:
        deployment = api_instance.read_namespaced_deployment_status(deployment_name, namespace)
        print(f"Status: {deployment.status.available_replicas} replicas available")
    except ApiException as e:
        print(f"Blad podczas sprawdzania statusu deploymentu: {e}")


list_deployments("default")
check_deployment_status("my-app-deployment", "default")
