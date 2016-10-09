from __future__ import print_function
import logging,time
import boto3
import botocore
import json
import decimal
import sys
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Test2')

def insert_data():
    actors={"A","B","C"}

    response = table.update_item(
	    Key={
	         "name":"SOME_RANDOM_KEY"
	    },
	    UpdateExpression="set partners = :v",
	    ExpressionAttributeValues={
	        ':v': actors
	    },
	    ReturnValues="UPDATED_NEW"
    )

    print ("Insert successful!",response)

def modify_data():
    response = table.update_item(
        Key={
             "name":"SOME_RANDOM_KEY"
        },
        UpdateExpression="ADD partners :v",  
        ExpressionAttributeValues={
            ':v': {"99"}
        },
        ReturnValues="UPDATED_NEW"
    )
    print ("Update successful!",response)
    
def remove_data():
    response = table.update_item(
    		Key={
    		     "name":"SOME_RANDOM_KEY"
    		},
    		UpdateExpression="DELETE partners  :v ",  
    		ExpressionAttributeValues={
    		    ':v': {"A"}    
    		} ,
    		ReturnValues="UPDATED_NEW"
	)
    print ("Del successful!",response)
    
def lambda_handler(event, context):
    # TODO implement
    modify_data()
    return 'Hello from Lambda'