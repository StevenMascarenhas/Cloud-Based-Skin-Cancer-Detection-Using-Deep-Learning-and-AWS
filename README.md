# Cloud-Based Skin Cancer Detection Using Deep Learning and AWS

A cloud-native AI pipeline for detecting skin cancer from dermatoscopic images using a fine-tuned Vision Transformer (ViT) model. This project integrates AWS Lambda, SageMaker, S3, and Streamlit to provide real-time predictions via a lightweight, scalable architecture.

---

## 🧠 Overview

Skin cancer is one of the most common cancers globally, and early detection is crucial. This project automates the diagnosis process using a pretrained ViT model deployed on AWS. Users interact via a Streamlit frontend and receive predictions in real time.

---

## 🚀 Technologies Used

- **Model**: Vision Transformer (HuggingFace)
- **Frontend**: Streamlit
- **Cloud Services**: 
  - Amazon S3 (image & result storage)
  - AWS Lambda (image preprocessing, inference trigger)
  - Amazon SageMaker (model hosting)
  - AWS CloudWatch (monitoring/logging)

---

## 📁 Project Structure

| Folder                          | Description                                                                |
|----------------------------------|----------------------------------------------------------------------------|
| `lambdafunctioncode/`            | AWS Lambda function to preprocess images and call SageMaker endpoint       |
| `sagemakernotebookwithcode/`     | Jupyter notebook for training & deploying the ViT model on SageMaker       |
| `streamlit app code/`            | Streamlit frontend for user uploads and displaying predictions             |
| `screenshots/`                   | AWS architecture diagrams and sample outputs                               |
| `requirements.txt`               | Required Python packages                                                   |
| `README.md`                      | Project overview and documentation                                         |
| `LICENSE`                        | MIT License for open-source use                                            |
| `.gitignore`                     | Files and folders excluded from version control                            |

---

## 🧪 How It Works

1. User uploads an image via Streamlit
2. Image is saved to S3 (`uploads/` folder)
3. S3 event triggers the Lambda function:
   - Converts image to RGB
   - Resizes to 224x224
   - Sends payload to SageMaker endpoint
4. ViT model returns prediction as JSON
5. Output is saved to `predictions/` in S3 and shown in the app

---

## 🧰 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/StevenMascarenhas/Cloud-Based-Skin-Cancer-Detection-Using-Deep-Learning-and-AWS.git
cd Cloud-Based-Skin-Cancer-Detection-Using-Deep-Learning-and-AWS

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app locally (if available)
streamlit run "streamlit app code/app.py"
