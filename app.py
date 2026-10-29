"""
ATS Resumer – Resume Builder and Optimizer
Main Application Entrypoint (Streamlit)
"""

import copy
import os
import streamlit as st
from modules.sample_data import DEFAULT_RESUME, SAMPLE_JOB_DESCRIPTIONS
from modules.home import render_home_page
from modules.resume_builder import render_resume_builder
from modules.job_analyzer import render_job_analyzer
from modules.resume_optimizer import render_resume_optimizer
from modules.my_resumes import render_my_resumes
from modules.settings import render_settings

# Configure page layout and metadata
st.set_page_config(
    page_title="ATS Resumer – Resume Builder and Optimizer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load and apply custom CSS styling
def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "assets", "style.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Initialize Session State
if "resume_data" not in st.session_state:
    st.session_state["resume_data"] = copy.deepcopy(DEFAULT_RESUME)

if "target_role" not in st.session_state:
    st.session_state["target_role"] = "Python Developer"

if "job_description" not in st.session_state:
    st.session_state["job_description"] = SAMPLE_JOB_DESCRIPTIONS.get("Python Developer", "")

if "nav_selection" not in st.session_state:
    st.session_state["nav_selection"] = "Home"

if "saved_resumes" not in st.session_state:
    st.session_state["saved_resumes"] = []

# ==========================================================
# SIDEBAR NAVIGATION (Matching Redesigned UI)
# ==========================================================
with st.sidebar:
    st.markdown("""
        <div style="padding: 10px 0 20px 0; text-align: left;">
            <div style="font-size: 24px; font-weight: 800; color: #ffffff; display: flex; align-items: center; gap: 10px;">
                <span style="background: #0066cc; padding: 4px 8px; border-radius: 6px; font-size: 18px;">📄</span> ATS Resumer
            </div>
            <div style="font-size: 12px; color: #94a3b8; margin-top: 6px; margin-left: 2px;">
                Resume Builder & Optimizer
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    sidebar_nav_options = [
        "Home",
        "Create Resume",
        "Analyze Resume",
        "My Resumes",
        "Settings"
    ]
    
    current_nav = st.session_state["nav_selection"]
    # If currently in Optimize Resume, map sidebar highlight appropriately or keep track
    active_idx = sidebar_nav_options.index(current_nav) if current_nav in sidebar_nav_options else 0
        
    nav_icons = {
        "Home": "🏠",
        "Create Resume": "📄",
        "Analyze Resume": "🔍",
        "My Resumes": "📁",
        "Settings": "⚙️"
    }
    
    selected_page = st.radio(
        "Navigation Menu:",
        sidebar_nav_options,
        index=active_idx,
        format_func=lambda x: f"{nav_icons.get(x, '')}  {x}",
        label_visibility="collapsed"
    )
    
    # Only override nav_selection if the user actively changed the radio button
    if selected_page != current_nav and current_nav in sidebar_nav_options:
        st.session_state["nav_selection"] = selected_page
    elif current_nav not in sidebar_nav_options and selected_page != "Home":
        st.session_state["nav_selection"] = selected_page

    st.markdown("---")
    
    # Candidate Status Widget in Sidebar
    active_cand = st.session_state["resume_data"].get("personal", {}).get("full_name", "Not set")
    active_role = st.session_state["resume_data"].get("personal", {}).get("target_role", "Developer")
    current_score = st.session_state.get("analysis_result", {}).get("score", None)
    
    st.markdown(f"""
        <div style="background-color: rgba(255, 255, 255, 0.05); padding: 14px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.1);">
            <div style="font-size: 11px; text-transform: uppercase; color: #94a3b8; font-weight: 700;">Active Profile</div>
            <div style="font-size: 15px; font-weight: 700; color: #ffffff; margin-top: 2px;">{active_cand}</div>
            <div style="font-size: 12px; color: #38bdf8;">{active_role}</div>
            {f'<div style="font-size: 13px; font-weight: 700; color: #4ade80; margin-top: 6px;">ATS Score: {current_score}%</div>' if current_score else ''}
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Quick Load Demo Data", use_container_width=True):
        st.session_state["resume_data"] = copy.deepcopy(DEFAULT_RESUME)
        st.session_state["target_role"] = "Python Developer"
        st.session_state["job_description"] = SAMPLE_JOB_DESCRIPTIONS.get("Python Developer", "")
        if "analysis_result" in st.session_state:
            del st.session_state["analysis_result"]
        st.success("Loaded demo dataset!")
        st.rerun()

# ==========================================================
# PAGE ROUTING
# ==========================================================
active_page = st.session_state["nav_selection"]

if active_page == "Home":
    render_home_page()
elif active_page == "Create Resume":
    render_resume_builder()
elif active_page == "Analyze Resume":
    render_job_analyzer()
elif active_page == "Optimize Resume":
    render_resume_optimizer()
elif active_page == "My Resumes":
    render_my_resumes()
elif active_page == "Settings":
    render_settings()
else:
    render_home_page()

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; color: #94a3b8; font-size: 12px; padding: 20px 0; border-top: 1px solid #e2e8f0;">
        <strong>ATS Resumer</strong> – Resume Builder & Optimizer &bull; College Mini-Project &bull; Built with Python & Streamlit
    </div>
""", unsafe_allow_html=True)
