import boto3
from boto3 import Session
from collections import defaultdict
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """
    success = False
    try:
        dev = boto3.session.Session(profile_name='vng')
        if region is None:
            s3_client = dev.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = dev.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
            success = True
    except ClientError as e:
        logging.error()
    return success


def get_credentials():
    """
    Retrieves the AWS credentials
    
    :return: the access and secret key    
    """
    session = Session()
    credentials = session.get_credentials()
    current_credentials = credentials.get_frozen_credentials()
    return current_credentials


def get_regions():
    """
    Retrieves the available AWS regions

    :return: a set with the names of the available regions
    :rtype: set
    """
    ec2 = boto3.client('ec2')
    try:
        response = ec2.describe_regions()
        available_regions = set()
        if 'Regions' in response:
            for region in response['Regions']:
                if 'RegionName' in region:
                    available_regions.add(region['RegionName'])
    except ClientError as e:
        logging.error(e)
    return available_regions


def get_azones(available_regions):
    """
    Retrieves the available Availability Zones (AZs) per region

    :param available_regions: the set of available regions
    :type available_regions: set
    :return: the mapping between regions and AZ names
    :rtype: defaultdict
    """
    availability_zones = defaultdict(set)
    try:
        for region in available_regions:
            ec2 = boto3.client('ec2', region_name=region)
            response = ec2.describe_availability_zones()
            if 'AvailabilityZones' in response:
                for az in response['AvailabilityZones']:
                    availability_zones[region].add(az['ZoneName'])
    except ClientError as e:
        logging.error(e)
    return availability_zones