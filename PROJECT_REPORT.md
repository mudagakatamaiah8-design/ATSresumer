# ATS Resumer – Resume Builder and Optimizer
## Comprehensive College Mini-Project Report

**Academic Year:** 2025–2026  
**Project Domain:** Natural Language Processing (NLP), Web Technologies & Document Engineering  
**Technology Stack:** Python 3.14, Streamlit, ReportLab, PyPDF, Pandas  

---

## 1. Project Abstract

In today's competitive employment marketplace, over 75% of job applications are filtered out by automated **Applicant Tracking Systems (ATS)** prior to reaching a human hiring manager. Traditional resume builders prioritize visual flair, complex multi-column tables, text boxes, and graphical elements—features that directly cause ATS parsing errors, resulting in qualified candidates being overlooked.

**ATS Resumer** is a complete, user-friendly, web-based software application engineered in Python and Streamlit to resolve this challenge. The system enables candidates to construct standard-compliant single-column resumes, paste job descriptions across various engineering roles (Python Developer, Java Developer, Web Developer, Data Analyst, Software Engineer), and execute algorithmic keyword matching. The application evaluates hard and soft competencies, calculates an ATS match score, pinpoints missing keywords, generates role-tailored summaries, and produces downloadable, high-fidelity PDFs via ReportLab. By upholding strict ethical guidelines—never inventing unverified qualifications—the system optimizes applicant visibility while maintaining document integrity.

---

## 2. Project Objectives

1. **ATS Standard Compliance:** Ensure generated resumes utilize a clean, single-column typographical layout with standard fonts (Helvetica) and semantic section headings for 100% parser compatibility.
2. **Automated Keyword Extraction:** Implement regex tokenization and domain taxonomy mapping to extract technical skills, tools, frameworks, and methodologies from job descriptions.
3. **Objective ATS Scoring Engine:** Compute a weighted compatibility score between candidate credentials and target job descriptions to quantify hiring alignment.
4. **Interactive Skill Gap Identification:** Provide transparent visual feedback separating matched competencies (green) from missing keywords (amber) alongside role-specific recommendations.
5. **Ethical Resume Optimization:** Facilitate content improvement by generating targeted professional summaries and prompting users to incorporate missing keywords only when they genuinely possess the required skill.
6. **Robust PDF Generation:** Compile verified candidate data into industry-grade PDF documents using ReportLab without external OS-level printer dependencies.
7. **Educational Usability:** Provide pre-loaded demonstration profiles (*M. Katamaiah*, B.Tech JNTU Hyderabad) and standard job descriptions to enable rapid demonstration during college project reviews.

---

## 3. System Requirements

### 3.1 Hardware Requirements
- **Processor:** Dual-core 2.0 GHz Intel/AMD or Apple Silicon processor (minimum); Quad-core i5/Ryzen 5 (recommended).
- **RAM:** Minimum 4 GB RAM (8 GB recommended for optimal browser responsiveness).
- **Storage:** 500 MB free hard disk space for Python runtime, libraries, and generated PDF assets.
- **Display:** 1280 x 720 minimum screen resolution (1920 x 1080 Full HD recommended).

### 3.2 Software Requirements
- **Operating System:** Windows 10/11, macOS Monterey+, or Linux (Ubuntu 20.04+).
- **Programming Language:** Python 3.10 to Python 3.14 (64-bit).
- **Web Browser:** Google Chrome, Microsoft Edge, Mozilla Firefox, or Safari (modern version with JavaScript enabled).
- **IDE:** Visual Studio Code (VS Code) with Python extension.
- **Core Python Libraries:**
  - `streamlit >= 1.30.0` (Reactive web frontend)
  - `reportlab >= 4.0.0` (PDF compilation and typography)
  - `pandas >= 2.0.0` (Data handling and tabular structures)
  - `pypdf >= 4.0.0` (PDF document reading and extraction)

---

## 4. System Architecture and Workflow Diagram

The ATS Resumer employs a modular, pipeline-oriented architecture consisting of five architectural tiers: Presentation Layer, Parsing & Ingestion Layer, ATS Analysis & Scoring Engine, Optimization Layer, and Document Compilation Engine.

### 4.1 System Architecture Diagram

