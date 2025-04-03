# Part.1
  Stawianie klastra kubernetes za pomocą Terraform, deployment oraz serwis powstają przy omocy kodu Pythonowego (pliki .bat uruchamiające kod)




  main.tf - Plik odpowiedzialny za utworzenie klastra kubernetes w GCP

  deployImage.bat - Tworzy deployment na bazie obrazu w rejestrze dockerHub

  checkDeployment.bat - Sprawdza stan deploymentu

  createService.bat - Tworzy serwis, a następnie wypisuje jego zewnętrzny adres IP

  /docker - W tym folderze znajduję się prosty obraz dockerowy, lekki i idealny do sprawdzenia działania projektu


