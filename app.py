import streamlit as st

# ==========================================
# 1. PORTFOLIO DATA (Education Removed)
# ==========================================
PORTFOLIO_DATA = {
    "name": "Omolola Blessing Lawal",
    "role": "Data Scientist",
    "email": "your.email@example.com", 
    "about": "Hi there! I am a Data Scientist with proven ability in analyzing complex datasets to identify trends, develop models and provide actionable insights that guides strategic development of secure and advanced initiatives. My experience spans data cleaning and transformation, data analysis and visualization, AI and machine learning solutions, web scraping and script automation. I am committed to innovation and collaboration and I believe we can make something remarkable together so let’s connect and make a difference through technology and data!",
    "contact": {
        "linkedin": "https://www.linkedin.com/in/omolola-lawal-2a9a45188",
        "github": "https://github.com/Lolita-codes"
    },
    "skills": [
        "Python", "Scikit-Learn", "Pandas", 
        "Seaborn", "Matplotlib", "Plotly",
        "Numpy", "SQL & PostgreSQL", "Tableau", 
        "Langchain", "NLTK", "SpaCy",
        "BeautifulSoup", "FastAPI", "Git & GitHub"
    ],
    "experience": [
        {
            "title": "Informatics Analyst",
            "company": "University College Hospital, Ibadan, Nigeria",
            "date": "Nov 2023 - Nov 2024",
            "points": [
                "Identified trends and opportunities for improving medication management and safety through data.",
                "Maintained inventory management software, ensuring seamless integration with pharmacy dispensing and procurement systems.",
                "Analyzed inventory data to identify usage trends and predict future demand for medications and maintained accurate records of drug stock levels."
            ]
        },
        {
            "title": "Data Scientist Intern",
            "company": "DC Clevertech (Contracted for Stacksuit)",
            "date": "May 2023 - May 2024",
            "points": [
                "Built an AI-powered application, leveraging natural language processing and integrating cloud storage and vector database for file storage and RAG data retrieval.",
                "Analyzed data and developed machine learning models for user segmentation.",
                "Carried out sentiment analysis on customers’ reviews and feedback.",
                "Collaborated with engineering team to understand business objectives and created compelling visualizations to communicate data findings."
            ]
        },
        {
            "title": "Software Developer Intern",
            "company": "DC Clevertech (Contracted for Stacksuit)",
            "date": "April 2022 - April 2023",
            "points": [
                "Maintained code integrity, organization, and applied object-oriented design principle.",
                "Collaborated with the product and engineering team to design and build high quality and reliable APIs and services.",
                "Ensured cross-country optimization.",
                "Debugged, troubleshoot and resolved production issues in a timely fashion."
            ]
        }
    ],
    "projects": [
        {
            "name": "Profitability Analysis",
            "desc": "Analyzes food order data to uncover insights regarding profitability, delivery efficiency, and payment methods.",
            "link": "https://github.com/Lolita-codes/delivery_orders_profitability",
            "image": "https://via.placeholder.com/600x350.png?text=Profitability+Analysis" 
        },
        {
            "name": "HR Churn Analysis",
            "desc": "Analyzes employee attrition trends to identify factors contributing to turnover and predict outcomes.",
            "link": "https://github.com/Lolita-codes/hr_data_analysis",
            "image": "https://via.placeholder.com/600x350.png?text=HR+Churn+Analysis"
        },
        {
            "name": "Customer Segmentation",
            "desc": "Segments customers based on standard FICO credit scores derived from multiple financial factors.",
            "link": "https://github.com/Lolita-codes/credit_score_customer_segmentation",
            "image": "https://via.placeholder.com/600x350.png?text=Customer+Segmentation"
        },
        {
            "name": "User Segmentation",
            "desc": "Segments users based on demographic and behavioral features to optimize ad targeting strategies.",
            "link": "https://github.com/Lolita-codes/user_segmentation",
            "image": "https://via.placeholder.com/600x350.png?text=User+Segmentation"
        },
        {
            "name": "House Price Prediction",
            "desc": "Builds a predictive model that estimates house prices based on various property characteristics.",
            "link": "https://github.com/Lolita-codes/Price_prediction",
            "image": "https://via.placeholder.com/600x350.png?text=House+Price+Prediction"
        },
        {
            "name": "Google Playstore Analysis",
            "desc": "Provides comprehensive insights into the Android app market, from app ratings to category competitiveness.",
            "link": "https://github.com/Lolita-codes/Google_Playstore_Apps",
            "image": "https://via.placeholder.com/600x350.png?text=Playstore+Analysis"
        }
    ],
    "certifications": [
        {
            "name": "The Data Science Course: Complete Bootcamp",
            "issuer": "Udemy",
            "image": "https://via.placeholder.com/400x250.png?text=Data+Science+Bootcamp"
        },
        {
            "name": "FastAPI – The Complete Course",
            "issuer": "Udemy",
            "image": "https://via.placeholder.com/400x250.png?text=FastAPI+Course"
        },
        {
            "name": "Python Django – The Practical Guide",
            "issuer": "Udemy",
            "image": "https://via.placeholder.com/400x250.png?text=Django+Guide"
        },
        {
            "name": "100 Days of Code: Python Pro",
            "issuer": "Udemy",
            "image": "https://via.placeholder.com/400x250.png?text=Python+100+Days"
        },
        {
            "name": "Data Structures and Algorithms",
            "issuer": "Udemy",
            "image": "https://via.placeholder.com/400x250.png?text=Data+Structures"
        }
    ]
}

