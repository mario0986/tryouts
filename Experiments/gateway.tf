# Any modifications to these components, requires to delete all the resources and create them it again
# Api Gateway is inmutable therefore doesnt handle updates well on tfplan

resource "google_api_gateway_api" "api" {
  provider = hashicorp-google-beta
  project  = var.project_id
  api_id   = "alberto-api-gateway-${terraform.workspace}" # To be([a-z0-9-]+) compliant  
}

resource "google_api_gateway_api_config" "api_cfg" {
  provider      = hashicorp-google-beta
  project       = var.project_id
  api           = google_api_gateway_api.api.api_id
  api_config_id = "alberto-api-gateway-config-${terraform.workspace}"

  openapi_documents {
    document {
      path     = "config.yaml"
      contents = filebase64("misc/signed_url/config/config.yaml")
    }
  }

  gateway_config {
    backend_config {
      google_service_account = "384772844928-compute@developer.gserviceaccount.com"
    }
  }

  depends_on = [
    google_api_gateway_api.api
  ]
}

resource "google_api_gateway_gateway" "gateway" {
  provider   = hashicorp-google-beta
  project    = var.project_id
  region     = var.region_id
  api_config = google_api_gateway_api_config.api_cfg.id # THIS MUST BE .ID FOR WHATEVER REASON
  gateway_id = "public"

  depends_on = [
    google_api_gateway_api_config.api_cfg,
    google_api_gateway_api.api
  ]
}
