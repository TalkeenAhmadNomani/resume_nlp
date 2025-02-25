# NLP project
# 📄 Resume Category Prediction

## 📌 Overview
The **Resume Category Prediction** app is a machine learning-based **Streamlit** application that predicts the job category of a given resume. It allows users to upload resumes in **PDF, DOCX, or TXT** formats, extracts the text, processes it, and classifies it using a **pre-trained Support Vector Classifier (SVC) model**.

## 🚀 Features
- 📂 **Resume Upload** – Supports PDF, DOCX, and TXT file formats.
- 🔍 **Text Extraction** – Extracts text from resumes while handling errors.
- 📝 **Text Cleaning** – Cleans resume text by removing unnecessary symbols, links, and special characters.
- 🤖 **Category Prediction** – Uses a trained ML model to classify resumes into relevant job categories.
- 🎨 **Interactive UI** – Built using Streamlit for an easy-to-use experience.

## 🛠️ Tech Stack
- **Python** 🐍
- **Streamlit** – For UI
- **Scikit-learn** – For Machine Learning
- **TF-IDF Vectorizer** – For text feature extraction
- **Support Vector Classifier (SVC)** – For classification
- **Pickle** – For model storage
- **PyPDF2 & python-docx** – For text extraction from resume.

## ⚡ Setup & Installation
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/resume-category-prediction.git
   cd resume-category-prediction

python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows

pip install -r requirements.txt

streamlit run app.py

## Usage
Upload a resume (PDF, DOCX, or TXT).
Extract text from the uploaded file.
View the cleaned resume text (optional).
Predict the job category using the trained ML model.
Optimize your resume based on the predicted category.
🤖 Future Enhancements
✅ Support for more file formats (e.g., DOC).
✅ Integration with real-time job market insights.
✅ Improved resume analysis with AI-powered suggestions.
## Contributing
Contributions are welcome! Feel free to fork this repo and submit a pull request.

## License
This project is licensed under the MIT License.
