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
| `lambdafunctioncode/`            | Lambda function code for image preprocessing and inference call |
| `sagemakernotebookwithcode/`     | Notebook for training and deploying the ViT model               |
| `streamlit app code/`            | Frontend UI to upload and display predictions                  |
| `screenshots/`                   | Architecture diagrams, output samples, and UI screenshots       |
| `requirements.txt`               | Python package dependencies                                     |
| `README.md`                      | This documentation                                              |
| `LICENSE`                        | MIT License                                                     |

---

## 🧪 How It Works

1. **User uploads an image** via the Streamlit app
2. Image is saved to **S3 (`uploads/`)**
3. **S3 event triggers** the Lambda function
4. Lambda:
   - Converts image to RGB
   - Resizes to 224×224
   - Sends image to SageMaker
5. **SageMaker ViT model** classifies the image into 7 skin condition categories
6. Prediction (JSON) is saved in S3 (`predictions/`) and shown in the UI

---

## 🖼️ Screenshot Highlights

- ✅ AWS Architecture Diagram
- ✅ Lambda setup and logs
- ✅ SageMaker Notebook and Endpoint
- ✅ S3 bucket structure
- ✅ Real Streamlit UI showing top prediction with confidence

Check the [`screenshots/`](./screenshots/) folder for visuals.

---

## 🧠 Model Details

- **Base**: Vision Transformer (ViT) pretrained on ImageNet-21k
- **Fine-tuned on**: [HAM10000-based dataset](https://huggingface.co/datasets/marmal88/skin_cancer)
- **Target Classes**:
  - Actinic keratoses
  - Basal cell carcinoma
  - Benign keratosis-like lesions
  - Dermatofibroma
  - Melanoma
  - Melanocytic nevi
  - Vascular lesions
- **Validation Accuracy**: ~96.95%
- **Training**: 5 epochs, Adam optimizer, learning rate 1e-4, batch size 32

---

## ⚙️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/StevenMascarenhas/Cloud-Based-Skin-Cancer-Detection-Using-Deep-Learning-and-AWS.git
cd Cloud-Based-Skin-Cancer-Detection-Using-Deep-Learning-and-AWS

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app (if running locally)
streamlit run "streamlit app code/app.py"
