import streamlit as st

# ==========================================
# 1. PORTFOLIO DATA
# ==========================================
PORTFOLIO_DATA = {
    "name": "Omolola Blessing Lawal",
    "role": "Data Scientist",
    "profile_image_url": "https://sitefile.co/6772c19a0931ea2de588b066/1735826699400_unnamed2.jpg",
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
    "education": [
        {
            "degree": "MSc in Community Health Sciences",
            "school": "University of Manitoba, Canada",
            "details": "Starting Fall 2026 | Research focus under Dr. Amani Hamad"
        },
        {
            "degree": "Bachelor of Pharmacy",
            "school": "Obafemi Awolowo University, Nigeria",
            "details": "CGPA 4.72/5.00 — Best Graduating Student, Faculty of Pharmacy '23"
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

# Bulletproof Alternating Color Theme CSS
st.markdown("""
    <style>
    /* Force Deep Blue Global Background */
    .stApp { background-color: #0E0E34 !important; }
    
    /* Hide Streamlit default header and footer */
    header[data-testid="stHeader"] { display: none !important; }
    footer { display: none !important; }
    
    /* Reduced padding on the sides and wider max-width */
    .block-container {
        padding-top: 2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 1250px !important; 
        margin: 0 auto !important;
    }

    /* Typography Imports */
    @import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Lora:ital,wght@0,400;0,700;1,400&display=swap');

    /* Global Typography Defaults */
    h1, h2, h3, h4, h5, h6 { font-family: 'Julius Sans One', sans-serif !important; text-align: center !important; margin-bottom: 1rem !important; }
    p, span, div, li, a { font-family: 'Lora', serif !important; }
    p, ul { text-align: center !important; }
    ul { list-style-position: inside; padding-left: 0; }
    
    /* Pill-Shaped Link Buttons Base Style */
    .stLinkButton > a {
        border-radius: 9999px !important;
        font-family: 'Lora', serif !important;
        font-weight: bold !important;
        padding: 0.5rem 1.5rem !important;
        border: none !important;
        transition: opacity 0.3s ease;
    }
    .stLinkButton > a:hover { opacity: 0.8 !important; }

    /* =======================================================
       THE BULLETPROOF ALTERNATING THEME SYSTEM (Using :has)
       ======================================================= */

    /* 1. LIGHT SECTIONS (White Background, Dark Blue Text) */
    div[data-testid="element-container"]:has(.theme-light) + div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 3rem 2rem !important;
        margin-bottom: 2rem !important;
    }
    div[data-testid="element-container"]:has(.theme-light) + div[data-testid="stVerticalBlockBorderWrapper"] * {
        color: #0E0E34 !important;
    }
    /* Inner cards for Light Sections */
    div[data-testid="element-container"]:has(.theme-light) + div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #f8f9fa !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        height: 100% !important;
        transition: transform 0.2s ease;
    }
    div[data-testid="element-container"]:has(.theme-light) + div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
    }
    /* Button colors for Light Sections */
    div[data-testid="element-container"]:has(.theme-light) + div[data-testid="stVerticalBlockBorderWrapper"] .stLinkButton > a {
        background-color: #0E0E34 !important; color: #ffffff !important;
    }

    /* 2. DARK GRAY SECTIONS (Dark Gray Background, White Text) */
    div[data-testid="element-container"]:has(.theme-dark) + div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #1a1a1a !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 3rem 2rem !important;
        margin-bottom: 2rem !important;
    }
    div[data-testid="element-container"]:has(.theme-dark) + div[data-testid="stVerticalBlockBorderWrapper"] * {
        color: #ffffff !important;
    }
    /* Inner cards for Dark Gray Sections */
    div[data-testid="element-container"]:has(.theme-dark) + div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #2a2a2a !important;
        border: 1px solid #333333 !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        height: 100% !important;
        transition: transform 0.2s ease;
    }
    div[data-testid="element-container"]:has(.theme-dark) + div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
    }
    /* Button colors for Dark Sections */
    div[data-testid="element-container"]:has(.theme-dark) + div[data-testid="stVerticalBlockBorderWrapper"] .stLinkButton > a {
        background-color: #ffffff !important; color: #0E0E34 !important;
    }
    
    /* Navbar styling for HTML section */
    .nav-link {
        color: #E6B5E8; text-decoration: none; font-family: 'Julius Sans One', sans-serif !important; font-weight: bold; font-size: 1rem; transition: color 0.3s;
    }
    .nav-link:hover { color: #ffffff; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. HTML HERO SECTION & FULL NAVBAR
# ==========================================
# Cleaned up HTML, keeping it as one line to avoid Streamlit Markdown errors
st.markdown(f"""<div style="text-align: center; padding-bottom: 3rem; color: white;"><div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem; flex-wrap: wrap; gap: 1rem;"><div style="font-family: 'Julius Sans One', sans-serif; font-size: 1.6rem; font-weight: bold; color: #ffffff;">My Portfolio</div><div style="display: flex; gap: 1.5rem; align-items: center; flex-wrap: wrap;"><a href="#about-me" target="_self" class="nav-link">About</a><a href="#technical-skills" target="_self" class="nav-link">Skills</a><a href="#experience" target="_self" class="nav-link">Experience</a><a href="#projects" target="_self" class="nav-link">Projects</a><a href="#certifications" target="_self" class="nav-link">Certifications</a><a href="{PORTFOLIO_DATA['contact']['linkedin']}" target="_blank" style="background-color: #ffffff; color: #0E0E34; padding: 0.5rem 1.2rem; border-radius: 9999px; text-decoration: none; font-family: 'Lora', serif; font-weight: bold; font-size: 0.95rem;">LinkedIn</a><a href="mailto:{PORTFOLIO_DATA['email']}" style="background-color: #ffffff; color: #0E0E34; padding: 0.5rem 1.2rem; border-radius: 9999px; text-decoration: none; font-family: 'Lora', serif; font-weight: bold; font-size: 0.95rem;">Email</a></div></div><h1 id="about-me" style="font-family: 'Julius Sans One', sans-serif; font-size: 3.8rem; margin-bottom: 2rem; line-height: 1.2; color: white !important;">{PORTFOLIO_DATA['name']}<br>{PORTFOLIO_DATA['role']}</h1><div style="display: flex; justify-content: center; margin-bottom: 2rem;"><img src="{PORTFOLIO_DATA['profile_image_url']}" style="width: 100%; max-width: 600px; height: 350px; object-fit: cover; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);"></div><p style="font-family: 'Lora', serif; font-size: 1.15rem; max-width: 800px; margin: 0 auto; line-height: 1.8; color: #e0e0e0 !important;">{PORTFOLIO_DATA['about']}</p></div>""", unsafe_allow_html=True)

# ==========================================
# 4. MAIN CONTENT
# ==========================================

# --- Section 1: Technical Skills (WHITE) ---
st.markdown('<div class="theme-light" style="display: none;"></div>', unsafe_allow_html=True)
with st.container(border=True):
    st.markdown("<h2 id='technical-skills'>Technical Skills</h2>", unsafe_allow_html=True)
    skills = PORTFOLIO_DATA["skills"]
    for i in range(0, len(skills), 3):
        cols = st.columns(3)
        with cols[0]:
            if i < len(skills):
                with st.container(border=True): st.markdown(f"### {skills[i]}")
        with cols[1]:
            if i+1 < len(skills):
                with st.container(border=True): st.markdown(f"### {skills[i+1]}")
        with cols[2]:
            if i+2 < len(skills):
                with st.container(border=True): st.markdown(f"### {skills[i+2]}")

# --- Section 2: Experience (DARK GRAY) ---
st.markdown('<div class="theme-dark" style="display: none;"></div>', unsafe_allow_html=True)
with st.container(border=True):
    st.markdown("<h2 id='experience'>Experience</h2>", unsafe_allow_html=True)
    for job in PORTFOLIO_DATA["experience"]:
        with st.container(border=True):
            st.markdown(f"### {job['title']}")
            st.markdown(f"**{job['company']}** | *{job['date']}*")
            for point in job["points"]:
                st.write(f"● {point}")

# --- Section 3: Projects (WHITE) ---
st.markdown('<div class="theme-light" style="display: none;"></div>', unsafe_allow_html=True)
with st.container(border=True):
    st.markdown("<h2 id='projects'>Projects</h2>", unsafe_allow_html=True)
    proj_cols = st.columns(2)
    for i, project in enumerate(PORTFOLIO_DATA["projects"]):
        with proj_cols[i % 2]:
            with st.container(border=True):
                st.image(project["image"], use_container_width=True)
                st.markdown(f"### {project['name']}")
                st.write(project["desc"])
                st.link_button("View on GitHub", project["link"], use_container_width=True)

# --- Section 4: Education (DARK GRAY) ---
st.markdown('<div class="theme-dark" style="display: none;"></div>', unsafe_allow_html=True)
with st.container(border=True):
    st.markdown("<h2>Education</h2>", unsafe_allow_html=True)
    for edu in PORTFOLIO_DATA["education"]:
        with st.container(border=True):
            st.markdown(f"### {edu['school']}")
            st.write(f"**{edu['degree']}**")
            st.write(edu["details"])

# --- Section 5: Certifications (WHITE) ---
st.markdown('<div class="theme-light" style="display: none;"></div>', unsafe_allow_html=True)
with st.container(border=True):
    st.markdown("<h2 id='certifications'>Certifications</h2>", unsafe_allow_html=True)
    cert_cols = st.columns(3)
    for i, cert in enumerate(PORTFOLIO_DATA["certifications"]):
        with cert_cols[i % 3]:
            with st.container(border=True):
                st.image(cert["image"], use_container_width=True)
                st.markdown(f"### {cert['name']}")
                st.write(f"Issuer: {cert['issuer']}")