import streamlit as st
import boto3
import time
import json
from PIL import Image
import io

# AWS configuration
bucket_name = "skin-cancer-demo-bucket"
upload_prefix = "uploads/"
prediction_prefix = "predictions/"
lambda_function_name = "skin-cancer-predictor-fn"

# AWS clients
s3 = boto3.client('s3')
lambda_client = boto3.client('lambda')

st.title("Skin Cancer Predictor")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    if st.button("Predict"):
        with st.spinner("Uploading and predicting..."):
            # Upload to S3
            image_name = uploaded_file.name
            s3_key = f"{upload_prefix}{image_name}"
            s3.upload_fileobj(uploaded_file, bucket_name, s3_key)

            # Trigger Lambda
            event_payload = {
                "Records": [
                    {
                        "s3": {
                            "bucket": {"name": bucket_name},
                            "object": {"key": s3_key}
                        }
                    }
                ]
            }

            lambda_response = lambda_client.invoke(
                FunctionName=lambda_function_name,
                InvocationType='RequestResponse',
                Payload=json.dumps(event_payload)
            )

            response_payload = json.load(lambda_response['Payload'])
            st.success("Prediction Completed")

            try:
                # Construct prediction file key
                prediction_key = f"{prediction_prefix}{image_name}.json"

                # Give S3 a short moment to reflect the new file
                time.sleep(2)

                # Download and parse the prediction result
                prediction_obj = s3.get_object(Bucket=bucket_name, Key=prediction_key)
                prediction_result = prediction_obj['Body'].read().decode('utf-8')
                prediction_data = json.loads(prediction_result)

                # Validate and show top prediction
                if isinstance(prediction_data, list) and isinstance(prediction_data[0], dict):
                    top = max(prediction_data, key=lambda x: x['score'])
                    st.success(f"Top Prediction: {top['label']} with score {top['score']:.2f}")
                    st.subheader("Full Prediction Output:")
                    st.json(prediction_data)
                else:
                    st.error("Prediction format is unexpected.")
                    st.json(prediction_data)

            except Exception as e:
                st.error(f"Error parsing prediction: {e}")
