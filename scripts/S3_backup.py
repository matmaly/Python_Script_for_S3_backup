#!/usr/bin/env python3

import boto3
import argparse

'''
Create a bucket in S3 with a specified name in a specified region or default one.
Argparser used to gather required input for bucket name and region
'''

parser = argparse.ArgumentParser(description="Process S3 requests through command line")
parser.add_argument("--region", "-r", help="Provide the region for the bucket")
parser.add_argument("--name", "-n", required=True, help="Provide the name for the bucket")

args = parser.parse_args()

def create_bucket():
    session = boto3.Session(profile_name="python_s3_backup")
    if args.region is None:
        s3_client = session.client("s3")
        s3_client.create_bucket(Bucket=args.name)
    else:
        s3_client = session.client("s3", region_name=args.region)
        location = {"LocationConstraint": args.region}
        s3_client.create_bucket(Bucket=args.name, CreateBucketConfiguration=location)
    
create_bucket()
