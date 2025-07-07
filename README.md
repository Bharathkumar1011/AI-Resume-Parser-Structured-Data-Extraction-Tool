# 📄 PARSER-AI: Resume Parser & Structured Data Extraction Tool

**PARSER-AI** is an AI-powered tool that extracts structured data from unstructured resume PDFs using the **Groq SDK with LLaMA 70B**. It supports multi-file uploads and generates clean, structured JSON files — ideal for downstream applications like **ranking, filtering, or analytics** in hiring systems.

A user-friendly **Streamlit** interface allows batch uploads, data previews, and downloads of parsed results.

---

## 🚀 Features

- 📥 Upload multiple PDF resumes at once  
- 🧠 Extracts key fields:
  - Name  
  - Email  
  - Skills  
  - Education  
  - Work Experience  
- ⚡ Fast parsing via **Groq LLaMA 70B** (direct SDK integration)  
- 💾 Outputs **clean JSON** for easy integration  
- 🌐 Streamlit web interface for smooth interaction  

---

## 🧠 How It Works

1. **PDF Text Extraction** using `pdfplumber`  
2. **Prompt-Based Parsing** via Groq SDK (LLaMA 70B) with custom system/human prompts  
3. **Structured JSON Output** for each resume  
4. **Streamlit App Workflow**:
   - Upload one or more PDFs  
   - Preview structured data  
   - Download JSON files  

---

## 📂 Input & Output

### 📤 Input

- One or more resume files in **PDF** format  
- Example input file:  
  [`17823436.rank5.pdf`](https://github.com/Bharathkumar1011/PARSER-AI-Resume-Parser-Structured-Data-Extraction-Tool/blob/main/PARSER-APP%20INPUT/17823436.rank5.pdf)

### 📥 Output

Each file is converted into structured JSON. Example:

```json
{
  "Contact Information": {
    "Name": "Aaditya Vijay Hirurkar",
    "Email": null,
    "Phone Number": null,
    "Website/Portfolio/LinkedIn": null,
    "Github Profile": null
  },
  "Education": {
    "Institution Name": "University of Mumbai",
    "Degree": "Bachelor of Engineering, Information Technology",
    "Graduation Date": "2008"
  },
  "Experience": [
    {
      "Job Title": "Business Analyst Sr. Technical Business Analyst",
      "Company Name": "Company Name",
      "Dates of Employment": "Jul 2011 to Dec 2013",
      "Description": "Requirement Gathering, Release management, Product management, Client handling, etc."
    }
  ],
  "Skills": {
    "Skills": [
      "C", "C++", "Java", "Oracle", "MS SQL Server",
      "Linux", "J2EE", "Eclipse", "Crystal Reports"
    ]
  }
}
## 🛠 Tech Stack

| Tool              | Purpose                                |
|-------------------|----------------------------------------|
| **Python**        | Core language                          |
| **Streamlit**     | Web-based interactive UI               |
| **Groq SDK**      | Fast LLaMA 70B inference               |
| **pdfplumber**    | PDF content extraction                 |
| **python-dotenv** | Environment variable management        |

---

## 📦 Installation

```bash
git clone https://github.com/Bharathkumar1011/PARSER-AI-Resume-Parser-Structured-Data-Extraction-Tool.git
cd PARSER-AI-Resume-Parser-Structured-Data-Extraction-Tool
pip install -r requirements.txt
# 🔐 API Key Setup

Create a `.env` file in the root folder and add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

# ▶️ Run the App

```bash
streamlit run ParserstreamlitApp.py
```

Open your browser and visit:  
[http://localhost:8501](http://localhost:8501)

---

# 📄 Requirements

```text
python-dotenv       # For managing Groq API keys  
groq                # LLM SDK (LLaMA 70B)  
pdfplumber          # PDF text extraction  
streamlit           # Web UI  
```

---

# 💡 Use Cases

- Resume filtering and ranking systems  
- ATS (Applicant Tracking System) input preparation  
- HR automation tools  
- AI-based candidate evaluation platforms

---

# 📬 Contact

Created by **Bharath Kumar**

For questions or suggestions, please open an issue on the GitHub repo
