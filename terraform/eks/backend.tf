terraform {
    backend "s3" {
    bucket = "terraform-tf-state"
    key = "us-east-1/s3/terraform.tfstate"
    region = "us-east-1"
    dynamodb_table = "terraform-state-locking"
    }
}

resource "aws_s3_bucket" "terraform_state"{
    bucket = "terraform-state"
    lifecycle {
        prevent_destroy = true
    }
    versioning {
        enabled = true
    }
    server_side_encryption_configuration {
        rule{
            apply_server_side_encryption_by_default {
                sse_algorithm = "AES256"
            }
        }
    }

}

resource "aws_dynamodb_table" "terraform_locks"{
    name = "terraform-state-locking"
    billing_mode = "PAY_PER_REQUEST"
    hash_key = "LockID"
    attribute {
        name = "LockID"
        type = "S"
    }
}
