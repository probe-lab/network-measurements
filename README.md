# p2p-observatory

## Step 0: Test Docker container locally

### Prerequisites

You need an AWS account with access rights to S3 and access to an Elastic Search cluster for which you have the login credentials of the master user.

1. Pull the Docker Image `vgiotsas/ipfs-crawler`

```
docker pull vgiotsas/ipfs-crawler
```

2. Run the `vgiotsas/ipfs-crawler` image providing the following environment variables:

|  Variable Name | Value   |
|---|---|
| AWS_ACCESS_KEY_ID  | The AWS access key   |
| AWS_SECRET_ACCESS_KEY  | The AWS secret key   |
| bucketname  |  The name of the bucket were the crawler's output will be uploaded  |
| ES_USER | The username for accessing the Elastic Search cluster |
| ES_PW   | The password for accessing the Elastic Search cluster |
| ES_URL   | The URL of the Elastic Search cluster |

For example:

```
docker run --env AWS_ACCESS_KEY_ID=<my_key> --env AWS_SECRET_ACCESS_KEY=<my_secret> --env bucketname=ipfs-crawls --env ES_USER=vgiotsas --env=ES_PW=<my_password> ES_URL="https://search-observatory-bn4ftthzrkyzsbnkye5tnoqsbm.eu-west-1.es.amazonaws.com/observatory/_doc"  --name test-crawler-image ipfs-crawler
```

3. Check that the crawler runs and that the output is uploaded in your S3 bucket


## Step 1: Provision the EC2 instances

1. Install Terraform following the instructions below:

https://learn.hashicorp.com/tutorials/terraform/install-cli

2. Set the following two environment variables for the Access Key and the Secret Key of your AWS account:

```
TF_VAR_accessKey=AKIAC7WDA7Z3KM4RA
TF_VAR_secretKey=XgRIh3EqkWQHR7HXV6nbHsiBl0xVwlQu
```

3. Set the SSH key of the new instances in the `tf/variables.tf` file.

4. In the `tf/` directory run:

```
terraform init
terraform apply
```

After you apply the changes and the requested resources are created, you should have an `ansible/host` folder inside the `tf` folder. The contents of the file should be similar to the following:

```
[probe]
<instance_ip> ansible_user=ubuntu ansible_ssh_private_key_file=<path_to_private_ssh_key>
```

For example:

```
[probe]
34.245.136.224 ansible_user=ubuntu ansible_ssh_private_key_file=/home/ubuntu/.ssh/terraform
```

### Troubleshooting:

If you get the error:
> sudo: add-apt-repository: command not found

you need to install the the `software-properties-common` package:

`sudo apt install software-properties-common`

### TODO

- Improve Elastic Search authentication
- Provision Elastic Search cluster through Terraform
- Create Docker image for steps 1 and 2