# ==========================================
# 2. APP CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="Omolola Lawal | Data Scientist",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    /* Force Deep Blue Global Background */
    .stApp { background-color: #0E0E34 !important; }
    
    /* Hide Streamlit default header and footer */
    header[data-testid="stHeader"] { display: none !important; }
    footer { display: none !important; }
    
    /* Reduce padding on the sides for wider content */
    .block-container {
        padding-top: 2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 1100px !important; 
        margin: 0 auto !important;
    }

    @import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Lora:ital,wght@0,400;0,700;1,400&display=swap');

    /* Global Typography */
    h1, h2, h3, h4, h5, h6 { font-family: 'Julius Sans One', sans-serif !important; text-align: center !important; margin-bottom: 1rem !important; }
    p, span, div, li, a { font-family: 'Lora', serif !important; }
    p, ul { text-align: center !important; }
    ul { list-style-position: inside; padding-left: 0; }
    
    /* =======================================================
       BULLETPROOF ALTERNATING COLOR SYSTEM
       ======================================================= */

    /* 1. OFF-WHITE SECTIONS */
    div[data-testid="stVerticalBlockBorderWrapper"]:has(.theme-offwhite) {
        background-color: #f4f4f5 !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 3rem 2rem !important;
        margin-bottom: 2rem !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:has(.theme-offwhite) * {
        color: #0E0E34 !important; 
    }
    /* Inner cards for Off-White Sections */
    div[data-testid="stVerticalBlockBorderWrapper"]:has(.theme-offwhite) div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        height: 100% !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
    }

    /* 2. BLUE SECTIONS */
    div[data-testid="stVerticalBlockBorderWrapper"]:has(.theme-blue) {
        background-color: #0E0E34 !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 20px !important;
        padding: 3rem 2rem !important;
        margin-bottom: 2rem !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:has(.theme-blue) * {
        color: #ffffff !important;
    }
    /* Inner cards for Blue Sections */
    div[data-testid="stVerticalBlockBorderWrapper"]:has(.theme-blue) div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        height: 100% !important;
    }

    /* Streamlit Link Button Overrides */
    .stLinkButton > a {
        border-radius: 9999px !important;
        font-family: 'Lora', serif !important;
        font-weight: bold !important;
        padding: 0.5rem 1.5rem !important;
        border: none !important;
        transition: opacity 0.3s ease;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:has(.theme-offwhite) .stLinkButton > a {
        background-color: #0E0E34 !important; color: #ffffff !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:has(.theme-blue) .stLinkButton > a {
        background-color: #ffffff !important; color: #0E0E34 !important;
    }

    /* =======================================================
       CUSTOM PILL NAVBAR & DROPDOWN
       ======================================================= */
    .nav-pill {
        background-color: #ffffff;
        color: #0E0E34 !important;
        padding: 0.6rem 1.5rem;
        border-radius: 9999px;
        text-decoration: none;
        font-family: 'Lora', serif !important;
        font-weight: bold;
        font-size: 0.95rem;
        display: inline-block;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: opacity 0.3s;
    }
    .nav-pill:hover { opacity: 0.8; }
    
    .nav-dropdown { position: relative; display: inline-block; }
    .nav-dropdown-content { 
        display: none; position: absolute; background-color: #ffffff; 
        min-width: 140px; box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2); 
        z-index: 999; border-radius: 12px; overflow: hidden; top: 100%; margin-top: 8px; left: 50%; transform: translateX(-50%);
    }
    .nav-dropdown:hover .nav-dropdown-content { display: flex; flex-direction: column; }
    .nav-dropdown-content a { 
        color: #0E0E34 !important; padding: 12px 16px; text-decoration: none; 
        font-family: 'Lora', serif !important; font-weight: bold; text-align: center !important;
    }
    .nav-dropdown-content a:hover { background-color: #f1f1f1; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. HERO & UNIFIED NAVBAR (No Image)
# ==========================================
st.markdown(f"""<div style="text-align: center; padding-bottom: 3rem; color: white;"><div style="font-family: 'Julius Sans One', sans-serif; font-size: 1.6rem; font-weight: bold; color: #ffffff; margin-bottom: 2rem;">My Portfolio</div><div style="display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center; margin-bottom: 4rem;"><a href="#about-me" class="nav-pill">About</a><a href="#technical-skills" class="nav-pill">Skills</a><a href="#experience" class="nav-pill">Experience</a><a href="#projects" class="nav-pill">Projects</a><a href="#certifications" class="nav-pill">Certifications</a><div class="nav-dropdown"><div class="nav-pill" style="cursor: pointer;">Connect ▾</div><div class="nav-dropdown-content"><a href="{PORTFOLIO_DATA['contact']['linkedin']}" target="_blank">LinkedIn</a><a href="mailto:{PORTFOLIO_DATA['email']}">Email</a></div></div></div><h1 id="about-me" style="font-family: 'Julius Sans One', sans-serif; font-size: 4rem; margin-bottom: 2rem; line-height: 1.2; color: white !important;">{PORTFOLIO_DATA['name']}<br>{PORTFOLIO_DATA['role']}</h1><p style="font-family: 'Lora', serif; font-size: 1.15rem; max-width: 800px; margin: 0 auto; line-height: 1.8; color: #e0e0e0 !important;">{PORTFOLIO_DATA['about']}</p></div>""", unsafe_allow_html=True)

# ==========================================
# 4. MAIN CONTENT (Alternating Colors)
# ==========================================

# --- Section 1: Technical Skills (OFF-WHITE) ---
# Shrunk to a compact, responsive cluster of inline badges instead of massive borders
with st.container(border=True):
    st.markdown('<div class="theme-offwhite"></div>', unsafe_allow_html=True)
    st.markdown("<h2 id='technical-skills'>Technical Skills</h2>", unsafe_allow_html=True)
    
    skills_html = '<div style="display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; margin-top: 1.5rem;">'
    for skill in PORTFOLIO_DATA["skills"]:
        skills_html += f'<span style="background-color: #0E0E34; color: #ffffff !important; padding: 10px 20px; border-radius: 9999px; font-family: \'Lora\', serif; font-weight: bold; font-size: 0.95rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">{skill}</span>'
    skills_html += '</div>'
    st.markdown(skills_html, unsafe_allow_html=True)

# --- Section 2: Experience (BLUE) ---
with st.container(border=True):
    st.markdown('<div class="theme-blue"></div>', unsafe_allow_html=True)
    st.markdown("<h2 id='experience'>Experience</h2>", unsafe_allow_html=True)
    for job in PORTFOLIO_DATA["experience"]:
        with st.container(border=True):
            st.markdown(f"### {job['title']}")
            st.markdown(f"**{job['company']}** | *{job['date']}*")
            for point in job["points"]:
                st.write(f"● {point}")

# --- Section 3: Projects (OFF-WHITE) ---
with st.container(border=True):
    st.markdown('<div class="theme-offwhite"></div>', unsafe_allow_html=True)
    st.markdown("<h2 id='projects'>Projects</h2>", unsafe_allow_html=True)
    proj_cols = st.columns(2)
    for i, project in enumerate(PORTFOLIO_DATA["projects"]):
        with proj_cols[i % 2]:
            with st.container(border=True):
                st.image(project["image"], use_container_width=True)
                st.markdown(f"### {project['name']}")
                st.write(project["desc"])
                st.link_button("View on GitHub", project["link"], use_container_width=True)

# --- Section 4: Certifications (BLUE) ---
with st.container(border=True):
    st.markdown('<div class="theme-blue"></div>', unsafe_allow_html=True)
    st.markdown("<h2 id='certifications'>Certifications</h2>", unsafe_allow_html=True)
    cert_cols = st.columns(3)
    for i, cert in enumerate(PORTFOLIO_DATA["certifications"]):
        with cert_cols[i % 3]:
            with st.container(border=True):
                st.image(cert["image"], use_container_width=True)
                st.markdown(f"### {cert['name']}")
                st.write(f"Issuer: {cert['issuer']}")