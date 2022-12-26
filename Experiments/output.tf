data "terraform_remote_state" "project" {
  backend   = "gcs"
  workspace = terraform.workspace

  config = {
    bucket = "mario-tfstate"
    prefix = "infra"
  }
}