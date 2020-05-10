# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:17:15 2020

@author: haris
"""

#AWS List Buckets
import boto3
# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')