# Cloud-Based Skin Cancer Detection Using Deep Learning and Scalable AWS Infrastructure

A real-time, cloud-native skin cancer detection system using a fine-tuned Vision Transformer (ViT), built on the AWS AI ecosystem and accessible via a Streamlit interface. This end-to-end solution demonstrates how deep learning and serverless infrastructure can be combined to deliver scalable, low-latency, and cost-effective healthcare tools.

---

## 🧠 Project Overview

Skin cancer is one of the most prevalent forms of cancer, with over 1.5 million cases reported annually. This project addresses the need for accessible early diagnosis using:

- A **Vision Transformer (ViT)** model from Hugging Face
- Deployed on **Amazon SageMaker**
- Triggered by **AWS Lambda**
- Served via **Streamlit**
- Integrated with **Amazon S3** and **CloudWatch**

This architecture aligns with the AWS Well-Architected Framework and uses scalable, serverless design principles.

---

## 🚀 Technologies Used

| Component     | Tool / Service         |
|---------------|------------------------|
| Model         | ViT (Hugging Face, fine-tuned) |
| Deployment    | Amazon SageMaker SDK   |
| Event Logic   | AWS Lambda + Pillow Layer |
| Storage       | Amazon S3              |
| Monitoring    | AWS CloudWatch         |
| Frontend      | Streamlit              |
| Roles/Security| AWS IAM                |

---

## 📁 Project Structure

| Folder                          | Description                                                      |
|----------------------------------|------------------------------------------------------------------|
| `lambdafunctioncode/`            | AWS Lambda function to preprocess images and call SageMaker     |
| `sagemakernotebookwithcode/`     | Jupyter notebook to train and deploy ViT model                  |
| `streamlit app code/`            | Frontend UI built with Streamlit                               |
| `screenshots/`                   | AWS setup screenshots and system output                        |
| `requirements.txt`               | Python dependencies for local/Streamlit deployment              |
| `CS5024_Project_Report_Steven_Mascarenhas.pdf` | Full academic report documenting the project                |
| `README.md`                      | This documentation                                               |
| `LICENSE`                        | MIT License                                                      |

---

## 🧪 How It Works

1. User uploads a dermatoscopic image via the Streamlit app
2. Image is stored in S3 under `uploads/`
3. AWS Lambda is triggered:
   - Image is resized, formatted (RGB, 224×224)
   - Forwarded to SageMaker endpoint
4. SageMaker ViT model returns the prediction
5. Result is saved to `predictions/` in S3 and displayed to the user

---

## 🖼️ Screenshot Highlights

Located in the `screenshots/` folder:
- AWS Lambda function
- SageMaker deployment and notebook
- Architecture diagram
- Streamlit UI and predictions

---

## 🧠 Model Summary

- **Base**: Vision Transformer (ViT) from Hugging Face
- **Fine-tuned on**: HAM10000 dataset (`marmal88/skin_cancer`)
- **Classes**:
  - Actinic keratoses
  - Basal cell carcinoma
  - Benign keratosis-like lesions
  - Dermatofibroma
  - Melanoma
  - Melanocytic nevi
  - Vascular lesions
- **Accuracy**: 96.95% (validation)
- **Training**: 5 epochs, Adam optimizer, lr=1e-4, batch size=32

---

## ⚙️ Local Setup

```bash
# Clone the repo
git clone https://github.com/StevenMascarenhas/Cloud-Based-Skin-Cancer-Detection-Using-Deep-Learning-and-AWS.git
cd Cloud-Based-Skin-Cancer-Detection-Using-Deep-Learning-and-AWS

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run "streamlit app code/app.py"
