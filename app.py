import streamlit as st

# ==========================================
# 1. PORTFOLIO DATA 
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
        {"name": "Profitability Analysis", "desc": "Analyzes food order data to uncover insights regarding profitability, delivery efficiency, and payment methods.", "link": "https://github.com/Lolita-codes/delivery_orders_profitability", "image": "https://via.placeholder.com/600x350.png?text=Profitability+Analysis"},
        {"name": "HR Churn Analysis", "desc": "Analyzes employee attrition trends to identify factors contributing to turnover and predict outcomes.", "link": "https://github.com/Lolita-codes/hr_data_analysis", "image": "https://via.placeholder.com/600x350.png?text=HR+Churn+Analysis"},
        {"name": "Customer Segmentation", "desc": "Segments customers based on standard FICO credit scores derived from multiple financial factors.", "link": "https://github.com/Lolita-codes/credit_score_customer_segmentation", "image": "https://via.placeholder.com/600x350.png?text=Customer+Segmentation"},
        {"name": "User Segmentation", "desc": "Segments users based on demographic and behavioral features to optimize ad targeting strategies.", "link": "https://github.com/Lolita-codes/user_segmentation", "image": "https://via.placeholder.com/600x350.png?text=User+Segmentation"},
        {"name": "House Price Prediction", "desc": "Builds a predictive model that estimates house prices based on various property characteristics.", "link": "https://github.com/Lolita-codes/Price_prediction", "image": "https://via.placeholder.com/600x350.png?text=House+Price+Prediction"},
        {"name": "Playstore Analysis", "desc": "Provides comprehensive insights into the Android app market, from app ratings to category competitiveness.", "link": "https://github.com/Lolita-codes/Google_Playstore_Apps", "image": "https://via.placeholder.com/600x350.png?text=Playstore+Analysis"},
        {"name": "US Police Shootings", "desc": "A comprehensive understanding of social trends and the factors contributing to fatal police use of force in the US.", "link": "https://github.com/Lolita-codes/US_police_shootings", "image": "https://via.placeholder.com/600x350.png?text=Police+Shootings"},
        {"name": "Flight Deal Finder", "desc": "Tracks locations and integrates with a flight search API to identify deals below a price threshold.", "link": "https://github.com/Lolita-codes/Flight_deal_finder", "image": "https://via.placeholder.com/600x350.png?text=Flight+Deals"},
        {"name": "Sentiment Analysis", "desc": "Identifies key sentiment trends and categorizes opinions regarding a vaccine across demographics.", "link": "https://github.com/Lolita-codes/Sentiment_analysis_Pfizer_vaccine", "image": "https://via.placeholder.com/600x350.png?text=Sentiment+Analysis"},
        {"name": "Price Optimization", "desc": "Predicts total price to maximize revenue considering category, freight, competitors, and attributes.", "link": "https://github.com/Lolita-codes/price_optimization", "image": "https://via.placeholder.com/600x350.png?text=Price+Optimization"}
    ],
    "certifications": [
        {"name": "The Data Science Course: Complete Bootcamp", "issuer": "Udemy", "image": "https://via.placeholder.com/400x250.png?text=Data+Science+Bootcamp"},
        {"name": "FastAPI – The Complete Course", "issuer": "Udemy", "image": "https://via.placeholder.com/400x250.png?text=FastAPI+Course"},
        {"name": "Python Django – The Practical Guide", "issuer": "Udemy", "image": "https://via.placeholder.com/400x250.png?text=Django+Guide"},
        {"name": "100 Days of Code: Python Pro", "issuer": "Udemy", "image": "https://via.placeholder.com/400x250.png?text=Python+100+Days"},
        {"name": "Data Structures and Algorithms", "issuer": "Udemy", "image": "https://via.placeholder.com/400x250.png?text=Data+Structures"}
    ]
}

# ==========================================
# 2. CONFIGURATION & CORE CSS
# ==========================================
st.set_page_config(page_title="Omolola Lawal | Data Scientist", layout="wide", initial_sidebar_state="collapsed")

# We turn Streamlit into a blank edge-to-edge canvas
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Lora:ital,wght@0,400;0,700;1,400&display=swap');