```mermaid
flowchart TD
    subgraph Presentation_Layer["Presentation Tier (Streamlit Web App)"]
        UI_Home["Module 1: Home Page"]
        UI_Builder["Module 2: Resume Builder (Stages 2 & 3)"]
        UI_Analyzer["Modules 3 & 4: Job Analyzer & ATS Score (Stages 4 & 5)"]
        UI_Optimizer["Module 5: Resume Optimizer (Stage 6)"]
        UI_Output["Module 6 & 7: Final Preview & PDF Download (Stages 7, 8, 9)"]
    end

    subgraph Logic_Layer["Logic & Processing Tier"]
        Parser["Resume Parser (PyPDF / PyMuPDF)"]
        Taxonomy["Keyword Taxonomy & Regex Extractor"]
        Scorer["ATS Compatibility Scoring Engine"]
        SummaryGen["Professional Summary Generator"]
    end

    subgraph Data_Layer["Storage & Data Tier"]
        State["Streamlit Session State"]
        JSONStore["Local JSON Resume Storage"]
        SampleDB["Pre-loaded Demo Profiles & Role Descriptions"]
    end

    subgraph Output_Tier["Output Generation"]
        ReportLabEngine["ReportLab Flowable Engine"]
        PDFFile["ATS-Compliant Single-Column PDF"]
    end

    UI_Home --> UI_Builder
    UI_Builder --> State
    UI_Builder -.-> Parser
    SampleDB --> State
    State --> Scorer
    UI_Analyzer --> Taxonomy
    Taxonomy --> Scorer
    Scorer --> UI_Analyzer
    UI_Analyzer --> UI_Optimizer
    UI_Optimizer --> SummaryGen
    SummaryGen --> State
    State --> ReportLabEngine
    ReportLabEngine --> PDFFile
    PDFFile --> UI_Output
    State <--> JSONStore
```

### 4.2 The 9-Stage User Workflow

The application mirrors the workflow represented below:

```mermaid
flowchart LR
    S1["1. Open App"] --> S2["2. Personal & Edu"]
    S2 --> S3["3. Skills & Exp"]
    S3 --> S4["4. Enter JD"]
    S4 --> S5["5. Analyze"]
    S5 --> S6["6. Optimize"]
    S6 --> S7["7. Generate Resume"]
    S7 --> S8["8. Download PDF"]
    S8 --> S9["9. Ready to Use"]
```

---

## 5. Module Descriptions

### Module 1: Home Page (`modules/home.py`)
- Provides an aesthetic hero banner highlighting the title *ATS Resumer* and the core motto *Build | Analyze | Optimize*.
- Offers one-click action buttons: "Get Started", "Load Sample Profile", and "Analyze Target Job".
- Displays three educational cards summarizing why ATS compliance is critical for job seekers.
- Renders an interactive 9-step roadmap showing current workflow progression.

### Module 2: Resume Creation (`modules/resume_builder.py`)
- **Stage 2 (Personal & Educational Details):** Collects candidate full name, target designation, contact email, phone number, location, and social links (LinkedIn, GitHub). Collects education history including degree, college/university, graduation year, and GPA.
- **Stage 3 (Skills, Experience and Projects):** Captures technical competencies as interactive pill badges with quick-add chips; captures employment records with designation, company, dates, and bulleted achievements; captures project portfolios with tech stacks and descriptions.
- **Import Capability:** Features an integrated PDF/text uploader using PyPDF to parse existing resumes directly into the form fields.

### Module 3: Job Description Input (`modules/job_analyzer.py`)
- Provides an expansive text area allowing candidates to paste arbitrary job postings.
- Features a role selector supporting *Python Developer*, *Java Developer*, *Web Developer*, *Data Analyst*, and *Software Engineer*.
- Provides a one-click button to load realistic sample job postings for instantaneous evaluation.

### Module 4: Resume Analysis & Scoring (`modules/job_analyzer.py` & `modules/utils.py`)
- Executes text normalization and regex-based token matching against an industry keyword taxonomy.
- Computes a weighted ATS Compatibility Score based on:
  $$\text{Score} = \left(\frac{\text{Matched Keywords}}{\text{Total JD Keywords}} \times 80\right) + \text{Section Completeness Bonus (up to 20)}$$
