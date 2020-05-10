# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:32:04 2020

@author: haris
"""

import boto3
from cryptography.fernet import Fernet


kms_client=boto3.client('kms','us-east-1')

text="My secret 56"
encoded=text.encode()

response=kms_client.generate_data_key(
        KeyId='alias/myKey1',
        NumberOfBytes=32)

plain_key=response['Plaintext']
print(plain_key)
enc_key=response['CiphertextBlob']

file=open('enckey.key',"wb")
file.write(enc_key)
file.close

f = Fernet(plain_key)
encrypted=f.encrypt(encoded)
print(encrypted)

file=open('safe_date.txt',"wb")
file.write(encrypted)
file.close()
