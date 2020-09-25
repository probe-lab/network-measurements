# p2p-observatory

## Motivation & Vision
Public, user-run, permissionless networks’ dynamics are rather unpredictable due to the multiple types of applications and services that leverage them. Because they are not owned by a single user, analysing their behavior needs to be done through (non-invasive) proxies and probes, rather than through (invasive) controls (analogous to how one measures and observes patterns in a brain). Because of this hard challenge, most P2P networks put observability as a secondary goal.

In order to promote a healthy ecosystem of protocol developers where hypotheses are tested and verified through real world measurements, we envisioned the P2P Networks Observatory,  a project focused on measuring all kinds of Public P2P Networks. We believe that having the ability to get information from the real-time performance of the network can help tremendously in both real-time decision-making (e.g., request routing and forwarding) and in long-term protocol design (e.g., best ways to populate routing tables).

[HERE](RFMs.md) list of measurements that will be implemented as part of the P2P observatory.

## Deployment instructions

### Manifest file

To deploy a measurement plan you first need to create a `.toml` manifest file that defines the plan deployment parameters. 
The manifest file should include the following sections and fields

- `[plan]`: section that defines the parameters of the measurement plan
  - `builder`: the two options are `go` or `python3`
  - `name`: the name of the measurement plan
  - `version`: the version of the measurement plan
  - `app_directory`: the path to the root directory of the measurement plan files
  - `output_directory`: the path to the directory where the results of the measurement (metrics) are stored
  - `command`: the commmand that executes the measurement
- `[aws]`: section that defines the parameters of the AWS environment
  - `access_key`: The AWS access key of the account where the measurement will be deployed
  - `secret_key`: The AWS secret key of the account where the measurement will be deployed
  - `metrics_s3_bucket`: The S3 bucket where the metrics of the measurement will be stored
  - `[aws.servers]`: subsection that defines the parameters related to the deployment of the measurement servers
    - `regions`: array that lists the desired region names for the servers to be deployed
    - `availability_zones`: number of availability zones per region
    - `az_servers`: number of servers per availability zone
    - `instance_type`: the instance type name of the measurement servers
- `[elasticsearch]`: section that defines the parameters of the ElasticSearch cluster
  - `username`: The name of the master user
  - `password`: The password of the master user
  - `domain`: The domain of the elasticsearch cluster


### Step 0: Test Docker container locally

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
docker run \
--env AWS_ACCESS_KEY_ID=<my_key> \
--env AWS_SECRET_ACCESS_KEY=<my_secret> \
--env bucketname=ipfs-crawls \
--env ES_USER=vgiotsas \
--env ES_PW=<my_password> \
--env ES_URL="https://search-observatory-bn4ftthzrkyzsbnkye5tnoqsbm.eu-west-1.es.amazonaws.com/observatory/_doc" \
--name test-crawler-image ipfs-crawler
```

3. Check that the crawler runs and that the output is uploaded in your S3 bucket


### Step 1: Provision the EC2 instances

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

5. After you apply the changes and the requested resources are created, run the `./create_ansible_hosts` script

This should populate the `ansible/host` file inside the `tf` folder with the IPs and credentials of the created instances. 
The contents of the file should be similar to the following:

```
[probe]
<instance_ip> ansible_user=ubuntu ansible_ssh_private_key_file=<path_to_private_ssh_key>
```

For example:

```
[probe]
34.245.136.224 ansible_user=ubuntu ansible_ssh_private_key_file=/home/ubuntu/.ssh/terraform
```

6. Run the ansible playbook as follows:

```
ansible-playbook -i hosts ipfs-crawler.yml
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
- Compile ipfs-crawler in Dockerfile
- Get all variables from a config file instead of environment variables
