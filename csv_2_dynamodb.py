# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:38:38 2020

@author: haris
"""

#csv to Dynamo db- Supports only string key attribute

import boto3
import csv

dynamodb= boto3.resource('dynamodb','us-east-1')

def read_csv(csv_file,list):
    rows = csv.DictReader(open(csv_file))
    
    for row in rows:
        list.append(row)
    print()
    
def load_table(table_name,row_list):
    table= dynamodb.Table(table_name)
    firstRec = True
    with table.batch_writer() as batch:
        for row in row_list:
            print(row)
            if(firstRec):
                firstRec=False
                continue
            batch.put_item(Item=row)
    return True         
"""
            batch.put_item(Item={
                    'id':{'N':row[0]},
                    'name':{'S':row[1]},
                    'class':{'N':row[2]},
                    'maths':{'N':row[3]},
                    'physics':{'N':row[4]},
                    'chemistry':{'N':row[5]},
                    'biology':{'N':row[6]},
                    'sports':{'N':row[7]}
                    }}
    return True 
"""

if __name__ == '__main__':
    table_name = 'schoolDb'
    file_name = 'Book1.csv'
    row_list = []
    
    read_csv(file_name,row_list)
    status= load_table(table_name,row_list)
    
    if(status):
        print('Suuccess')
    else:
        print('error')