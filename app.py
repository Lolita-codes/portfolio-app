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

# Unified Dark Theme CSS (No fragile layout hacks)
st.markdown("""
    <style>
    /* Force App Background */
    .stApp { background-color: #0E0E34 !important; }
    
    /* Hide Streamlit default header and footer */
    header[data-testid="stHeader"] { display: none !important; }
    footer { display: none !important; }
    
    /* Layout constraints */
    .block-container {
        padding-top: 2rem !important;
        max-width: 1000px !important;
        margin: 0 auto !important;
    }

    /* Typography Imports */
    @import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Lora:ital,wght@0,400;0,700;1,400&display=swap');

    /* Force all text to be white to guarantee readability */
    h1, h2, h3, h4, h5, h6, p, span, div, li, a {
        color: #ffffff !important;
    }

    /* Apply Fonts */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Julius Sans One', sans-serif !important;
        text-align: center !important;
        margin-bottom: 1rem !important;
    }
    p, span, div, li, a {
        font-family: 'Lora', serif !important;
    }
    
    /* Center align paragraphs and lists */
    p, ul { text-align: center !important; }
    ul { list-style-position: inside; padding-left: 0; }

    /* Elegant Glass Cards for ALL containers */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 20px !important;
        padding: 2rem !important;
        margin-bottom: 1rem !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.4) !important;
    }

    /* Pill-Shaped Link Buttons */
    .stLinkButton > a {
        background-color: #ffffff !important;
        color: #0E0E34 !important;
        border-radius: 9999px !important;
        font-family: 'Lora', serif !important;
        font-weight: bold !important;
        padding: 0.5rem 1.5rem !important;
        border: none !important;
        transition: opacity 0.3s ease;
    }
    .stLinkButton > a:hover { opacity: 0.8 !important; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. HTML HERO SECTION
# ==========================================
# No blank lines inside this multi-line string to prevent Streamlit markdown glitches
st.markdown(f"""<div style="text-align: center; padding-bottom: 3rem;"><div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4rem;"><div style="font-family: 'Julius Sans One', sans-serif; font-size: 1.5rem; font-weight: bold; color: #ffffff;">My Portfolio</div><div style="display: flex; gap: 1rem;"><a href="{PORTFOLIO_DATA['contact']['linkedin']}" target="_blank" style="background-color: #ffffff; color: #0E0E34; padding: 0.6rem 1.5rem; border-radius: 9999px; text-decoration: none; font-family: 'Lora', serif; font-weight: bold; font-size: 0.95rem;">LinkedIn</a><a href="mailto:{PORTFOLIO_DATA['email']}" style="background-color: #ffffff; color: #0E0E34; padding: 0.6rem 1.5rem; border-radius: 9999px; text-decoration: none; font-family: 'Lora', serif; font-weight: bold; font-size: 0.95rem;">Email</a></div></div><h1 style="font-family: 'Julius Sans One', sans-serif; font-size: 3.5rem; margin-bottom: 2rem; line-height: 1.2;">{PORTFOLIO_DATA['name']}<br>{PORTFOLIO_DATA['role']}</h1><div style="display: flex; justify-content: center; margin-bottom: 2rem;"><img src="{PORTFOLIO_DATA['profile_image_url']}" style="width: 100%; max-width: 600px; height: 350px; object-fit: cover; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);"></div><p style="font-family: 'Lora', serif; font-size: 1.1rem; max-width: 800px; margin: 0 auto; line-height: 1.8;">{PORTFOLIO_DATA['about']}</p></div>""", unsafe_allow_html=True)

# ==========================================
# 4. MAIN CONTENT
# ==========================================

# --- Section 1: Technical Skills ---
with st.container(border=True):
    st.markdown("<h2>Technical Skills</h2>", unsafe_allow_html=True)
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

# --- Section 2: Experience ---
with st.container(border=True):
    st.markdown("<h2>Experience</h2>", unsafe_allow_html=True)
    for job in PORTFOLIO_DATA["experience"]:
        with st.container(border=True):
            st.markdown(f"### {job['title']}")
            st.markdown(f"**{job['company']}** | *{job['date']}*")
            for point in job["points"]:
                st.write(f"● {point}")

# --- Section 3: Projects ---
with st.container(border=True):
    st.markdown("<h2>Projects</h2>", unsafe_allow_html=True)
    proj_cols = st.columns(2)
    for i, project in enumerate(PORTFOLIO_DATA["projects"]):
        with proj_cols[i % 2]:
            with st.container(border=True):
                st.image(project["image"], use_container_width=True)
                st.markdown(f"### {project['name']}")
                st.write(project["desc"])
                st.link_button("View on GitHub", project["link"], use_container_width=True)

# --- Section 4: Education ---
with st.container(border=True):
    st.markdown("<h2>Education</h2>", unsafe_allow_html=True)
    for edu in PORTFOLIO_DATA["education"]:
        with st.container(border=True):
            st.markdown(f"### {edu['school']}")
            st.write(f"**{edu['degree']}**")
            st.write(edu["details"])

# --- Section 5: Certifications ---
with st.container(border=True):
    st.markdown("<h2>Certifications</h2>", unsafe_allow_html=True)
    cert_cols = st.columns(3)
    for i, cert in enumerate(PORTFOLIO_DATA["certifications"]):
        with cert_cols[i % 3]:
            with st.container(border=True):
                st.image(cert["image"], use_container_width=True)
                st.markdown(f"### {cert['name']}")
                st.write(f"Issuer: {cert['issuer']}")