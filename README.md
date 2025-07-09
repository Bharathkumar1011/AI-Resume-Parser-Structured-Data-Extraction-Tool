# 📄 PARSER-AI: Resume Parser & Structured Data Extraction Tool

PARSER-AI is a powerful resume parsing application that takes **multiple PDF files** as input and converts them into **structured JSON outputs**. It uses the Groq API powered by LLaMA 3.3 and incorporates custom, case-sensitive Python logic to accurately extract relevant fields. Designed for seamless integration into workflows like resume ranking, skill gap analysis, and personalized feedback systems, it features a clean Streamlit interface for batch uploads, data previews, and easy result downloads.


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
2. **Parsing** via Groq API(LLaMA 3.3) with custom python logic  
3. **Structured JSON Output** for each resume  
4. **Streamlit App Workflow**:
   - Upload one or more PDFs  
   - Preview structured data  
   - Download JSON files  

---

## 📂 Input & Output

## 📤 Input

### - One or more resume files in **PDF** format  
### - Example input file:  
  [`17823436.rank5.pdf`](https://github.com/Bharathkumar1011/PARSER-AI-Resume-Parser-Structured-Data-Extraction-Tool/blob/main/PARSER-APP%20INPUT/17823436.rank5.pdf)

## 📥 Output

### - Each file is converted into structured JSON. 
### - Example output file:  

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
```

---

## 🛠 Tech Stack

| Tool              | Purpose                                |
|-------------------|----------------------------------------|
| **Python**        | Core language                          |
| **Streamlit**     | Web-based interactive UI               |
| **Groq API**      | Fast LLaMA3.3 inference               |
| **pdfplumber**    | PDF content extraction                 |
| **python-dotenv** | Environment variable management        |

---

## 📦 Installation

```bash
git clone https://github.com/Bharathkumar1011/PARSER-AI-Resume-Parser-Structured-Data-Extraction-Tool.git
cd PARSER-AI-Resume-Parser-Structured-Data-Extraction-Tool
pip install -r requirements.txt
```

---

## 🔐 API Key Setup

Create a `.env` file in the root folder and add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run ParserstreamlitApp.py
```

Open your browser and visit:  
[http://localhost:8501](http://localhost:8501)

---

## 📄 Requirements

```text
python-dotenv       # For managing Groq API keys  
groq                # LLM (API) (LLaMA 3.3)  
pdfplumber          # PDF text extraction  
streamlit           # Web UI  
```

---

## 💡 Use Cases

- Resume filtering and ranking systems
- skill gap analysis and individual upskill feedback 
- ATS (Applicant Tracking System) input preparation  
- HR automation tools  
- AI-based candidate evaluation platforms

---

## 📬 Contact

Created by **Bharath Kumar**

For questions or suggestions, please open an issue on the GitHub repo.
