import boto3
import base64
import json
import os
from PIL import Image
import io

runtime = boto3.client('sagemaker-runtime')
s3 = boto3.client('s3')

# Corrected environment variable key
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']

def lambda_handler(event, context):
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        # Download the image from S3
        image_obj = s3.get_object(Bucket=bucket, Key=key)
        image_content = image_obj['Body'].read()

        # Resize the image to 224x224
        image = Image.open(io.BytesIO(image_content)).convert("RGB").resize((224, 224))
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG")
        buffer.seek(0)
        payload = buffer.read()

        # Invoke SageMaker endpoint
        response = runtime.invoke_endpoint(
            EndpointName=ENDPOINT_NAME,
            ContentType='image/jpeg',
            Body=payload
        )

        result = json.loads(response['Body'].read().decode())

        # Save prediction result to S3
        s3.put_object(
            Bucket=bucket,
            Key=key.replace("uploads/", "predictions/") + ".json",
            Body=json.dumps(result)
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Prediction completed and stored.')
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error parsing prediction: {str(e)}")
        }
