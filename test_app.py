"""
Automated Test Suite for ATS Resumer Mini-Project.
Validates module imports, ATS scoring engine, PDF generation, and text parsing.
"""

import sys
import os

# Add root directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    print("[1/6] Testing module imports...")
    import streamlit
    import reportlab
    import pandas
    import pypdf
    from modules.sample_data import DEFAULT_RESUME, SAMPLE_JOB_DESCRIPTIONS
    from modules.utils import calculate_ats_match, extract_keywords_from_text, generate_optimized_summary
    from modules.pdf_generator import generate_ats_resume_pdf
    from modules.resume_parser import extract_text_from_pdf, parse_resume_content
    print("  -> All modules and third-party dependencies imported successfully.")

def test_sample_data():
    print("[2/6] Validating sample data...")
    from modules.sample_data import DEFAULT_RESUME, SAMPLE_JOB_DESCRIPTIONS
    assert DEFAULT_RESUME["personal"]["full_name"] == "M. Katamaiah"
    assert DEFAULT_RESUME["personal"]["target_role"] == "Python Developer"
    assert len(DEFAULT_RESUME["technical_skills"]) >= 5
    assert len(SAMPLE_JOB_DESCRIPTIONS) >= 5
    print("  -> Sample candidate data and 5 role descriptions validated.")

def test_keyword_extraction():
    print("[3/6] Testing keyword extraction...")
    from modules.utils import extract_keywords_from_text
    sample_text = "Looking for a Python Developer with Django, Flask, SQL, REST APIs, and Docker experience."
    keywords = extract_keywords_from_text(sample_text)
    expected = ["Docker", "Django", "Flask", "Python", "REST APIs", "SQL"]
    for exp in expected:
        assert exp in keywords, f"Expected keyword '{exp}' was not extracted"
    print(f"  -> Successfully extracted {len(keywords)} keywords: {keywords}")

def test_ats_match_scoring():
    print("[4/6] Testing ATS score calculation against benchmark...")
    from modules.sample_data import DEFAULT_RESUME, SAMPLE_JOB_DESCRIPTIONS
    from modules.utils import calculate_ats_match
    jd = SAMPLE_JOB_DESCRIPTIONS["Python Developer"]
    result = calculate_ats_match(DEFAULT_RESUME, jd, "Python Developer")
    assert result["score"] >= 70, f"Expected ATS score >= 70, got {result['score']}"
    assert len(result["matched_skills"]) > 0
    assert len(result["missing_skills"]) > 0
    print(f"  -> ATS Match Score: {result['score']}%")
    print(f"  -> Matched Skills ({len(result['matched_skills'])}): {result['matched_skills']}")
    print(f"  -> Missing Keywords ({len(result['missing_skills'])}): {result['missing_skills']}")

def test_pdf_generation_and_parsing():
    print("[5/6] Testing ReportLab PDF generation and round-trip parsing...")
    from modules.sample_data import DEFAULT_RESUME
    from modules.pdf_generator import generate_ats_resume_pdf
    from modules.resume_parser import extract_text_from_pdf
    
    pdf_bytes = generate_ats_resume_pdf(DEFAULT_RESUME)
    assert len(pdf_bytes) > 1000, "Generated PDF is too small or empty"
    print(f"  -> ReportLab PDF generated: {len(pdf_bytes)} bytes.")
    
    # Verify PDF text extraction
    extracted_text = extract_text_from_pdf(pdf_bytes)
    assert "M. Katamaiah" in extracted_text, "Candidate name missing from parsed PDF"
    assert "Python Developer" in extracted_text, "Target role missing from parsed PDF"
    assert "JNTU Hyderabad" in extracted_text, "University name missing from parsed PDF"
    print("  -> PDF parse round-trip verified successfully (Candidate name, role, and university found).")

def test_summary_optimization():
    print("[6/6] Testing AI/Rule-based summary optimization...")
    from modules.sample_data import DEFAULT_RESUME
    from modules.utils import generate_optimized_summary
    opt_sum = generate_optimized_summary(DEFAULT_RESUME, "Python Developer", ["Python", "Django", "SQL", "Flask"])
    assert "Python Developer" in opt_sum
    assert "Django" in opt_sum
    print("  -> Summary optimization passed.")

if __name__ == "__main__":
    print("=" * 60)
    print("ATS Resumer Mini-Project - Automated Test Suite")
    print("=" * 60)
    try:
        test_imports()
        test_sample_data()
        test_keyword_extraction()
        test_ats_match_scoring()
        test_pdf_generation_and_parsing()
        test_summary_optimization()
        print("=" * 60)
        print("ALL TESTS PASSED! (6/6 Test Cases Succeeded)")
        print("=" * 60)
    except Exception as e:
        print(f"Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
