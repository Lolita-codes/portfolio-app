import streamlit as st


PORTFOLIO_DATA = {
    "about": """
Hi there! I am a Data Scientist with proven ability in analyzing complex datasets to identify trends, develop models and provide actionable insights that guides strategic development of secure and advanced initiatives.

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

# Custom CSS to hide Streamlit defaults and recreate the hero/navbar layout
st.markdown("""
    <style>
    /* Hide Streamlit default header and footer */
    header[data-testid="stHeader"] {display: none;}
    footer {display: none;}
    
    /* Remove padding at the top of the app to let the nav sit flush */
    .block-container {
        padding-top: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    
    /* Content wrapper for Streamlit elements to keep them centered below the hero */
    .content-wrapper {
        max-width: 1000px;
        margin: 0 auto;
        padding: 2rem;
    }

    /* Import Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Montserrat:wght@400;600&display=swap');

    /* Hero Section Styling */
    .hero-container {
        background-color: #35325D; /* Matches the dark purple vibe */
        color: white;
        padding-bottom: 5rem;
        font-family: 'Montserrat', sans-serif;
        text-align: center;
        width: 100%;
    }
    
    /* Custom Navbar Styling */
    .custom-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 2rem 5%;
    }
    .nav-left {
        font-weight: 600;
        font-size: 1.3rem;
        color: #E6B5E8; /* Pink accent */
    }
    .nav-right {
        display: flex;
        gap: 2.5rem;
        font-size: 0.95rem;
    }
    .nav-right a {
        color: #E6B5E8;
        text-decoration: none;
        transition: color 0.3s;
    }
    .nav-right a:hover {
        color: white;
    }
    
    /* Dropdown Styling */
    .nav-dropdown {
        position: relative;
        display: inline-block;
        color: #E6B5E8;
        cursor: pointer;
    }
    .nav-dropdown-content {
        display: none;
        position: absolute;
        background-color: #2b284c;
        min-width: 120px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.3);
        z-index: 1;
        right: 0;
        border-radius: 4px;
        margin-top: 5px;
    }
    .nav-dropdown:hover .nav-dropdown-content {
        display: block;
    }
    .nav-dropdown-content a {
        color: white;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
        text-align: left;
    }
    .nav-dropdown-content a:hover {
        background-color: #433e75;
    }

    /* Hero Content Styling */
    .hero-content {
        padding-top: 5rem;
    }
    .hero-title {
        font-family: 'Dancing Script', cursive;
        font-size: 5rem;
        margin-bottom: 0.5rem;
        color: white;
    }
    .hero-subtitle {
        font-size: 1.5rem;
        font-weight: 400;
        margin-bottom: 1.5rem;
        color: white;
    }
    .resume-link {
        color: #E6B5E8;
        text-decoration: none;
        font-size: 1.1rem;
        border-bottom: 1px dashed #E6B5E8;
        transition: color 0.3s;
    }
    .resume-link:hover {
        color: white;
        border-bottom: 1px dashed white;
    }
    
    /* Small Social Icons */
    .social-icons {
        margin-top: 2rem;
        display: flex;
        justify-content: center;
        gap: 1.5rem;
    }
    .social-icons a {
        color: #E6B5E8;
        font-size: 1.2rem;
        text-decoration: none;
    }
    .social-icons a:hover {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. HTML NAVBAR & HERO SECTION
# ==========================================
st.markdown(f"""
    <div class="hero-container">
        <div class="custom-nav">
            <div class="nav-left">Omolola Lawal <span style="font-weight:400; font-size:0.95rem; color:#b5b3c7;">| Data Scientist</span></div>
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
            <div class="hero-title">I'm Omolola</div>
            <div class="hero-subtitle">A Data Scientist</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 4. MAIN CONTENT
# ==========================================

# We create an empty container in the center for the rest of the page content
with st.container():
    st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)
    
    # --- About Me ---
    st.markdown("<h2 id='about-me'>About Me</h2>", unsafe_allow_html=True)
    st.write(PORTFOLIO_DATA["about"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- Technical Skills (3 x 5 Layout) ---
    st.markdown("<h2 id='technical-skills'>Technical Skills</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    skills = PORTFOLIO_DATA["skills"]
    
    # Looping exactly 5 times for the 15 skills
    for i in range(5):
        col1.markdown(f"- **{skills[i]}**")
        col2.markdown(f"- **{skills[i+5]}**")
        col3.markdown(f"- **{skills[i+10]}**")

    st.divider()

    # --- Experience ---
    st.markdown("<h2 id='experience'>Experience</h2>", unsafe_allow_html=True)
    for job in PORTFOLIO_DATA["experience"]:
        with st.container(border=True):
            ecol1, ecol2 = st.columns([3, 1])
            with ecol1:
                st.subheader(job["title"])
                st.write(f"**{job['company']}**")
            with ecol2:
                st.write(f"*{job['date']}*")
            
            for point in job["points"]:
                st.write(f"✓ {point}")

    st.divider()

    # --- Projects (With Images) ---
    st.markdown("<h2 id='projects'>Featured Projects</h2>", unsafe_allow_html=True)
    
    proj_cols = st.columns(2)
    for i, project in enumerate(PORTFOLIO_DATA["projects"]):
        with proj_cols[i % 2]:
            with st.container(border=True):
                st.image(project["image"], use_container_width=True)
                st.markdown(f"#### {project['name']}")
                st.write(project["desc"])
                st.link_button("View on GitHub", project["link"], use_container_width=True)

    st.divider()

    # --- Certifications (With Images) ---
    st.markdown("<h2 id='certifications'>Certifications</h2>", unsafe_allow_html=True)
    
    cert_cols = st.columns(3)
    for i, cert in enumerate(PORTFOLIO_DATA["certifications"]):
        with cert_cols[i % 3]:
            with st.container(border=True):
                st.image(cert["image"], use_container_width=True)
                st.markdown(f"**{cert['name']}**")
                st.caption(f"Issuer: {cert['issuer']}")

    st.markdown("</div>", unsafe_allow_html=True)