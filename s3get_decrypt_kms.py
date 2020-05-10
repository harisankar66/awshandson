# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:45:51 2020

@author: haris
"""

#Read buket and decrpty using kms key
import boto3
import base64

msg='This is confidential'


s3 = boto3.resource('s3')
s3.meta.client.download_file('testbkt4hari', 'upload1.txt', 'upload2.txt')

f=open('upload1.txt','rb')
safer_msg=f.read()
f.close()

print(safer_msg)

kms_client=boto3.client('kms','us-east-1')
response=kms_client.decrypt(
        CiphertextBlob=safer_msg,
        KeyId='alias/myKey1')

msgr_b24=response['Plaintext']

print(msgr_b24)
msgr_bytes=base64.b64decode(msgr_b24)
msgr=msgr_bytes.decode('ascii')

print(msgr)

print(msgr==msg)