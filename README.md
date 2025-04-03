# terraformProject
Projekt testowy do nauki korzystania z Terraform

gcloud auth login //Załącza autoryzacje z googleCloud
gcloud config set project <project_id> //Wybiera projekt jako używany
gcloud container clusters get-credentials <cluster_name> --zone <zone> --project <project_id> //Pobiera plik kubeconfig, który konfiguruje całość połączenia

Part.1
  Stawianie klastra kubernetes za pomocą Terraform, deployment oraz serwis powstają przy omocy kodu Pythonowego (pliki .bat uruchamiające kod)

Part.2
  Faktyczny IaC, terraform stawia całą architekturę.
