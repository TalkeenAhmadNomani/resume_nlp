import streamlit as st
import pickle
import docx  # Extract text from Word file
import PyPDF2  # Extract text from PDF
import re

# Load pre-trained model and TF-IDF vectorizer (ensure these exist)
try:
    svc_model = pickle.load(open('clf.pkl', 'rb'))  
    tfidf = pickle.load(open('tfidf.pkl', 'rb'))  
    le = pickle.load(open('encoder.pkl', 'rb'))  
except FileNotFoundError as e:
    st.error(f"Error: {e}. Ensure the model files exist in the same directory.")
    st.stop()  # Stop execution if models are missing

# Function to clean resume text
def cleanResume(txt):
    cleanText = re.sub('http\S+\s', ' ', txt)
    cleanText = re.sub('RT|cc', ' ', cleanText)
    cleanText = re.sub('#\S+\s', ' ', cleanText)
    cleanText = re.sub('@\S+', '  ', cleanText)
    cleanText = re.sub(r'[^\w\s]', ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub('\s+', ' ', cleanText)
    return cleanText.strip()

# Function to extract text from PDF
def extract_text_from_pdf(file):
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            extracted_text = page.extract_text()
            text += extracted_text if extracted_text else ''
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {e}")
        return None

# Function to extract text from DOCX
def extract_text_from_docx(file):
    try:
        doc = docx.Document(file)
        text = '\n'.join([p.text for p in doc.paragraphs])
        return text
    except Exception as e:
        st.error(f"Error extracting text from DOCX: {e}")
        return None

# Function to extract text from TXT
def extract_text_from_txt(file):
    try:
        text = file.read().decode('utf-8', errors='ignore')
        return text
    except Exception as e:
        st.error(f"Error extracting text from TXT: {e}")
        return None

# Function to handle file upload and extraction
def handle_file_upload(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension == 'pdf':
        return extract_text_from_pdf(uploaded_file)
    elif file_extension == 'docx':
        return extract_text_from_docx(uploaded_file)
    elif file_extension == 'txt':
        return extract_text_from_txt(uploaded_file)
    else:
        st.error("Unsupported file type. Please upload a PDF, DOCX, or TXT file.")
        return None

# Function to predict the category of a resume
def pred(input_resume):
    cleaned_text = cleanResume(input_resume)
    vectorized_text = tfidf.transform([cleaned_text]).toarray()
    predicted_category = svc_model.predict(vectorized_text)
    return le.inverse_transform(predicted_category)[0]  # Return the category name

# Streamlit app layout
def main():
    st.set_page_config(page_title="Resume Category Prediction", page_icon="📄", layout="wide")
    st.title("Resume Category Prediction App")
    st.markdown("Upload a resume in PDF, TXT, or DOCX format and get the predicted job category.")

    uploaded_file = st.file_uploader("Upload a Resume", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        resume_text = handle_file_upload(uploaded_file)
        if not resume_text or not resume_text.strip():
            st.error("The uploaded resume is empty or unreadable. Please try another file.")
            return

        st.success("Successfully extracted the text from the uploaded resume.")

        if st.checkbox("Show extracted text", False):
            st.text_area("Extracted Resume Text", resume_text, height=300)

        st.subheader("Predicted Category")
        category = pred(resume_text)
        st.write(f"The predicted category of the uploaded resume is: **{category}**")

if __name__ == "__main__":
    main()