/* Reset Streamlit defaults */
.stApp { background-color: #0E0E34 !important; }
header[data-testid="stHeader"], footer { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* Section Containers - Controls alternating backgrounds and padding */
.section-blue { background-color: #0E0E34; color: white; padding: 5rem 2rem; }
.section-offwhite { background-color: #f7f7f8; color: #111111; padding: 5rem 2rem; }
.content-wrapper { max-width: 1200px; margin: 0 auto; }

/* Grid Layouts - Forces exactly 3 columns */
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
@media (max-width: 900px) { .grid-3 { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 600px) { .grid-3 { grid-template-columns: 1fr; } }

/* Cards */
.card-light { background: white; border: 1px solid #e0e0e0; border-radius: 16px; padding: 2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05); display: flex; flex-direction: column; transition: transform 0.2s; }
.card-light:hover { transform: translateY(-4px); box-shadow: 0 8px 16px rgba(0,0,0,0.1); }
.card-dark { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 2.5rem; display: flex; flex-direction: column; transition: transform 0.2s; }
.card-dark:hover { transform: translateY(-4px); border-color: rgba(255,255,255,0.3); }

/* Typography */
h1, h2, h3 { font-family: 'Julius Sans One', sans-serif; }
p, li, span { font-family: 'Lora', serif; }
.section-title { text-align: center; font-size: 2.5rem; margin-top: 0; margin-bottom: 3rem; }

/* Buttons */
.btn-blue { background-color: #0E0E34; color: white !important; text-decoration: none; padding: 0.8rem 1.5rem; border-radius: 9999px; text-align: center; font-family: 'Lora', serif; font-weight: bold; margin-top: 1.5rem; }
.btn-blue:hover { opacity: 0.8; }

/* Nav Bar & Dropdown */
.nav-pill { color: white !important; text-decoration: none; padding: 0.6rem 1.2rem; border-radius: 9999px; font-family: 'Lora', serif; font-weight: bold; font-size: 1rem; transition: background 0.3s; cursor: pointer; }
.nav-pill:hover { background-color: rgba(255,255,255,0.1); }
.nav-dropdown { position: relative; display: inline-block; }
.nav-dropdown-content { display: none; position: absolute; background-color: white; min-width: 150px; box-shadow: 0 8px 16px rgba(0,0,0,0.2); z-index: 999; border-radius: 12px; top: 100%; right: 0; overflow: hidden; margin-top: 5px; }
.nav-dropdown:hover .nav-dropdown-content { display: flex; flex-direction: column; }
.nav-dropdown-content a { color: #0E0E34 !important; padding: 12px 16px; text-decoration: none; font-family: 'Lora', serif; font-weight: bold; text-align: center; }
.nav-dropdown-content a:hover { background-color: #f1f1f1; }
</style>
"""

# ==========================================
# 3. HTML GENERATION LOGIC
# ==========================================

# --- Nav & Hero ---
hero_html = f"""
<div class="section-blue" style="padding-top: 2rem;">
    <div class="content-wrapper">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5rem; flex-wrap: wrap; gap: 1rem;">
            <div style="font-family: 'Julius Sans One', sans-serif; font-size: 1.8rem; font-weight: bold; color: white;">My Portfolio</div>
            <div style="display: flex; gap: 0.2rem; align-items: center; flex-wrap: wrap;">
                <a href="#about-me" class="nav-pill">About</a>
                <a href="#technical-skills" class="nav-pill">Skills</a>
                <a href="#experience" class="nav-pill">Experience</a>
                <a href="#projects" class="nav-pill">Projects</a>
                <a href="#certifications" class="nav-pill">Certifications</a>
                <div class="nav-dropdown">
                    <div class="nav-pill">Connect ▾</div>
                    <div class="nav-dropdown-content">
                        <a href="{PORTFOLIO_DATA['contact']['linkedin']}" target="_blank">LinkedIn</a>
                        <a href="mailto:{PORTFOLIO_DATA['email']}">Email</a>
                    </div>
                </div>
            </div>
        </div>
        <div id="about-me" style="text-align: center; padding-bottom: 4rem;">
            <h1 style="font-size: 4.5rem; margin-top: 0; margin-bottom: 2rem; line-height: 1.2;">{PORTFOLIO_DATA['name']}<br>{PORTFOLIO_DATA['role']}</h1>
            <p style="font-size: 1.15rem; max-width: 800px; margin: 0 auto; line-height: 1.8; color: #e0e0e0;">{PORTFOLIO_DATA['about']}</p>
        </div>
    </div>
</div>
"""

# --- Skills ---
skills_html = '<div class="section-offwhite" id="technical-skills"><div class="content-wrapper"><h2 class="section-title">Technical Skills</h2><div class="grid-3">'
for skill in PORTFOLIO_DATA["skills"]:
    skills_html += f'<div class="card-light"><h3 style="margin:0; text-align:center;">{skill}</h3></div>'
skills_html += '</div></div></div>'

# --- Experience ---
exp_html = '<div class="section-blue" id="experience"><div class="content-wrapper"><h2 class="section-title">Experience</h2><div style="display: flex; flex-direction: column; gap: 1.5rem;">'
for job in PORTFOLIO_DATA["experience"]:
    points = "".join([f"<li style='text-align: justify; margin-bottom: 0.8rem; line-height: 1.6;'>{p}</li>" for p in job["points"]])
    exp_html += f"""
    <div class="card-dark" style="color: white;">
        <h2 style="margin-top: 0; margin-bottom: 0.5rem; text-align: left;">{job['title']}</h2>
        <h3 style="color: #E6B5E8; margin-bottom: 1.5rem; font-family: 'Lora', serif; text-align: left; font-size: 1.2rem;">{job['company']} <span style="color: #cccccc; font-weight: normal;">| <em>{job['date']}</em></span></h3>
        <ul style="padding-left: 1.5rem; margin: 0;">{points}</ul>
    </div>
    """
exp_html += '</div></div></div>'

# --- Projects ---
proj_html = '<div class="section-offwhite" id="projects"><div class="content-wrapper"><h2 class="section-title">Projects</h2><div class="grid-3">'
for p in PORTFOLIO_DATA["projects"]:
    proj_html += f"""
    <div class="card-light">
        <img src="{p['image']}" style="width: 100%; border-radius: 8px; margin-bottom: 1.5rem;">
        <h2 style="margin-top: 0; text-align: center; font-size: 1.5rem;">{p['name']}</h2>
        <p style="text-align: center; flex-grow: 1; line-height: 1.6;">{p['desc']}</p>
        <a href="{p['link']}" target="_blank" class="btn-blue">View on GitHub</a>
    </div>
    """
proj_html += '</div></div></div>'

# --- Certifications ---
cert_html = '<div class="section-blue" id="certifications"><div class="content-wrapper"><h2 class="section-title">Certifications</h2><div class="grid-3">'
for c in PORTFOLIO_DATA["certifications"]:
    cert_html += f"""
    <div class="card-dark" style="text-align: center; color: white;">
        <img src="{c['image']}" style="width: 100%; border-radius: 8px; margin-bottom: 1.5rem;">
        <h2 style="margin-top: 0; font-size: 1.3rem;">{c['name']}</h2>
        <p style="margin-bottom: 0; color: #cccccc;">Issuer: {c['issuer']}</p>
    </div>
    """
cert_html += '</div></div></div>'

# --- Connect ---
connect_html = f"""
<div class="section-offwhite" id="connect">
    <div class="content-wrapper">
        <h2 class="section-title">Connect</h2>
        <div class="grid-3">
            <div class="card-light" style="align-items: center; justify-content: center; text-align: center; padding: 3rem 2rem;">
                <h2 style="margin-top: 0;">Email</h2>
                <a href="mailto:{PORTFOLIO_DATA['email']}" class="btn-blue" style="width: 100%; max-width: 250px;">Send an Email</a>
            </div>
            <div class="card-light" style="align-items: center; justify-content: center; text-align: center; padding: 3rem 2rem;">
                <h2 style="margin-top: 0;">LinkedIn</h2>
                <a href="{PORTFOLIO_DATA['contact']['linkedin']}" target="_blank" class="btn-blue" style="width: 100%; max-width: 250px;">View Profile</a>
            </div>
            <div class="card-light" style="align-items: center; justify-content: center; text-align: center; padding: 3rem 2rem;">
                <h2 style="margin-top: 0;">GitHub</h2>
                <a href="{PORTFOLIO_DATA['contact']['github']}" target="_blank" class="btn-blue" style="width: 100%; max-width: 250px;">View Repos</a>
            </div>
        </div>
    </div>
</div>
"""

# ==========================================
# 4. RENDER EVERYTHING
# ==========================================
# Combine all the HTML strings and render them securely to the page
full_page = css + hero_html + skills_html + exp_html + proj_html + cert_html + connect_html
st.markdown(full_page, unsafe_allow_html=True)