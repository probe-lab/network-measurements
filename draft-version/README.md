# P2P Observatory 

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
  - `metrics_s3_bucket`: The S3 bucket where the metrics of the measurement will be stored
  - `[aws.servers]`: subsection that defines the parameters related to the deployment of the measurement servers
    - `regions`: array that lists the desired region names for the servers to be deployed
    - `availability_zones`: number of availability zones per region
    - `az_servers`: number of servers per availability zone
    - `instance_type`: the instance type name of the measurement servers
- `[docker]`
  - `hub_username`: the username for the docker hub
  - `hub_password`: [OPTIONAL] API Token or password for the docker hub
  - `dockercfg_path`: [OPTIONAL] The path to the docker configuration file (if different from the default)  
  Either the `hub_password` or the `dockercfg_path` attributes should be provided.
- `[elasticsearch]`: section that defines the parameters of the ElasticSearch cluster
  - `username`: The name of the master user
  - `password`: The password of the master user
  - `domain`: The domain of the elasticsearch cluster


### How to run

1. Install the following prerequisites:
  * Terraform: https://learn.hashicorp.com/tutorials/terraform/install-cli
  * Ansible: https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
  * Docker: https://docs.docker.com/get-docker/

2. Populate the `toml` minefst file.

3. The experiments are deployed and destroyed using the `p2po` binary, using the following syntax:

```
usage: p2po [-h] [-m MANIFEST] (--deploy | --destroy)

Deploy a measurement to the P2P observatory

optional arguments:
  -h, --help            show this help message and exit
  -m MANIFEST, --manifest MANIFEST
                        Path to manifest file
  --deploy              Deploy a new experiment
  --destroy             Destroy the resources of a deployed experiment
```

If the `--manifest` parameter is not provided, the `p2po` binary will use `config.toml` as the default location.

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
