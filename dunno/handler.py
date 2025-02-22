import json


def juas(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully! --- ??????",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def hello(event, context):
    body = {
        "message": "Hola Mundo",
        "test1": "Hello World",
        "test2": "Hello",
        "test3": "World",
        "test4":{
            "test5": "-",
            "test6": "--",
            "test7": "---",
            "test8": "----",
        }
    }
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response