- Visually categorizes results into:
  - **Key Matched Skills:** Displayed in green badges with checkmarks.
  - **Missing Keywords:** Displayed in amber warning tags indicating skill gaps.
  - **Actionable Suggestions:** Provides bulleted recommendations for formatting and keyword inclusion.

### Module 5: Resume Optimization (`modules/resume_optimizer.py`)
- Implements an AI/rule-based **Professional Summary Enhancer** that drafts an opening career statement incorporating the candidate's target title and verified competencies.
- Features an **Interactive Skill Integration Assistant**: Displays checkboxes for missing keywords, allowing candidates to select only those skills they genuinely possess (preventing fabrication of qualifications).
- Provides an "Apply Suggestions & Update Resume" button that updates the session model and recalculates the ATS score.

### Module 6: ReportLab PDF Compilation (`modules/pdf_generator.py`)
- Constructs an in-memory document using ReportLab Platypus (`SimpleDocTemplate`, `Paragraph`, `HRFlowable`, `Table`).
- Adheres to single-column guidelines: standard Helvetica fonts, left-aligned headings, subtle blue accent dividers, clean contact lines, and standardized bullet points.
- Guarantees 100% parseability across parsers without relying on external system fonts or graphics.

### Module 7: Saved Resumes & Success Management (`modules/my_resumes.py`)
- **Stage 7 (Review):** Displays an on-screen preview of the formatted resume paper.
- **Stage 8 (Download):** Offers a direct `st.download_button` to download the compiled PDF.
- **Stage 9 (Ready to Use):** Displays the green celebration screen and provides a local repository where users can save multiple resume variants, reload them, or export/import them via JSON.

---

## 6. Complete Source Code Structure

The source code is organized into a clean modular package:

```
c:\Users\M. KATAMAIAH\Downloads\ATS resumer1\
├── app.py                      # Main entrypoint with state manager & routing
├── requirements.txt            # Dependency definitions
├── README.md                   # Installation & usage documentation
├── PROJECT_REPORT.md           # Mini-project report (this document)
├── test_app.py                 # Automated test suite (6/6 passing tests)
├── assets/
│   ├── style.css               # Blue-and-white custom theme stylesheet
│   └── workflow_stages.jpg     # 9-Stage visual reference graphic
└── modules/
    ├── __init__.py             # Package marker
    ├── home.py                 # Landing page & overview
    ├── resume_builder.py       # Personal, education, skills, experience forms
    ├── job_analyzer.py         # JD text input, keyword matching & analysis
    ├── resume_optimizer.py     # Summary enhancement & skill gap resolution
    ├── pdf_generator.py        # ReportLab ATS PDF rendering engine
    ├── my_resumes.py           # Saved resumes manager & download view
    ├── resume_parser.py        # PyPDF parser for uploaded resumes
    ├── sample_data.py          # Pre-configured demo data & role postings
    ├── settings.py             # User preferences & taxonomy inspector
    └── utils.py                # Regex extraction, keyword dictionary & scoring
```

---

## 7. Installation and Execution Steps

### Step 1: Open in Visual Studio Code
Open your terminal in Visual Studio Code and navigate to the project root:
```powershell
cd "c:\Users\M. KATAMAIAH\Downloads\ATS resumer1"
```

### Step 2: (Optional) Set Up Virtual Environment
```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 4: Execute Automated Test Suite
```powershell
py test_app.py
```

### Step 5: Run the Streamlit Application
```powershell
py -m streamlit run app.py
```
Open your browser to `http://localhost:8501`.

---

## 8. Detailed Walkthrough of the Nine Main Workflow Stages

