import json
import uuid

def lambda_handler(event, context):
    reset_token = str(uuid.uuid4())
    print(reset_token)
    reset_link = f"http://testcompany/passwordreset/{reset_token}"
    response = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'reset_link': reset_link})
    }
    return response