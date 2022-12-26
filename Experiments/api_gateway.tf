resource "google_api_gateway_api" "api" {
  provider = hashicorp-google-beta
  project  = var.project_id
  api_id   = "${var.project_id}-api-gateway"
}

resource "google_api_gateway_api_config" "api_cfg" {
  provider      = hashicorp-google-beta
  project       = var.project_id
  api           = google_api_gateway_api.api.api_id
  api_config_id = "${var.project_id}-api-config"
  openapi_documents {
    document {
      path     = "config.yaml"
      contents = filebase64("signed_url/config/config.yaml")
    }
  }
}

resource "google_api_gateway_gateway" "gateway" {
  provider   = hashicorp-google-beta
  project    = var.project_id
  region     = "us-central1"
  api_config = google_api_gateway_api_config.api_cfg.id # THIS MUST BE .ID FOR WHATEVER REASON
  gateway_id = "public"
}

resource "google_api_gateway_api_config_iam_member" "member" {
  project    = var.project_id
  provider   = hashicorp-google-beta
  api        = google_api_gateway_api_config.api_cfg.api
  api_config = google_api_gateway_api_config.api_cfg.id
  role       = "roles/cloudfunction.invoker"
  member     = "user:cloud-storage-owner@programiv.iam.gserviceaccount.com"
}

output "project" {
  value = var.project_id
}
output "api" {
  value = google_api_gateway_api_config.api_cfg.api
}

output "api_config" {
  value = google_api_gateway_api_config.api_cfg.id
}

output "api_config_other" {
  value = google_api_gateway_api_config.api_cfg.api_config_id
}
