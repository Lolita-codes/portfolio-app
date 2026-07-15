import streamlit as st


PORTFOLIO_DATA = {
    "email": "lawalblessing4u@gmail.com",
    "about": """
I am a Data Scientist with proven ability in analyzing complex datasets to identify trends, develop models and provide actionable insights that guides strategic development of secure and advanced initiatives.

My experience spans data cleaning and transformation, data analysis and visualization, AI and machine learning solutions, web scraping and script automation. 

I am committed to innovation and collaboration and I believe we can make something remarkable together so let’s connect and make a difference through technology and data!
    """,
    "contact": {
        "email": "lawalblessing4u@gmail.com",
        "linkedin": "https://www.linkedin.com/in/omolola-lawal-2a9a45188",
        "github": "https://github.com/Lolita-codes"
    },
    # Exactly 15 skills to fit perfectly in a 3x5 column layout
    "skills": [
        "Python", "Scikit-Learn", "Pandas", 
        "Seaborn", "Matplotlib", "Plotly",
        "Numpy", "SQL & PostgreSQL", "Tableau", 
        "Langchain", "NLTK", "SpaCy",
        "BeautifulSoup", "FastAPI", "Git & GitHub"
    ],
    "experience": [
        {
            "title": "Junior Data Scientist",
            "company": "DC Clevertech, Ilorin, Nigeria",
            "date": "Jan 2025 - Present",
            "points": [
                "Built an AI-powered application, leveraging natural language processing and integrating cloud storage and vector database for file storage and RAG data retrieval.",
                "Collaborated with engineering team to understand business objectives and created compelling visualizations to communicate data findings."            ]
        },
        {
            "title": "Data/Informatics Analyst",
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
            "company": "Stacksuit",
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
            "company": "Stacksuit",
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
            "name": "AI Chatbot",
            "desc": "A dynamic PDF-querying web application built that enables real-time document extraction and Retrieval-Augmented Generation (RAG) on user-uploaded files.",
            "link": "https://aichatbot-with-rag.streamlit.app/",
            "image": "images/app.png"
        },
        {
            "name": "AI Interview Assistant",
            "desc": "AI-powered interview platform that conducts structured technical interviews, evaluates candidate responses with question-by-question scoring, and provides detailed performance feedback.",
            "link": "https://ai-interview-assistant-app.streamlit.app/",
            "image": "images/app.png"
        },
        {
            "name": "AI Interview Assistant",
            "desc": "A predictive model app that can estimate house prices based on various property characteristics.",
            "link": "https://priceprediction-app.streamlit.app/",
            "image": "images/app.png"
        },
        {
            "name": "Profitability Analysis",
            "desc": "Analyzes food order data to uncover insights regarding profitability, delivery efficiency, and payment methods.",
            "link": "https://github.com/Lolita-codes/delivery_orders_profitability",
            "image": "images/orders.png"  
      },
        {
            "name": "HR Churn Analysis",
            "desc": "Analyzes employee attrition trends to identify factors contributing to turnover and predict outcomes.",
            "link": "https://github.com/Lolita-codes/hr_data_analysis",
            "image": "images/hr_data.png"
        },
        {
            "name": "Customer Segmentation",
            "desc": "Segments customers based on standard FICO credit scores derived from multiple financial factors.",
            "link": "https://github.com/Lolita-codes/credit_score_customer_segmentation",
            "image": "images/github.png"
        },
        {
            "name": "User Segmentation",
            "desc": "Segments users based on demographic and behavioral features to optimize ad targeting strategies.",
            "link": "https://github.com/Lolita-codes/user_segmentation",
            "image": "images/github.png"
        },
        {
            "name": "House Price Prediction",
            "desc": "Builds a predictive model that estimates house prices based on various property characteristics.",
            "link": "https://github.com/Lolita-codes/Price_prediction",
            "image": "images/github.png"
        },
        {
            "name": "Google Playstore Analysis",
            "desc": "Provides comprehensive insights into the Android app market, from app ratings to category competitiveness.",
            "link": "https://github.com/Lolita-codes/Google_Playstore_Apps",
            "image": "images/github.png"
        },
    ],

    "certifications": [
        {
            "name": "The Data Science Course: Complete Data Science Bootcamp",
            "issuer": "Udemy",
            "image": "https://via.placeholder.com/400x250.png?text=Data+Science+Bootcamp" # Replace with your certificate image paths
        },
        {
            "name": "FastAPI – The Complete Course (Beginner+Advanced)",
            "issuer": "Udemy",
            "image": "https://via.placeholder.com/400x250.png?text=FastAPI+Course"
        },
        {
            "name": "Python Django – The Practical Guide",
            "issuer": "Udemy",
            "image": "https://via.placeholder.com/400x250.png?text=Django+Guide"
        },
        {
            "name": "100 Days of Code: The Python Pro Bootcamp",
            "issuer": "Udemy",
            "image": "https://via.placeholder.com/400x250.png?text=Python+100+Days"
        },
        {
            "name": "Python - Data Structures and Algorithms",
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

# Custom CSS for Fonts, Alternating Backgrounds, and Cards
st.markdown("""
    <style>
    /* --- 1. Global App Background and Fonts --- */
    .stApp {
        background-color: #0E0E34;
        color: #e0e0e0;
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Julius+Sans+One&family=Lora:ital,wght@0,400;0,700;1,400&display=swap');

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Julius Sans One', sans-serif !important;
        color: #ffffff !important;
        text-align: center !important;
        margin-bottom: 1rem !important;
    }

    /* Smaller Texts */
    p, span, div, li, a {
        font-family: 'Lora', serif;
    }
    
    /* Center align texts globally */
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
        max-width: 1000px !important;
        margin: 0 auto !important;
    }

    /* --- 3. The Breakout Trick for Main Sections --- */
    /* Forces top-level containers to stretch full width of the screen */
    .block-container > div > div > div[data-testid="stVerticalBlockBorderWrapper"] {
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
        border: none !important;
        border-radius: 0 !important;
        padding: 5rem 10% !important;
    }

    /* --- 4. Alternating Full-Width Backgrounds --- */
    /* Even sections: About, Experience, Certs */
    .block-container > div > div:nth-child(even) > div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #1a1a1a !important; /* Dark Gray */
    }
    /* Odd sections: Skills, Projects */
    .block-container > div > div:nth-child(odd) > div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #0E0E34 !important; /* Dark Blue */
    }

    /* --- 5. Nested Cards --- */
    /* Prevents the individual project/experience cards from breaking out, and styles them beautifully */
    div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stVerticalBlockBorderWrapper"] {
        width: 100% !important;
        position: relative !important;
        left: auto !important;
        right: auto !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
        border: 1px solid rgba(230, 181, 232, 0.2) !important;
        border-radius: 12px !important;
        padding: 2rem !important;
        background-color: rgba(255, 255, 255, 0.03) !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    
    /* --- 6. Navbar & Hero Styling --- */
    .hero-container {
        background-color: #0E0E34;
        color: white;
        padding-bottom: 5rem;
        text-align: center;
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
    }
    
    .custom-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 2rem 10%;
        max-width: 1200px;
        margin: 0 auto;
    }
    .nav-left {
        font-family: 'Julius Sans One', sans-serif !important;
        font-weight: 600;
        font-size: 1.3rem;
        color: #E6B5E8 !important; 
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .nav-left span {
        font-family: 'Julius Sans One', sans-serif !important;
    }
    .nav-right {
        display: flex;
        gap: 2.5rem;
        font-size: 0.95rem;
    }
    .nav-right a, .nav-dropdown span {
        font-family: 'Julius Sans One', sans-serif !important;
        color: #E6B5E8 !important;
        text-decoration: none;
        transition: color 0.3s;
    }
    .nav-right a:hover, .nav-dropdown span:hover {
        color: white !important;
    }
    
    /* Dropdown */
    .nav-dropdown {
        position: relative;
        display: inline-block;
        cursor: pointer;
    }
    .nav-dropdown-content {
        display: none;
        position: absolute;
        background-color: #1a1a1a;
        min-width: 120px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.3);
        z-index: 999;
        right: 0;
        border-radius: 4px;
        margin-top: 5px;
    }
    .nav-dropdown:hover .nav-dropdown-content {
        display: block;
    }
    .nav-dropdown-content a {
        padding: 12px 16px;
        display: block;
        text-align: left !important;
    }
    .nav-dropdown-content a:hover {
        background-color: #333;
    }

    /* Hero Content */
    .hero-content {
        padding-top: 3rem;
    }
    .hero-title {
        font-family: 'Dancing Script', cursive !important;
        font-size: 5.5rem !important;
        margin-bottom: 0.5rem;
        color: white !important;
    }
    .hero-subtitle {
        font-family: 'Julius Sans One', sans-serif !important;
        font-size: 1.5rem !important;
        margin-bottom: 1.5rem;
        color: white;
    }
    .resume-link {
        font-family: 'Lora', serif !important;
        color: #E6B5E8 !important;
        text-decoration: none;
        font-size: 1.1rem;
        border-bottom: 1px dashed #E6B5E8;
        transition: color 0.3s;
    }
    .resume-link:hover {
        color: white !important;
        border-bottom: 1px dashed white;
    }
    
    /* Social Icons */
    .social-icons {
        margin-top: 2rem;
        display: flex;
        justify-content: center;
        gap: 1.5rem;
    }
    .social-icons a {
        color: #E6B5E8 !important;
        font-size: 1.2rem;
        text-decoration: none;
    }
    .social-icons a:hover {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. HTML NAVBAR & HERO SECTION
# ==========================================
st.markdown(f"""
    <div class="hero-container">
        <div class="custom-nav">
            <div class="nav-left">Portfolio <span style="font-weight:400; font-size:0.95rem; color:#b5b3c7;"></span></div>
            <div class="nav-right">
                <a href="#about-me">About</a>
                <a href="#technical-skills">Skills</a>
                <a href="#projects">Projects</a>
                <a href="#certifications">Certifications</a>
                <div class="nav-dropdown">
                    <span>Connect ▾</span>
                    <div class="nav-dropdown-content">
                        <a href="{PORTFOLIO_DATA['contact']['linkedin']}" target="_blank">LinkedIn</a>
                        <a href="mailto:{PORTFOLIO_DATA['email']}">Email</a>
                    </div>
                </div>
            </div>
        </div>
        <div class="hero-content">
            <div class="hero-title">Hi, I'm Omolola Lawal</div>
            <div class="hero-subtitle">Data Scientist</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 4. MAIN CONTENT
# ==========================================

# --- About Me (Will be Dark Gray) ---
with st.container(border=True):
    st.markdown("<h2 id='about-me'>About Me</h2>", unsafe_allow_html=True)
    st.write(PORTFOLIO_DATA["about"])

# --- Technical Skills (Will be #0E0E34) ---
with st.container(border=True):
    st.markdown("<h2 id='technical-skills'>Technical Skills</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    skills = PORTFOLIO_DATA["skills"]
    
    for i in range(5):
        col1.markdown(f"- {skills[i]}")
        col2.markdown(f"- {skills[i+5]}")
        col3.markdown(f"- {skills[i+10]}")

# --- Experience (Will be Dark Gray) ---
with st.container(border=True):
    st.markdown("<h2 id='experience'>Experience</h2>", unsafe_allow_html=True)
    for job in PORTFOLIO_DATA["experience"]:
        # The CSS ensures these nested containers look like beautiful cards, not full-width sections
        with st.container(border=True):
            st.markdown(f"### {job['title']}")
            st.markdown(f"**{job['company']}** | *{job['date']}*")
            for point in job["points"]:
                st.write(f"✓ {point}")

# --- Projects (Will be #0E0E34) ---
with st.container(border=True):
    st.markdown("<h2 id='projects'>Featured Projects</h2>", unsafe_allow_html=True)
    
    proj_cols = st.columns(2)
    for i, project in enumerate(PORTFOLIO_DATA["projects"]):
        with proj_cols[i % 2]:
            with st.container(border=True):
                st.image(project["image"], use_container_width=True)
                st.markdown(f"### {project['name']}")
                st.write(project["desc"])
                st.link_button("View on GitHub", project["link"], use_container_width=True)

# --- Certifications (Will be Dark Gray) ---
with st.container(border=True):
    st.markdown("<h2 id='certifications'>Certifications</h2>", unsafe_allow_html=True)
    
    cert_cols = st.columns(3)
    for i, cert in enumerate(PORTFOLIO_DATA["certifications"]):
        with cert_cols[i % 3]:
            with st.container(border=True):
                st.image(cert["image"], use_container_width=True)
                st.markdown(f"**{cert['name']}**")
                st.write(f"Issuer: {cert['issuer']}")
