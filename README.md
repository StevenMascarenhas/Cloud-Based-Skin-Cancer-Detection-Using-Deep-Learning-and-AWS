# Cloud-Based Skin Cancer Detection Using Deep Learning and Scalable AWS Infrastructure

A scalable, cloud-native AI system that detects skin cancer from dermatoscopic images using a fine-tuned Vision Transformer (ViT) model deployed on AWS. The project combines deep learning with Amazon S3, AWS Lambda, SageMaker, and Streamlit for a cost-effective and real-time diagnostic pipeline.

## 📁 Project Structure

- `lambdafunctioncode/`  
  Contains the AWS Lambda function that preprocesses uploaded images and invokes the SageMaker model.

- `sagemakernotebookwithcode/`  
  Jupyter notebook for fine-tuning and deploying the Vision Transformer (ViT) model on SageMaker.

- `streamlit app code/`  
  Streamlit web app where users can upload images and see real-time classification results.

- `screenshots/`  
  Visual references of architecture, cloud configurations, and output predictions.

- `requirements.txt`  
  Required Python packages for running the project locally or in cloud environments.

- `README.md`  
  Documentation explaining the project, architecture, and usage instructions.

- `LICENSE`  
  MIT license for open-source usage.



## 📌 Project Overview
Skin cancer affects millions worldwide, and early detection is crucial. This solution enables users to upload images of skin lesions and receive classification results in real time through a user-friendly web interface. The project aligns with the AWS Well-Architected Framework to ensure operational excellence and scalability.

## ⚙️ Architecture
- **Frontend:** Streamlit web app for user interaction
- **Storage:** Amazon S3 for image and result storage
- **Processing:** AWS Lambda for image preprocessing and inference orchestration
- **Inference:** Amazon SageMaker hosting a Hugging Face ViT model
- **Monitoring:** AWS CloudWatch for logging and billing alerts

## 🧠 Model
- **Model Type:** Vision Transformer (ViT)
- **Source:** Fine-tuned on HAM10000 dataset via Hugging Face (`Anwarkh1/Skin_Cancer-Image_Classification`)
- **Classes:** 
  - Actinic Keratoses
  - Basal Cell Carcinoma
  - Benign Keratosis-like Lesions
  - Dermatofibroma
  - Melanoma
  - Melanocytic Nevi
  - Vascular Lesions

## 🚀 How It Works
1. User uploads a skin lesion image via Streamlit.
2. Image is saved in the `uploads/` folder of an S3 bucket.
3. Upload event triggers a Lambda function:
   - Converts to RGB
   - Resizes to 224×224
   - Sends to SageMaker endpoint
4. SageMaker returns classification as JSON with confidence scores.
5. Output saved to `predictions/` folder and displayed in UI.

## 🧪 Installation & Deployment

```bash
git clone https://github.com/yourusername/skin-cancer-detector.git
cd skin-cancer-detector
pip install -r requirements.txt
streamlit run app.py
```

## 🔐 Security
IAM roles follow the principle of least privilege. CloudWatch monitors usage and billing alarms ensure resource control within free-tier limits.

## 📈 Scalability
- Serverless Lambda allows parallel processing.
- S3 provides high throughput for millions of objects.
- Future-ready for integration with DynamoDB and Amazon Athena for analytics.

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👤 Author
**Steven Gerard Mascarenhas**  
Student ID: 24044407  
Module: CS5024 - Theory and Practice of Advanced AI Ecosystems
