terraform {
  backend "gcs" {
    bucket = "mario-tfstate"
    prefix = "infra"
  }
  required_providers {
    hashicorp-google = {
      source  = "hashicorp/google"
      version = ">= 3.51, < 5.0"
    }
    hashicorp-google-beta = {
      source  = "hashicorp/google-beta"
      version = ">= 3.51, < 5.0"
    }
  }
}




