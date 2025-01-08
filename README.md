# Multiple Disease Prediction
Welcome to the Multiple Disease Prediction project repository! This project was developed by Team Break-A-Leg for the Weal Club at PESU Hackathon Healthack. Our chosen problem statement was "Analysis, Diagnosis, and Encryption of Blood Work Using Machine Learning and Blockchain".

# Project Overview
## Motivation
With the growing trend towards home-based medical testing systems, our solution aims to streamline the diagnosis process. Typically, after receiving a medical test report, one would consult a doctor to interpret the results, often incurring consultation charges. Our solution automates this process, providing an initial diagnosis for three major diseases.

## Diseases Diagnosed
1. Diabetes
2. Heart Disease
3. Chronic Kidney Disease

# Features
1. **Optical Character Recognition (OCR):** Reads and extracts information from blood reports.
2. **Machine Learning and Deep Learning Models:** Trained models to diagnose the diseases mentioned above, achieving an overall accuracy of 92%.
3. **Blockchain for Data Security:** Utilizes Ethereum Mainnet and Polygon to encrypt and store personal information securely.

# How It Works
1. **Data Extraction:** The module reads blood report information using OCR.
2. **Disease Prediction:** The extracted data is used by trained ML and DL models to predict the likelihood of Diabetes, Heart Disease, and Chronic Kidney Disease.
3. **Data Security:** Personal information from the blood report is encrypted and stored on the Blockchain. The encryption ensures that only the patient and their family doctor have access to the data.
4. **Web Interface:** The entire process is hosted on a web application using Streamlit, providing an intuitive and user-friendly interface.

# Usage
## Web Application
Our web application is deployed and accessible via the following link: https://shreyaskatti-analysis-diagnosis-and-encryption-of-blood-work.streamlit.app/

## Testing
To test the product:
1. Download all datasets from this repository.
2. Use the "Blood_report.pdf" file provided.

## Technical Details
### Machine Learning Models
1. The models are designed to use specific values required for predicting each disease.
2. Continuous learning from user data to improve accuracy.

### Blockchain Implementation
1. Built on Ethereum Mainnet and deployed on Polygon.
2. Ensures high-level encryption and security of personal data.
3. Unique key generation for each blood report, accessible only by the patient and their family doctor.

# Achievements
This project was recognized as an award-winning project due to its innovative approach and unique features.

#
Thank you for exploring our project! We hope you find it useful and innovative.

Happy Diagnosing!
