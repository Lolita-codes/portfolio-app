import textwrap
import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Omolola Blessing Lawal | Data Scientist",
    page_icon="\U0001F4A0",
    layout="wide",
)

ACCENT = "#0E0E34"


def md(html: str):
    """st.markdown wrapper that strips common leading whitespace so
    indented HTML never gets misread as a markdown code block."""
    st.markdown(textwrap.dedent(html), unsafe_allow_html=True)


# ---------- DATA ----------
LINKEDIN_URL = "https://www.linkedin.com/in/omolola-lawal-2a9a45188"
GITHUB_URL = "https://github.com/Lolita-codes"
EMAIL = "your-email@example.com"  # TODO: replace with your real email

SKILLS = [
    "Python", "Scikit-Learn", "Pandas", "Seaborn", "Matplotlib",
    "Plotly", "Numpy", "SQL & PostgreSQL", "Tableau", "Langchain",
    "NLTK", "SpaCy", "BeautifulSoup", "FastAPI", "Git & GitHub",
]

EXPERIENCE = [
    {
        "title": "Informatics Analyst",
        "meta": "University College Hospital, Ibadan, Nigeria · Nov 2023 – Nov 2024",
        "points": [
            "Identified trends and opportunities for improving medication management and safety through data.",
            "Maintained inventory management software, ensuring seamless integration with pharmacy dispensing and procurement systems.",
            "Analyzed inventory data to identify usage trends and predict future demand for medications, and maintained accurate records of drug stock levels.",
        ],
    },
    {
        "title": "Data Scientist Intern",
        "meta": "Stacksuit, Prague, Czech Republic · May 2023 – May 2024",
        "points": [
            "Built an AI-powered application leveraging natural language processing, integrating cloud storage and a vector database for file storage and RAG data retrieval.",
            "Analyzed data and developed machine learning models for user segmentation.",
            "Carried out sentiment analysis on customers' reviews and feedback.",
            "Collaborated with the engineering team to understand business objectives and created compelling visualizations to communicate data findings.",
        ],
    },
    {
        "title": "Software Developer Intern",
        "meta": "Stacksuit, Prague, Czech Republic · April 2022 – April 2023",
        "points": [
            "Maintained code integrity and organization, applying object-oriented design principles.",
            "Collaborated with the product and engineering team to design and build high-quality, reliable APIs and services.",
            "Ensured cross-country optimization.",
            "Debugged, troubleshot, and resolved production issues in a timely fashion.",
        ],
    },
]

GITHUB_MARK = "https://sitefile.co/6772c19a0931ea2de588b066/1736605813995_github-mark-ea2971cee799.png"

PROJECTS = [
    {
        "title": "Profitability Analysis",
        "desc": "Analyzes food order data to uncover insights on profitability, delivery efficiency, payment methods, and discount trends; identifies optimization areas and simulates proposed changes.",
        "url": "https://github.com/Lolita-codes/delivery_orders_profitability",
        "img": "https://sitefile.co/6772c19a0931ea2de588b066/1736605428839_deliveryordersdb.png",
    },
    {
        "title": "HR Churn Analysis",
        "desc": "Analyzes employee attrition trends within a corporate environment to identify factors contributing to employees leaving and predict employee turnover.",
        "url": "https://github.com/Lolita-codes/hr_data_analysis",
        "img": "https://sitefile.co/6772c19a0931ea2de588b066/1736605833566_hrdatadashboard.png",
    },
    {
        "title": "Credit Score – Customer Segmentation",
        "desc": "Segments customers based on standard FICO credit scores derived from multiple financial factors.",
        "url": "https://github.com/Lolita-codes/credit_score_customer_segmentation",
        "img": GITHUB_MARK,
    },
    {
        "title": "User Segmentation",
        "desc": "Segments users based on demographic and behavioral features to optimize ad targeting strategies and increase engagement and conversions.",
        "url": "https://github.com/Lolita-codes/user_segmentation",
        "img": GITHUB_MARK,
    },
    {
        "title": "House Price Prediction",
        "desc": "Explores trends and factors contributing to house pricing and builds a predictive model that estimates prices from property characteristics.",
        "url": "https://github.com/Lolita-codes/Price_prediction",
        "img": GITHUB_MARK,
    },
    {
        "title": "Google Playstore Analysis",
        "desc": "Comprehensive insights into the Android app market — ratings, reviews, category competitiveness, and pricing strategies — to help developers make informed decisions.",
        "url": "https://github.com/Lolita-codes/Google_Playstore_Apps",
        "img": GITHUB_MARK,
    },
    {
        "title": "US Police Shootings",
        "desc": "Explores social trends and factors contributing to fatal police use of force in the United States.",
        "url": "https://github.com/Lolita-codes/US_police_shootings",
        "img": GITHUB_MARK,
    },
    {
        "title": "Flight Deal Finder",
        "desc": "Tracks specified locations against a price threshold, integrates a flight search API to find deals below the cutoff, and delivers details via email and SMS.",
        "url": "https://github.com/Lolita-codes/Flight_deal_finder",
        "img": GITHUB_MARK,
    },
    {
        "title": "Sentiment Analysis – Pfizer Vaccine",
        "desc": "Identifies key sentiment trends, categorizes opinions, and provides insight into how the vaccine is perceived across demographics and platforms.",
        "url": "https://github.com/Lolita-codes/Sentiment_analysis_Pfizer_vaccine",
        "img": GITHUB_MARK,
    },
    {
        "title": "Price Optimization",
        "desc": "Uses historical sales data to predict product pricing that maximizes revenue, factoring in category, unit price, freight price, competitor prices, and other attributes.",
        "url": "https://github.com/Lolita-codes/price_optimization",
        "img": GITHUB_MARK,
    },
]

