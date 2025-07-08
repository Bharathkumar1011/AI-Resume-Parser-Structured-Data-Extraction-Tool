import streamlit as st
import json
from groq import Groq
from langchain_community.document_loaders import PDFPlumberLoader
from dotenv import load_dotenv
import os
import tempfile
import base64
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize Groq client
groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key) if groq_api_key else None

# System and human prompts
system_prompt = """You are an AI assistant designed to extract structured resume data.
                   Always respond with a strictly valid JSON object. Use `null` for missing values,
                   ensuring compliance with JSON standards. Do not include explanations,
                   comments, or any additional text outside the JSON structure.
                """

human_prompt = """
             **Task:** Extract key information from the following resume text.

            **Resume Text:**
            {context}

            **Instructions:**
            Please extract the following information and format it in a clear structure:

            1. **Contact Information:**
            - Name:
            - Email:
            - Phone Number:
            - Website/Portfolio/LinkedIn:
            - Github Profile:

            2. **Education:**
            - Institution Name:
            - Degree:
            - Graduation Date:

            3. **Experience:**
            - Job Title:
            - Company Name:
            - Location:
            - Dates of Employment:
            - Description:

            5. **Skills:**
            - Skills:

            **Question:**
            Extract this information as a structured and valid JSON object. Use `null` for missing or unavailable valuesDo not include explanations,
                   comments, or any additional text outside the JSON structure.
        """

def clean_resume_data(json_data):
    """Clean and standardize the resume JSON data"""
    # 1. Remove duplicate skills (case insensitive)
    if 'skills' in json_data and isinstance(json_data['skills'], list):
        seen_skills = set()
        unique_skills = []
        for skill in json_data['skills']:
            if skill and isinstance(skill, str):
                lower_skill = skill.strip().lower()
                if lower_skill not in seen_skills:
                    seen_skills.add(lower_skill)
                    unique_skills.append(skill.strip())
        json_data['skills'] = unique_skills
    
    # 2. Standardize website/portfolio fields
    website_aliases = [
        'website', 'portfolio', 'linkedin', 
        'Website', 'Portfolio', 'LinkedIn',
        'personal_website', 'webpage'
    ]
    
    # Find the first existing website-related field
    website_field = None
    website_value = None
    for field in website_aliases:
        if field in json_data:
            website_field = field
            website_value = json_data[field]
            break
    
    # Standardize to 'website' if we found a value
    if website_field and website_value:
        # Remove all website-related fields
        for field in website_aliases:
            if field in json_data:
                del json_data[field]
        # Add the standardized field
        json_data['website'] = website_value.strip()
    
    return json_data

def extract_text_pdf(pdf_path):
    loader = PDFPlumberLoader(pdf_path)
    docs = loader.load()
    text = ''
    for doc in docs:
        text += doc.page_content
    return text

def process_resume(pdf_path, index=None):
    if not client:
        st.error("GROQ_API_KEY not found in environment variables")
        return None
    
    # Extract text from PDF
    context = extract_text_pdf(pdf_path)
    
    # Call LLM API
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": human_prompt.format(context=context)
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        
        output = completion.choices[0].message.content
        
        # Extract JSON content
        json_start = output.find('{')
        json_end = output.rfind('}') + 1
        json_content = output[json_start:json_end]
        
        json_data = json.loads(json_content)
        cleaned_data = clean_resume_data(json_data)
        
        return cleaned_data
        
    except Exception as e:
        st.error(f"Error processing resume: {str(e)}")
        return None

def create_download_link(data, filename):
    """Create a download link for JSON data"""
    json_str = json.dumps(data, indent=2)
    b64 = base64.b64encode(json_str.encode()).decode()
    href = f'<a href="data:application/json;base64,{b64}" download="{filename}">Download JSON File</a>'
    return href

def main():
    st.set_page_config(page_title="Resume Parser", page_icon="📄", layout="wide")
    
    st.title("📄 Resume Parser")
    st.markdown("Upload PDF resumes to extract structured data in JSON format")
    
    # File uploader
    uploaded_files = st.file_uploader("Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)
    
    if uploaded_files:
        st.success(f"Uploaded {len(uploaded_files)} file(s)")
        
        # Process each file
        for i, uploaded_file in enumerate(uploaded_files):
            st.divider()
            st.subheader(f"Processing: {uploaded_file.name}")
            
            # Save to temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.getvalue())
                tmp_path = tmp.name
            
            # Process the resume
            with st.spinner(f"Extracting data from {uploaded_file.name}..."):
                json_data = process_resume(tmp_path, i+1)
                
                # Remove temp file
                try:
                    os.unlink(tmp_path)
                except:
                    pass
            
            if json_data:
                # Create columns for preview and download
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.subheader("Extracted Data Preview")
                    st.json(json_data)
                
                with col2:
                    st.subheader("Download")
                    # Generate filename with timestamp
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"resume_data_{i+1}_{timestamp}.json"
                    
                    # Create download link
                    st.markdown(create_download_link(json_data, filename), unsafe_allow_html=True)
                    
                    # Show basic info
                    if 'name' in json_data:
                        st.metric("Candidate Name", json_data['name'])
                    if 'email' in json_data:
                        st.metric("Email", json_data['email'])
                    if 'skills' in json_data and json_data['skills']:
                        st.write("**Skills:**")
                        st.write(", ".join(json_data['skills']))
            else:
                st.error(f"Failed to process {uploaded_file.name}")

if __name__ == "__main__":
