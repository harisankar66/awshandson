# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 00:18:30 2020

@author: haris

#scan dynamodb

"""

import boto3
import json
import time
from boto3.dynamodb.conditions import Key

def print_time():
    current_time= datetime.now()
    print(current_time)

dynamodb = boto3.resource('dynamodb','us-east-1')

table=dynamodb.Table('schoolDb')

fe=Key("standard").eq('7')
pe="rollno,fullname"

start_time = time.time()

response= table.scan(
        FilterExpression=fe,
        ProjectionExpression=pe)

print("--- %s seconds ---" % (time.time() - start_time))

#for i in response['Items']:
#    print(json.dumps(i))

