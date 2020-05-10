# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:50:00 2020

@author: haris
"""

#Write in Bucket

import boto3
import logging
from botocore.exceptions import ClientError

def upload_file(file_name,bucket,object_name=None):
    if object_name is None:
        object_name=file_name
    s3_client=boto3.client('s3')
    try:
        response=s3_client.upload_file(file_name,bucket,object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
if __name__ == '__main__':
    file_name = "S3Test.txt"
    status=upload_file(file_name,'testbkt4hari')
    print(status)