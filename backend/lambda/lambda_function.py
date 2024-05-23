# lambda_function.py
import json

def lambda_handler(event, context):
    # Example processing
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
