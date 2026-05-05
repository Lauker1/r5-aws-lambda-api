import json

def lambda_handler(event, context):
    query = event.get("queryStringParameters", {}) or {}
    dataset = query.get("dataset", "test.csv")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "status": "OK",
            "message": "Inferencia simulada correcta",
            "dataset": dataset,
            "prediction": "class_A"
        })
    }