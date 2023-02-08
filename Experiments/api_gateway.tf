resource "google_api_gateway_api" "api" {
  provider = hashicorp-google-beta
  project  = var.project_id
  api_id   = "${var.project_id}-api-gateway"

}

resource "google_api_gateway_api_config" "api_cfg" {
  provider      = hashicorp-google-beta
  project       = var.project_id
  api           = google_api_gateway_api.api.api_id
  api_config_id = "${var.project_id}-api-configs"
  openapi_documents {
    document {
      path     = "config.yaml"
      contents = filebase64("signed_url/config/config.yaml")
    }
  }
  depends_on = [
    google_api_gateway_api.api
  ]
  gateway_config {
    backend_config {
      google_service_account = "test-541@programiv.iam.gserviceaccount.com"
    }
  }
}

resource "google_api_gateway_gateway" "gateway" {
  provider   = hashicorp-google-beta
  project    = var.project_id
  region     = "us-central1"
  api_config = google_api_gateway_api_config.api_cfg.id # THIS MUST BE .ID FOR WHATEVER REASON
  gateway_id = "public"
  depends_on = [
    google_api_gateway_api_config.api_cfg,
    google_api_gateway_api.api
  ]
}