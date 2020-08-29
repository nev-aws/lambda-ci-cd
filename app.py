import json

# import requests


def lambda_handler(event, context):
 
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world -I made a change, again and again. ..again :(",
            # "location": ip.text.replace("\n", "")
        }),
    }
