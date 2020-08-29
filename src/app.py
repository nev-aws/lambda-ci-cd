import json

# import requests


def lambda_handler(event, context):
 
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world -I made a change, which doesn't trigger.",
            # "location": ip.text.replace("\n", "")
        }),
    }