| Stage # | Stage Title | User Actions & System Operations |
|---|---|---|
| **Stage 1** | **Launch Application** | The user launches the application in the browser. The home screen presents the project banner, feature cards, and the **"Load Sample Profile"** button for instant demonstration. |
| **Stage 2** | **Enter Personal & Educational Details** | The candidate enters contact details (Full Name: *M. Katamaiah*, Email: *katamaiah@example.com*, Phone: *+91 9876543210*, Location: *Hyderabad, India*) and university credentials (*B.Tech, JNTU Hyderabad, 2020*). |
| **Stage 3** | **Add Skills, Experience and Projects** | Technical skills (*Python, Django, SQL, JavaScript, MySQL*) are selected via interactive tags. Work history at *ABC Technologies* and projects (*ATS Resumer*) are documented with bulleted achievements. |
| **Stage 4** | **Enter Job Description** | The user selects *Python Developer* from the role dropdown and pastes the job posting requiring Django, Flask, SQL, data analysis, and communication skills. |
| **Stage 5** | **Analyze Resume** | The ATS engine compares resume content against the posting. The system displays an **82% Match Score**, lists key matched skills in green, identifies missing keywords (*Flask, Git, REST APIs*), and outputs tailored recommendations. |
| **Stage 6** | **Optimize Your Resume** | The candidate follows recommendations. The AI/Rule-based summary enhancer generates an optimized career statement. The candidate selects genuinely possessed missing skills using checkboxes and clicks **"Apply Suggestions"**. |
| **Stage 7** | **Generate Final Resume** | The application updates the resume model, recalculates the score, and renders a live, formatted resume card reflecting the optimized content. |
| **Stage 8** | **Download as PDF** | The user clicks **"📥 Download PDF"**. ReportLab renders the document into a clean, single-column, ATS-compliant PDF and serves it directly to the browser. |
| **Stage 9** | **Run and Use Your ATS Resumer** | The green celebration screen confirms ATS screening readiness. The user can start a new resume or store/export the resume in the **My Resumes** library. |

---

## 9. Testing Results

An automated test suite (`test_app.py`) was executed to validate system integrity across six comprehensive test cases:

| Test ID | Module Tested | Test Description | Test Inputs | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|---|
| **TC-01** | `imports` | Verify core dependencies and module accessibility | `streamlit, reportlab, pandas, pypdf` | All libraries import without `ImportError` | All libraries imported successfully | **PASSED** |
| **TC-02** | `sample_data` | Validate demo dataset integrity | `DEFAULT_RESUME` & `SAMPLE_JOB_DESCRIPTIONS` | Valid candidate record with at least 5 skills & 5 role descriptions | Record contains M. Katamaiah, 10 skills, 5 JDs | **PASSED** |
| **TC-03** | `utils.extract` | Test regex keyword extraction engine | String containing "Python, Django, Flask, SQL, Docker" | List containing canonical names for all 5 technologies | Successfully extracted `['Django', 'Docker', 'Flask', 'Python', 'REST APIs', 'SQL']` | **PASSED** |
| **TC-04** | `utils.scorer` | Test ATS match score against benchmark | M. Katamaiah profile vs Python Dev job description | ATS score $\ge 75\%$, with both matched & missing skills | Score: 82%, Matched: 10 skills, Missing: 3 skills | **PASSED** |
| **TC-05** | `pdf_generator` & `parser` | Verify PDF compilation & text round-trip extraction | Resume dictionary passed to ReportLab and read back via PyPDF | PDF size $> 1000$ bytes; text contains candidate name & college | PDF size: 3716 bytes; Name & JNTU Hyderabad extracted | **PASSED** |
| **TC-06** | `resume_optimizer` | Verify role-targeted summary synthesis | Target role: Python Developer + skills list | Synthesized text contains role and top technologies | Summary synthesized cleanly with all target terms | **PASSED** |

**Summary:** 6 out of 6 test cases passed (100% test success rate).

---

## 10. Conclusion and Future Enhancements

### 10.1 Conclusion
The **ATS Resumer** mini-project demonstrates how software engineering and natural language processing can be applied to solve real-world recruitment challenges. By combining Streamlit's reactive web framework with ReportLab's document rendering capabilities and a robust regex taxonomy parser, the system provides candidates with a transparent, privacy-first, and ATS-compliant platform to optimize their resumes. The application satisfies all project objectives and serves as an exemplary computer science mini-project demonstration.

### 10.2 Future Enhancements
1. **Large Language Model (LLM) Integration:** Incorporate lightweight open-source models (e.g. LLaMA-3 or Mistral) via Ollama/HuggingFace for contextual bullet point rewriting and grammatical enhancement.
2. **Multi-Template ATS PDF Styles:** Provide candidates with selectable ATS-friendly color accents and typography pairings (Modern Slate, Executive Navy, Classic Monochrome).
3. **Cover Letter Generator:** Automatically synthesize targeted cover letters matching the parsed job description keywords.
4. **LinkedIn Profile URL Scraper:** Allow candidates to automatically populate resume details by connecting their professional profile links.
