# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:10:43 2020

@author: haris

DynamoDB Create Table
"""
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


table = dynamodb.create_table(
    TableName='schoolDb',
    KeySchema=[
        {
            'AttributeName': 'rollno',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'fullname',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'rollno',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'fullname',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Table status:", table.table_status)


