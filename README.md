# ATS Resumer – Resume Builder and Optimizer

A complete, user-friendly, web-based **Applicant Tracking System (ATS) Resume Optimizer and Builder** mini-project built with **Python** and **Streamlit**.

This project helps job seekers create professional, ATS-compliant resumes, analyze job descriptions, identify matching keywords, calculate ATS compatibility scores, and download high-resolution, single-column PDF resumes with a clean corporate layout.

## 👥 Project Team

This mini project was developed by the following team members:

- M. Katamaiah
- P. Naveen
- B. Charan Deekshith
- B. Rajasekar
- C. Yogananda

---

## 📌 Features & Highlights

- **9-Stage Complete Workflow**: From initial profile creation to job description benchmarking, ATS scoring, content optimization, and PDF generation.
- **Strict Single-Column ATS Layout**: Uses standardized typography and semantic sections (Summary, Skills, Experience, Projects, Education) that pass ATS parsers (Taleo, Workday, Greenhouse).
- **Intelligent Keyword Matching Engine**: Analyzes job descriptions for hard skills, soft skills, tools, and databases with regex-based boundary recognition.
- **Visual Match Score & Metrics**: Radial score indicators, matched keyword badges (green), missing keyword alerts (amber), and actionable recommendations.
- **Ethical Resume Optimizer**: Generates role-tailored professional summaries and allows users to incorporate missing keywords only if they genuinely possess those skills.
- **One-Click ReportLab PDF Generator**: Instant compilation of ATS-friendly PDF documents.
- **Resume Import & Export**: Supports uploading existing PDF/TXT resumes or backing up data via JSON.
- **Pre-Loaded Sample Dataset**: Includes demo profile for *M. Katamaiah* and sample job descriptions for Python Developer, Java Developer, Web Developer, Data Analyst, and Software Engineer.

---

## 🛠️ Technology Stack

| Component | Technology | Description |
|---|---|---|
| **Programming Language** | Python 3.10+ / 3.14 | Core language for processing & web server |
| **Frontend Framework** | Streamlit | Modern reactive web UI with custom blue-and-white theme |
| **PDF Generation Engine** | ReportLab 5.1.0 | Single-column ATS-compliant document formatting |
| **PDF & Text Extraction** | PyPDF 6.19.0 / PyMuPDF | Extracts text and structure from uploaded resume PDFs |
| **Data Handling** | Python & Pandas | Structured storage and tabular transformations |
| **Text Processing** | Python Regex & NLP Taxonomy | Domain-specific keyword matching and tokenization |

---

## 📁 Project Structure

```text
ATS resumer1/
├── app.py                      # Main Streamlit web application & sidebar router
├── requirements.txt            # Python dependencies
├── README.md                   # Installation & execution manual
├── PROJECT_REPORT.md           # Comprehensive academic mini-project report
├── test_app.py                 # Automated unit and integration test suite
├── assets/
│   ├── style.css               # Professional blue-and-white corporate UI styling
│   └── workflow_stages.jpg     # 9-Stage visual workflow reference diagram
└── modules/
    ├── __init__.py
    ├── home.py                 # Module 1: Home Page & feature overview
    ├── resume_builder.py       # Module 2: Stages 2 & 3 (Personal, Education, Skills, Work, Projects)
    ├── job_analyzer.py         # Module 3 & 4: Stages 4 & 5 (Job description input & ATS scoring)
    ├── resume_optimizer.py     # Module 5: Stage 6 (Summary enhancer & missing skill integrator)
    ├── pdf_generator.py        # Module 6: Stages 7 & 8 (ReportLab single-column ATS PDF generator)
    ├── my_resumes.py           # Module 7: Stage 9 (Resume preview, saved library, JSON export)
    ├── resume_parser.py        # PDF/text resume parser using PyPDF
    ├── sample_data.py          # Pre-loaded candidate profiles and role job descriptions
    ├── settings.py             # Configuration preferences and taxonomy viewer
    └── utils.py                # Regex extraction, keyword taxonomy, and ATS matching algorithms
```

---

## 🚀 Installation & Execution Guide (VS Code on Windows)

