def handle(event, context):
    return {
        "statusCode": 200,
        "body": {
            "name": event.query['lang']
        }
    }