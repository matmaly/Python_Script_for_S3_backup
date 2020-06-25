#!/usr/bin/env python3

import boto3

session = boto3.Session(profile_name="python_s3_backup")

s3_backup = session.client("s3")

s3_backup.create_bucket(Bucket="testbucket.1235346347323ls")