### Step 1: Open the Project in Visual Studio Code
1. Launch **Visual Studio Code**.
2. Go to **File** > **Open Folder...** and select:
   ```
   C:\Users\<Your_Username>\Downloads\ATS resumer1
   ```
3. Open the integrated terminal (`Ctrl + ~` or **Terminal** > **New Terminal**).

---

### Step 2: (Optional) Create a Python Virtual Environment
To isolate project dependencies, create and activate a virtual environment:

```powershell
# In PowerShell / Command Prompt
py -m venv venv

# Activate virtual environment on Windows
.\venv\Scripts\Activate.ps1
```

> *Tip: If you encounter an execution policy error in PowerShell, run:*
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

---

### Step 3: Install Required Dependencies
Install all required libraries using `pip`:

```powershell
pip install -r requirements.txt
```
*Dependencies installed:*
- `streamlit`
- `reportlab`
- `pandas`
- `pypdf`

---

### Step 4: Run the Automated Test Suite
Before launching the UI, verify your installation by running the automated test suite:

```powershell
py test_app.py
```

*Expected output:*
```text
============================================================
ATS Resumer Mini-Project - Automated Test Suite
============================================================
[1/6] Testing module imports...
  -> All modules and third-party dependencies imported successfully.
[2/6] Validating sample data...
  -> Sample candidate data and 5 role descriptions validated.
[3/6] Testing keyword extraction...
  -> Successfully extracted 6 keywords: ['Django', 'Docker', 'Flask', 'Python', 'REST APIs', 'SQL']
[4/6] Testing ATS score calculation against benchmark...
  -> ATS Match Score: 82%
  -> Matched Skills (10): ['Agile', 'Communication', 'Data Analysis', 'Django', 'Flask', 'MySQL', 'Problem Solving', 'Python', 'SQL', 'Web Development']
  -> Missing Keywords (3): ['Git', 'REST APIs', 'Version Control']
[5/6] Testing ReportLab PDF generation and round-trip parsing...
  -> ReportLab PDF generated: 3716 bytes.
  -> PDF parse round-trip verified successfully.
[6/6] Testing AI/Rule-based summary optimization...
  -> Summary optimization passed.
============================================================
ALL TESTS PASSED! (6/6 Test Cases Succeeded)
============================================================
```

---

### Step 5: Launch the ATS Resumer Web Application
Start the Streamlit development server:

```powershell
py -m streamlit run app.py
```

The application will automatically start and open in your default web browser at:
```text
http://localhost:8501
```

---

## 🔄 The 9-Stage Workflow Demonstration

1. **Stage 1 (Launch App)**: View the Home Page and click **"Load Sample Profile"** or **"Get Started"**.
2. **Stage 2 (Personal & Education)**: Enter contact details (Name, Email, Phone, Location) and degrees.
3. **Stage 3 (Skills & Experience)**: Add technical skills using quick-add tags, work history, and projects.
4. **Stage 4 (Job Description)**: Select target role (e.g. *Python Developer*) and paste the job description (or click **"Load Sample Job Description"**).
5. **Stage 5 (Analyze Resume)**: View the ATS Match Score (82%), matched skills, and missing keywords.
6. **Stage 6 (Optimize Resume)**: Select verified missing skills and generate a tailored summary. Click **"Apply Suggestions"**.
7. **Stage 7 (Generate Resume)**: Review the final formatted resume on the clean preview card.
8. **Stage 8 (Download PDF)**: Click **"📥 Download PDF"** to get your ATS-compliant PDF.
9. **Stage 9 (Ready to Use)**: View completion screen and access saved resumes under **My Resumes**.

---

## ❓ Troubleshooting FAQ

### 1. `streamlit: command not found`
Run Streamlit explicitly through the Python launcher:
```powershell
py -m streamlit run app.py
```

### 2. Port `8501` is already in use
Specify an alternate port:
```powershell
py -m streamlit run app.py --server.port 8502
```

### 3. Missing packages
Ensure you installed requirements:
```powershell
py -m pip install -r requirements.txt
```

---

## 📜 License & Academic Notice
Developed as a computer science mini-project demonstration for resume optimization, natural language processing, and ATS compliance. Free for educational and personal use.