CERTIFICATIONS = [
    {
        "title": "The Data Science Course: Complete Data Science Bootcamp",
        "issuer": "Udemy",
        "img": "https://sitefile.co/6772c19a0931ea2de588b066/1735836118191_dscertpage-0001.jpg",
    },
    {
        "title": "FastAPI – The Complete Course (Beginner + Advanced)",
        "issuer": "Udemy",
        "img": "https://sitefile.co/6772c19a0931ea2de588b066/1735837771789_uc-3da0935c-a9df-4f53-9c66-3a966b0cefee.jpg",
    },
    {
        "title": "Python Django – The Practical Guide",
        "issuer": "Udemy",
        "img": "https://sitefile.co/6772c19a0931ea2de588b066/1735836792320_img4471.jpg",
    },
    {
        "title": "100 Days of Code: The Complete Python Pro Bootcamp",
        "issuer": "Udemy",
        "img": "https://sitefile.co/6772c19a0931ea2de588b066/1735835863257_python100dayscertpage-0001.jpg",
    },
    {
        "title": "Python – Data Structures and Algorithms",
        "issuer": "Udemy",
        "img": "https://sitefile.co/6772c19a0931ea2de588b066/1735836945675_675830081page-00011.jpg",
    },
]

# ---------- STYLING ----------
md(f"""
<style>
    html, body, [class*="css"] {{
        font-family: 'Lora', serif;
    }}
    h1, h2, h3 {{
        font-family: 'Georgia', serif;
        letter-spacing: 0.5px;
    }}

    /* top nav */
    .topnav {{
        position: sticky;
        top: 0;
        z-index: 999;
        background-color: {ACCENT};
        padding: 0.8rem 1.5rem;
        border-radius: 0 0 10px 10px;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 1.8rem;
        margin: -1rem -1rem 1.5rem -1rem;
    }}
    .topnav a {{
        color: #f0f0f5 !important;
        text-decoration: none;
        font-size: 0.92rem;
        font-weight: 600;
        white-space: nowrap;
    }}
    .topnav a:hover {{ color: #ffffff !important; text-decoration: underline; }}
    .dropdown {{ position: relative; display: inline-block; }}
    .dropdown-content {{
        display: none;
        position: absolute;
        right: 0;
        background-color: white;
        min-width: 150px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.15);
        border-radius: 8px;
        padding: 0.4rem 0;
        z-index: 1000;
    }}
    .dropdown-content a {{
        color: {ACCENT} !important;
        display: block;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }}
    .dropdown-content a:hover {{ background-color: #f0f0f5; text-decoration: none; }}
    .dropdown:hover .dropdown-content {{ display: block; }}

    .hero {{
        background-color: {ACCENT};
        color: white;
        padding: 3rem 2rem;
        border-radius: 12px;
        margin-bottom: 1rem;
    }}
    .hero h1 {{ color: white; font-size: 2.4rem; margin-bottom: 0.2rem; }}
    .hero p {{ color: #e0e0f0; font-size: 1.05rem; line-height: 1.6; }}

    .section-title {{
        border-bottom: 3px solid {ACCENT};
        padding-bottom: 0.3rem;
        margin-top: 2.5rem;
        margin-bottom: 1rem;
        scroll-margin-top: 90px;
    }}

    .skills-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 0.7rem;
    }}
    .skill-pill {{
        background-color: #f0f0f5;
        color: {ACCENT};
        padding: 0.6rem 0.9rem;
        border-radius: 10px;
        font-size: 0.9rem;
        font-weight: 600;
        text-align: center;
    }}

    .card {{
        background-color: #fafafc;
        border: 1px solid #e5e5ec;
        border-radius: 10px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        height: 100%;
    }}
    .card h3 {{ margin-bottom: 0.3rem; color: {ACCENT}; }}
    .card .meta {{ font-size: 0.85rem; color: #666; margin-bottom: 0.6rem; }}
    .card img {{
        width: 100%;
        height: 160px;
        object-fit: cover;
        border-radius: 8px;
        margin-bottom: 0.8rem;
        background-color: #eee;
    }}
    .cert-img {{
        width: 100%;
        border-radius: 8px;
        margin-bottom: 0.6rem;
    }}

    a {{ color: {ACCENT}; text-decoration: none; font-weight: 600; }}
    a:hover {{ text-decoration: underline; }}
</style>
""")

