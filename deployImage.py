from kubernetes import client, config
from kubernetes.client.rest import ApiException


config.load_kube_config() #załączenie kubeconfig


def create_deployment(image_name):

    container = client.V1Container(
        name="my-app",
        image=image_name,
        ports=[client.V1ContainerPort(container_port=80)]
    )

    #specyfikujemy deployment

    spec = client.V1PodSpec(containers=[container])
    template = client.V1PodTemplateSpec(metadata=client.V1ObjectMeta(labels={"app": "my-app"}), spec=spec)
    selector = client.V1LabelSelector(match_labels={"app": "my-app"})
    deployment_spec = client.V1DeploymentSpec(replicas=3, template=template, selector=selector)

    deployment = client.V1Deployment(
        #tworzymy deployment
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name="my-app-deployment"),
        spec=deployment_spec
    )

    api_instance = client.AppsV1Api()


    try:
        api_instance.create_namespaced_deployment(
            namespace="default",
            body=deployment
        )
        print("Utworzono deployment")
    except ApiException as e:
        print(f"Blad podczas tworzenia deploymentu: {e}")


create_deployment("turzynskimaks/simple_app:latestest")