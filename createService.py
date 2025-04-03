import time
from kubernetes import client, config
from kubernetes.client.rest import ApiException


def create_service(namespace="default", service_name="flask-service", deployment_name="my-app-deployment"):
    
    config.load_kube_config()
    
    
    api_instance = client.CoreV1Api() #tworzy klienta dla API Services
    
    
    #definiujemy serwis
    
    service = client.V1Service(
        metadata=client.V1ObjectMeta(name=service_name),
        spec=client.V1ServiceSpec(
            selector={"app": "my-app"},
            ports=[client.V1ServicePort(
                protocol="TCP",
                port=80,
                target_port=80
            )],
            type="LoadBalancer"
        )
    )
    
    #tworzymy serwis
    
    try:
        odp = api_instance.create_namespaced_service(namespace=namespace, body=service)
        print(f"Serwis {service_name} został utworzony")
    except ApiException as e:
        print(f"Błąd podczas tworzenia serwisu: {e}")
        
    while True:
        try: 
            service_info = api_instance.read_namespaced_service(service_name, namespace)
            if service_info.status.load_balancer and service_info.status.load_balancer.ingress:
                external_ip = service_info.status.load_balancer.ingress[0].ip
                if external_ip:
                    print(f"Serwis dostępny pod adresem: http://{external_ip}")
                    break
        except ApiException as e:
            print(f"Błąd podczas sprawdzania statusu: {e}")
        
        print("Czekam na przypisanie adresu...")
        time.sleep(5)
        
create_service(namespace="default", service_name="flask-service", deployment_name="my-app-deployment")