# ---------- TOP NAVIGATION ----------
md(f"""
<div class="topnav">
    <a href="#about">About Me</a>
    <a href="#skills">Technical Skills</a>
    <a href="#projects">Projects</a>
    <a href="#experience">Experience</a>
    <a href="#certifications">Certifications</a>
    <div class="dropdown">
        <a href="#">Connect &#9662;</a>
        <div class="dropdown-content">
            <a href="{LINKEDIN_URL}" target="_blank">LinkedIn</a>
            <a href="{GITHUB_URL}" target="_blank">GitHub</a>
            <a href="mailto:{EMAIL}">Email</a>
        </div>
    </div>
</div>
""")

# ---------- HERO / ABOUT ME ----------
md("""
<div id="about" class="hero">
    <h1>Omolola Blessing Lawal</h1>
    <h3 style="color:#c9c9e8; font-weight:400; margin-top:0;">Data Scientist</h3>
    <p>
    Hi there! I am a Data Scientist with proven ability in analyzing complex datasets to identify trends,
    develop models, and provide actionable insights that guide the strategic development of secure and
    advanced initiatives.<br><br>
    My experience spans data cleaning and transformation, data analysis and visualization,
    AI and machine learning solutions, web scraping, and script automation.<br><br>
    I am committed to innovation and collaboration, and I believe we can make something remarkable
    together — so let's connect and make a difference through technology and data!
    </p>
</div>
""")

# ---------- SKILLS ----------
skill_pills = "".join(f'<div class="skill-pill">{s}</div>' for s in SKILLS)
md(f"""
<h2 id="skills" class="section-title">Technical Skills</h2>
<div class="skills-grid">{skill_pills}</div>
""")

# ---------- PROJECTS ----------
md('<h2 id="projects" class="section-title">Projects</h2>')
proj_cols = st.columns(2)
for i, proj in enumerate(PROJECTS):
    with proj_cols[i % 2]:
        md(f"""
        <div class="card">
            <img src="{proj['img']}" alt="{proj['title']}">
            <h3>{proj['title']}</h3>
            <p>{proj['desc']}</p>
            <a href="{proj['url']}" target="_blank">View on GitHub &rarr;</a>
        </div>
        """)

# ---------- EXPERIENCE ----------
md('<h2 id="experience" class="section-title">Experience</h2>')
for job in EXPERIENCE:
    points_html = "".join(f"<li>{p}</li>" for p in job["points"])
    md(f"""
    <div class="card">
        <h3>{job['title']}</h3>
        <div class="meta">{job['meta']}</div>
        <ul>{points_html}</ul>
    </div>
    """)

# ---------- CERTIFICATIONS ----------
md('<h2 id="certifications" class="section-title">Certifications</h2>')
cert_cols = st.columns(2)
for i, cert in enumerate(CERTIFICATIONS):
    with cert_cols[i % 2]:
        md(f"""
        <div class="card">
            <img class="cert-img" src="{cert['img']}" alt="{cert['title']}">
            <h3>{cert['title']}</h3>
            <div class="meta">{cert['issuer']}</div>
        </div>
        """)

# ---------- CONTACT ----------
md('<h2 id="connect" class="section-title">Contact</h2>')
md(f"""
Let's connect! Reach out via <a href="{LINKEDIN_URL}" target="_blank">LinkedIn</a>,
check out my work on <a href="{GITHUB_URL}" target="_blank">GitHub</a>,
or drop me an <a href="mailto:{EMAIL}">email</a>.
""")

st.markdown("---")
st.caption("© Omolola Blessing Lawal")