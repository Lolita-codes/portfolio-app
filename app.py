import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Omolola Blessing Lawal | Data Scientist",
    page_icon="💠",
    layout="wide",
)

# ---------- STYLING ----------
ACCENT = "#0E0E34"

st.markdown(
    f"""
    <style>
        html, body, [class*="css"] {{
            font-family: 'Lora', serif;
        }}
        h1, h2, h3 {{
            font-family: 'Georgia', serif;
            letter-spacing: 0.5px;
        }}
        .hero {{
            background-color: {ACCENT};
            color: white;
            padding: 3rem 2rem;
            border-radius: 12px;
            margin-bottom: 2rem;
        }}
        .hero h1 {{
            color: white;
            font-size: 2.4rem;
            margin-bottom: 0.2rem;
        }}
        .hero p {{
            color: #e0e0f0;
            font-size: 1.05rem;
            line-height: 1.6;
        }}
        .section-title {{
            border-bottom: 3px solid {ACCENT};
            padding-bottom: 0.3rem;
            margin-top: 2.5rem;
            margin-bottom: 1rem;
        }}
        .skill-pill {{
            display: inline-block;
            background-color: #f0f0f5;
            color: {ACCENT};
            padding: 0.35rem 0.9rem;
            margin: 0.2rem;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 600;
        }}
        .card {{
            background-color: #fafafc;
            border: 1px solid #e5e5ec;
            border-radius: 10px;
            padding: 1.2rem;
            margin-bottom: 1rem;
        }}
        .card h3 {{
            margin-bottom: 0.3rem;
            color: {ACCENT};
        }}
        .card .meta {{
            font-size: 0.85rem;
            color: #666;
            margin-bottom: 0.6rem;
        }}
        a {{
            color: {ACCENT};
            text-decoration: none;
            font-weight: 600;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- DATA ----------
LINKEDIN_URL = "https://www.linkedin.com/in/omolola-lawal-2a9a45188"
GITHUB_URL = "https://github.com/Lolita-codes"
EMAIL = "your-email@example.com"  # TODO: replace with your real email

SKILLS = [
    "Python", "Scikit-Learn", "Pandas", "Seaborn", "Matplotlib", "Plotly",
    "Numpy", "SQL & PostgreSQL", "Tableau", "Langchain", "NLTK", "SpaCy",
    "BeautifulSoup", "FastAPI", "Git & GitHub",
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

PROJECTS = [
    {
        "title": "Profitability Analysis",
        "desc": "Analyzes food order data to uncover insights on profitability, delivery efficiency, payment methods, and discount trends; identifies optimization areas and simulates proposed changes.",
        "url": "https://github.com/Lolita-codes/delivery_orders_profitability",
    },
    {
        "title": "HR Churn Analysis",
        "desc": "Analyzes employee attrition trends within a corporate environment to identify factors contributing to employees leaving and predict employee turnover.",
        "url": "https://github.com/Lolita-codes/hr_data_analysis",
    },
    {
        "title": "Credit Score – Customer Segmentation",
        "desc": "Segments customers based on standard FICO credit scores derived from multiple financial factors.",
        "url": "https://github.com/Lolita-codes/credit_score_customer_segmentation",
    },
    {
        "title": "User Segmentation",
        "desc": "Segments users based on demographic and behavioral features to optimize ad targeting strategies and increase engagement and conversions.",
        "url": "https://github.com/Lolita-codes/user_segmentation",
    },
    {
        "title": "House Price Prediction",
        "desc": "Explores trends and factors contributing to house pricing and builds a predictive model that estimates prices from property characteristics.",
        "url": "https://github.com/Lolita-codes/Price_prediction",
    },
    {
        "title": "Google Playstore Analysis",
        "desc": "Comprehensive insights into the Android app market — ratings, reviews, category competitiveness, and pricing strategies — to help developers make informed decisions.",
        "url": "https://github.com/Lolita-codes/Google_Playstore_Apps",
    },
    {
        "title": "US Police Shootings",
        "desc": "Explores social trends and factors contributing to fatal police use of force in the United States.",
        "url": "https://github.com/Lolita-codes/US_police_shootings",
    },
    {
        "title": "Flight Deal Finder",
        "desc": "Tracks specified locations against a price threshold, integrates a flight search API to find deals below the cutoff, and delivers details via email and SMS.",
        "url": "https://github.com/Lolita-codes/Flight_deal_finder",
    },
    {
        "title": "Sentiment Analysis – Pfizer Vaccine",
        "desc": "Identifies key sentiment trends, categorizes opinions, and provides insight into how the vaccine is perceived across demographics and platforms.",
        "url": "https://github.com/Lolita-codes/Sentiment_analysis_Pfizer_vaccine",
    },
    {
        "title": "Price Optimization",
        "desc": "Uses historical sales data to predict product pricing that maximizes revenue, factoring in category, unit price, freight price, competitor prices, and other attributes.",
        "url": "https://github.com/Lolita-codes/price_optimization",
    },
]

EDUCATION = {
    "school": "Obafemi Awolowo University, Nigeria",
    "detail": "Bachelor of Pharmacy — CGPA 4.72/5.00\nBest Graduating Student, Faculty of Pharmacy '23",
}

CERTIFICATIONS = [
    "The Data Science Course: Complete Data Science Bootcamp — Udemy",
    "FastAPI – The Complete Course (Beginner + Advanced) — Udemy",
    "Python Django – The Practical Guide — Udemy",
    "100 Days of Code: The Complete Python Pro Bootcamp — Udemy",
    "Python – Data Structures and Algorithms — Udemy",
]

# ---------- HERO ----------
st.markdown(
    f"""
    <div class="hero">
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
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("💼 LinkedIn", LINKEDIN_URL, use_container_width=True)
with col2:
    st.link_button("🐙 GitHub", GITHUB_URL, use_container_width=True)
with col3:
    st.link_button("✉️ Email", f"mailto:{EMAIL}", use_container_width=True)

# ---------- SKILLS ----------
st.markdown('<h2 class="section-title">Technical Skills</h2>', unsafe_allow_html=True)
st.markdown(
    "".join(f'<span class="skill-pill">{s}</span>' for s in SKILLS),
    unsafe_allow_html=True,
)

# ---------- EXPERIENCE ----------
st.markdown('<h2 class="section-title">Experience</h2>', unsafe_allow_html=True)
for job in EXPERIENCE:
    points_html = "".join(f"<li>{p}</li>" for p in job["points"])
    st.markdown(
        f"""
        <div class="card">
            <h3>{job['title']}</h3>
            <div class="meta">{job['meta']}</div>
            <ul>{points_html}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- PROJECTS ----------
st.markdown('<h2 class="section-title">Projects</h2>', unsafe_allow_html=True)
proj_cols = st.columns(2)
for i, proj in enumerate(PROJECTS):
    with proj_cols[i % 2]:
        st.markdown(
            f"""
            <div class="card">
                <h3>{proj['title']}</h3>
                <p>{proj['desc']}</p>
                <a href="{proj['url']}" target="_blank">View on GitHub →</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------- EDUCATION ----------
st.markdown('<h2 class="section-title">Education</h2>', unsafe_allow_html=True)
st.markdown(
    f"""
    <div class="card">
        <h3>{EDUCATION['school']}</h3>
        <p>{EDUCATION['detail'].replace(chr(10), '<br>')}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- CERTIFICATIONS ----------
st.markdown('<h2 class="section-title">Certifications</h2>', unsafe_allow_html=True)
cert_cols = st.columns(2)
for i, cert in enumerate(CERTIFICATIONS):
    with cert_cols[i % 2]:
        st.markdown(f"- {cert}")

# ---------- CONTACT ----------
st.markdown('<h2 class="section-title">Contact</h2>', unsafe_allow_html=True)
st.markdown(
    f"""
    Let's connect! Reach out via [LinkedIn]({LINKEDIN_URL}), check out my work on
    [GitHub]({GITHUB_URL}), or drop me an [email](mailto:{EMAIL}).
    """
)

st.markdown("---")
st.caption("© Omolola Blessing Lawal")
