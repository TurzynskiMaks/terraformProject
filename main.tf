provider "google" {
  project = "ubuntu-418103"
  region  = "us-west1"
}

resource "google_container_cluster" "primary" {
  name     = "my-cluster"
  location = "us-west1-a"
  initial_node_count = 3
  deletion_protection = false

  node_config {
    machine_type = "e2-micro"
    disk_size_gb = 50
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform",
    ]
  }
}
