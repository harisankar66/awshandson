# -*- coding: utf-8 -*-
"""
Created on Sat May  2 07:53:03 2020

@author: haris
"""

#generate KMS data key
import boto3
import base64
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

msg='This is confidential'
message_bytes = msg.encode('ascii')
msg_b24_bytes= base64.b64encode(message_bytes)
msg_b24 = msg_b24_bytes.decode('ascii')

kms_client=boto3.client('kms','us-east-1')

"""
response=kms_client.generate_data_key(
        KeyId='alias/myKey1',
        KeySpec='AES_256')

print(response['Plaintext'])

plain_key=response['Plaintext']
safe_key=response['CiphertextBlob']
"""
response=kms_client.encrypt(
        Plaintext=msg_b24,
        KeyId='alias/myKey1')

safe_msg=response['CiphertextBlob']
print(safe_msg)

file_name="upload1.txt"
f= open(file_name,"wb")
f.write(safe_msg)
f.close()

status=upload_file(file_name,'testbkt4hari')
print(status)
