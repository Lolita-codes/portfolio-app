import streamlit as st

# ==========================================
# 1. PORTFOLIO DATA
# ==========================================
PORTFOLIO_DATA = {
    "name": "Omolola Blessing Lawal",
    "role": "Data Scientist",
    "profile_image_url": "https://sitefile.co/6772c19a0931ea2de588b066/1735826699400_unnamed2.jpg",
    "email": "your.email@example.com", 
    "about": """
Hi there! I am a Data Scientist with proven ability in analyzing complex datasets to identify trends, develop models and provide actionable insights that guides strategic development of secure and advanced initiatives.

My experience spans data cleaning and transformation, data analysis and visualization, AI and machine learning solutions, web scraping and script automation. 

I am committed to innovation and collaboration and I believe we can make something remarkable together so let’s connect and make a difference through technology and data!
    """,
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
# 2. APP CONFIGURATION & CSS
# ==========================================
st.set_page_config(
    page_title="Omolola Lawal | Data Scientist",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS targeting Vzy template styles
st.markdown("""
    <style>
    /* --- 1. Global App Background and Fonts --- */
    .stApp {
        background-color: #ffffff;
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Lora:ital,wght@0,400;0,700;1,400&display=swap');

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Julius Sans One', sans-serif !important;
        text-align: center !important;
        margin-bottom: 1rem !important;
    }

    /* Smaller Texts */
    p, span, div, li, a {
        font-family: 'Lora', serif;
    }
    
    p, ul {
        text-align: center !important;
    }
    ul {
        list-style-position: inside;
        padding-left: 0;
    }
    
    /* Hide Streamlit default header and footer */
    header[data-testid="stHeader"] {display: none;}
    footer {display: none;}
    
    /* --- 2. Main Content Layout --- */
    .block-container {
        padding-top: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 1100px !important;
        margin: 0 auto !important;
    }

    /* --- 3. The Breakout Trick for Main Sections --- */
    .block-container > div > div > div[data-testid="stVerticalBlockBorderWrapper"] {
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
        border: none !important;
        border-radius: 0 !important;
        padding: 6rem 10% !important;
    }

    /* --- 4. Section Background Colors (Mimicking Vzy Layout) --- */
    /* 1: Skills (Grey) */
    .block-container > div > div > div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(1) { background-color: #f7f7f8 !important; }
    /* 2: Experience (Accent #0E0E34) */
    .block-container > div > div > div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(2) { background-color: #0E0E34 !important; }
    /* 3: Projects (Grey) */
    .block-container > div > div > div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(3) { background-color: #f7f7f8 !important; }
    /* 4: Education (Accent #0E0E34) */
    .block-container > div > div > div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(4) { background-color: #0E0E34 !important; }
    /* 5: Contact (Accent #0E0E34) */
    .block-container > div > div > div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(5) { background-color: #0E0E34 !important; border-top: 1px solid rgba(255,255,255,0.05) !important;}
    /* 6: Certifications (White) */
    .block-container > div > div > div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(6) { background-color: #ffffff !important; }

    /* Fix Header Colors based on Section Background */
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(1) h2,
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(3) h2,
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(6) h2 { color: #0E0E34 !important; font-weight: bold !important; }
    
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(2) h2,
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(4) h2,
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(5) h2 { color: #ffffff !important; font-weight: bold !important; }

    /* --- 5. Nested Cards (.min-shape from Vzy) --- */
    div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stVerticalBlockBorderWrapper"] {
        width: 100% !important;
        position: relative !important;
        left: auto !important;
        right: auto !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
        border-radius: 24px !important; /* Vzy soft rounded cards */
        padding: 2.5rem 2rem !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        text-align: center;
        height: 100%;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-5px);
    }
    
    /* Light Cards (Skills, Projects, Certs) */
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(1) div[data-testid="stVerticalBlockBorderWrapper"],
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(3) div[data-testid="stVerticalBlockBorderWrapper"],
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(6) div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important;
        border: 1px solid #eaeaea !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03) !important;
        color: #333333 !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(1) h3,
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(3) h3,
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(6) h3 { color: #0E0E34 !important; font-weight: bold !important; }

    /* Dark/Glass Cards (Experience, Education, Contact) */
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(2) div[data-testid="stVerticalBlockBorderWrapper"],
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(4) div[data-testid="stVerticalBlockBorderWrapper"],
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(5) div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        color: #ffffff !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(2) h3,
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(4) h3,
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(5) h3 { color: #ffffff !important; }
    
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(2) p,
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(4) p,
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(5) p { color: #e0e0e0 !important; }

    /* --- 6. Pill-Shaped Link Buttons --- */
    .stLinkButton > a {
        border-radius: 9999px !important;
        font-family: 'Lora', serif !important;
        font-weight: bold !important;
        padding: 0.5rem 1.5rem !important;
        transition: opacity 0.3s ease;
    }
    .stLinkButton > a:hover { opacity: 0.8; }
    
    /* Buttons in Light Sections */
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(3) .stLinkButton > a,
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(6) .stLinkButton > a {
        background-color: #0E0E34 !important;
        color: #ffffff !important;
        border: none !important;
    }
    
    /* Buttons in Dark Sections */
    div[data-testid="stVerticalBlockBorderWrapper"]:nth-of-type(5) .stLinkButton > a {
        background-color: #ffffff !important;
        color: #0E0E34 !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. HTML NAVBAR & HERO SECTION
# ==========================================
st.markdown(f"""
    <div style="background-color: #0E0E34; color: white; padding: 3rem 10% 6rem 10%; text-align: center; width: 100vw; position: relative; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw;">
        <!-- Navbar -->
        <div style="display: flex; justify-content: space-between; align-items: center; max-width: 1100px; margin: 0 auto; padding-bottom: 5rem;">
            <div style="font-family: 'Julius Sans One', sans-serif; font-size: 1.5rem; font-weight: bold; color: #ffffff;">My Portfolio</div>
            <div style="display: flex; gap: 1rem;">
                <a href="{PORTFOLIO_DATA['contact']['linkedin']}" target="_blank" style="background-color: #ffffff; color: #0E0E34; padding: 0.6rem 1.5rem; border-radius: 9999px; text-decoration: none; font-family: 'Lora', serif; font-weight: bold; font-size: 0.95rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">LinkedIn</a>
                <a href="mailto:{PORTFOLIO_DATA['email']}" style="background-color: #ffffff; color: #0E0E34; padding: 0.6rem 1.5rem; border-radius: 9999px; text-decoration: none; font-family: 'Lora', serif; font-weight: bold; font-size: 0.95rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">Email</a>
            </div>
        </div>

        <!-- Hero Content -->
        <h1 style="font-family: 'Julius Sans One', sans-serif; font-size: 4rem; margin-bottom: 2rem; color: white !important; line-height: 1.2;">{PORTFOLIO_DATA['name']}<br>{PORTFOLIO_DATA['role']}</h1>
        
        <div style="display: flex; justify-content: center; margin-bottom: 3rem;">
            <img src="{PORTFOLIO_DATA['profile_image_url']}" style="width: 100%; max-width: 800px; height: 450px; object-fit: cover; border-radius: 32px; box-shadow: 0 20px 40px rgba(0,0,0,0.3);">
        </div>
        
        <p style="font-family: 'Lora', serif; font-size: 1.25rem; max-width: 800px; margin: 0 auto; line-height: 1.8; color: #e0e0e0 !important;">
            {PORTFOLIO_DATA['about']}
        </p>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 4. MAIN CONTENT
# ==========================================

# --- Section 1: Technical Skills (Grey) ---
with st.container(border=True):
    st.markdown("<h2>Technical Skills</h2>", unsafe_allow_html=True)
    
    skills = PORTFOLIO_DATA["skills"]
    # Iterate through skills and display them in a 3-column masonry-style grid
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

# --- Section 2: Experience (Dark) ---
with st.container(border=True):
    st.markdown("<h2>Experience</h2>", unsafe_allow_html=True)
    for job in PORTFOLIO_DATA["experience"]:
        with st.container(border=True):
            st.markdown(f"### {job['title']}")
            st.markdown(f"**{job['company']}** | *{job['date']}*")
            for point in job["points"]:
                st.write(f"● {point}")

# --- Section 3: Projects (Grey) ---
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

# --- Section 4: Education (Dark) ---
with st.container(border=True):
    st.markdown("<h2>Education</h2>", unsafe_allow_html=True)
    for edu in PORTFOLIO_DATA["education"]:
        with st.container(border=True):
            st.markdown(f"### {edu['school']}")
            st.write(f"**{edu['degree']}**")
            st.write(edu["details"])

# --- Section 5: Contact (Dark) ---
with st.container(border=True):
    st.markdown("<h2>Contact</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    with c1:
        with st.container(border=True):
            st.markdown("### Email")
            st.link_button("Send an Email", f"mailto:{PORTFOLIO_DATA['email']}", use_container_width=True)
    with c2:
        with st.container(border=True):
            st.markdown("### LinkedIn")
            st.link_button("View Profile", PORTFOLIO_DATA['contact']['linkedin'], use_container_width=True)
    with c3:
        with st.container(border=True):
            st.markdown("### GitHub")
            st.link_button("View Repos", PORTFOLIO_DATA['contact']['github'], use_container_width=True)

# --- Section 6: Certifications (White) ---
with st.container(border=True):
    st.markdown("<h2>Certifications</h2>", unsafe_allow_html=True)
    cert_cols = st.columns(3)
    for i, cert in enumerate(PORTFOLIO_DATA["certifications"]):
        with cert_cols[i % 3]:
            with st.container(border=True):
                st.image(cert["image"], use_container_width=True)
                st.markdown(f"### {cert['name']}")
                st.write(f"Issuer: {cert['issuer']}")
                