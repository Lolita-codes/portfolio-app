import streamlit as st
from PIL import Image
import requests
from io import BytesIO


PORTFOLIO_DATA = {
    "name": "Omolola Blessing Lawal",
    "role": "Data Scientist",
    "profile_image_url": "https://sitefile.co/6772c19a0931ea2de588b066/1735826699400_unnamed2.jpg",
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
        "Python", "Scikit-Learn", "Pandas", "Seaborn", "Matplotlib", "Plotly",
        "Numpy", "SQL & PostgreSQL", "Tableau", "Langchain", "NLTK", "SpaCy",
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
            "name": "Profitability Analysis",
            "desc": "Analyzes food order data to uncover insights regarding profitability, delivery efficiency, and payment methods.",
            "link": "https://github.com/Lolita-codes/delivery_orders_profitability"
        },
        {
            "name": "HR Churn Analysis",
            "desc": "Analyzes employee attrition trends to identify factors contributing to turnover and predict outcomes.",
            "link": "https://github.com/Lolita-codes/hr_data_analysis"
        },
        {
            "name": "Credit Score - Customer Segmentation",
            "desc": "Segments customers based on standard FICO credit scores derived from multiple financial factors.",
            "link": "https://github.com/Lolita-codes/credit_score_customer_segmentation"
        },
        {
            "name": "User Segmentation",
            "desc": "Segments users based on demographic and behavioral features to optimize ad targeting strategies.",
            "link": "https://github.com/Lolita-codes/user_segmentation"
        },
        {
            "name": "House Price Prediction",
            "desc": "Builds a predictive model that estimates house prices based on various property characteristics.",
            "link": "https://github.com/Lolita-codes/Price_prediction"
        },
        {
            "name": "Google Playstore Analysis",
            "desc": "Provides comprehensive insights into the Android app market, from app ratings to category competitiveness.",
            "link": "https://github.com/Lolita-codes/Google_Playstore_Apps"
        },
        {
            "name": "Flight Deal Finder",
            "desc": "Tracks specific locations and integrates with a flight search API to identify and notify about deals below a price threshold.",
            "link": "https://github.com/Lolita-codes/Flight_deal_finder"
        },
        {
            "name": "Sentiment Analysis",
            "desc": "Identifies key sentiment trends and provides insights into how a vaccine is perceived across demographics.",
            "link": "https://github.com/Lolita-codes/Sentiment_analysis_Pfizer_vaccine"
        }
    ],
    "education": [
        {
            "degree": "Bachelor of Pharmacy",
            "school": "Obafemi Awolowo University, Nigeria",
            "details": "CGPA 4.72/5.00 — Best Graduating Student, Faculty of Pharmacy '23"
        }
    ],
    "certifications": [
        "The Data Science Course: Complete Data Science Bootcamp (Udemy)",
        "FastAPI – The Complete Course (Beginner+Advanced) (Udemy)",
        "Python Django – The Practical Guide (Udemy)",
        "100 Days of Code: The Complete Python Pro Bootcamp (Udemy)",
        "Python - Data Structures and Algorithms (Udemy)"
    ]
}

# ==========================================
# 2. APP CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title=f"{PORTFOLIO_DATA['name']} | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a cleaner look
st.markdown("""
    <style>
    /* Adjust top padding */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 2rem;
    }
    /* Style for the project cards */
    .st-emotion-cache-12w0qpk {
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    }
    .st-emotion-cache-12w0qpk:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Fetch image helper function
@st.cache_data
def load_image(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
    except:
        return None

# ==========================================
# 3. SIDEBAR NAVIGATION & CONTACT
# ==========================================
with st.sidebar:
    profile_img = load_image(PORTFOLIO_DATA["profile_image_url"])
    if profile_img:
        # Create a circular mask for the image if desired, or just display
        st.image(profile_img, use_container_width=True)
    
    st.title(PORTFOLIO_DATA["name"])
    st.subheader(PORTFOLIO_DATA["role"])
    
    st.divider()
    
    # Navigation mapping
    st.markdown("### Navigation")
    st.markdown("[About & Skills](#about-skills)")
    st.markdown("[Experience](#experience)")
    st.markdown("[Projects](#projects)")
    st.markdown("[Education & Certifications](#education-certifications)")
    
    st.divider()
    
    st.markdown("### Connect")
    st.link_button("LinkedIn", PORTFOLIO_DATA["contact"]["linkedin"], use_container_width=True)
    st.link_button("GitHub", PORTFOLIO_DATA["contact"]["github"], use_container_width=True)

# ==========================================
# 4. MAIN CONTENT
# ==========================================

# --- About & Skills ---
st.markdown("<h2 id='about-skills'>About Me</h2>", unsafe_allow_html=True)
st.write(PORTFOLIO_DATA["about"])

st.markdown("### Technical Skills")
# Using Streamlit's native pills (or columns for badges) for skills
st.pills("Skills", PORTFOLIO_DATA["skills"], label_visibility="collapsed")

st.divider()

# --- Experience ---
st.markdown("<h2 id='experience'>Experience</h2>", unsafe_allow_html=True)
for job in PORTFOLIO_DATA["experience"]:
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader(job["title"])
            st.write(f"**{job['company']}**")
        with col2:
            st.write(f"*{job['date']}*")
        
        for point in job["points"]:
            st.write(f"✓ {point}")

st.divider()

# --- Projects ---
st.markdown("<h2 id='projects'>Featured Projects</h2>", unsafe_allow_html=True)
st.write("A selection of my recent data science and machine learning work.")

# Display projects in a grid layout (3 columns)
cols = st.columns(3)
for i, project in enumerate(PORTFOLIO_DATA["projects"]):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"#### {project['name']}")
            st.write(project["desc"])
            st.link_button("View on GitHub", project["link"], use_container_width=True)

st.divider()

# --- Education & Certifications ---
st.markdown("<h2 id='education-certifications'>Education & Certifications</h2>", unsafe_allow_html=True)

col_edu, col_cert = st.columns(2)

with col_edu:
    st.markdown("### Education")
    for edu in PORTFOLIO_DATA["education"]:
        with st.container(border=True):
            st.subheader(edu["degree"])
            st.write(f"**{edu['school']}**")
            st.write(edu["details"])

with col_cert:
    st.markdown("### Certifications")
    with st.container(border=True):
        for cert in PORTFOLIO_DATA["certifications"]:
            st.write(f"🏆 {cert}")
            