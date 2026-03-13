import streamlit as st
import base64

from scraper.wiki_scraper import fetch_wikipedia_page, parse_article
from nlp.key_facts import extract_key_facts
from nlp.concepts import extract_concepts
from nlp.keywords import extract_keywords


# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="ScarPit",
    page_icon="📚",
    layout="wide"
)


# ---------- BACKGROUND IMAGE ----------
def set_bg(image_file):

    with open(image_file, "rb") as f:
        data = f.read()

    encoded = base64.b64encode(data).decode()

    bg_css = f"""
    <style>

    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* HEADER BOX */
    .header-box {{
        background-color:white;
        padding:25px;
        border-radius:12px;
        margin-bottom:20px;
        box-shadow:0px 2px 10px rgba(0,0,0,0.25);
    }}

    .header-title {{
        font-size:42px;
        font-weight:700;
        color:black;
    }}

    .header-sub {{
        font-size:17px;
        color:#333;
    }}

    /* SEARCH BOX FIX */
    div[data-testid="stTextInput"] {{
        background:white;
        padding:20px;
        border-radius:12px;
        margin-bottom:15px;
        box-shadow:0px 2px 8px rgba(0,0,0,0.25);
    }}

    div[data-testid="stTextInput"] label {{
        color:black;
        font-size:18px;
        font-weight:600;
    }}

    div[data-testid="stTextInput"] input {{
        background-color:white !important;
        color:black !important;
    }}

    /* SEARCH BUTTON */
    div.stButton > button {{
        background-color:#333;
        color:white;
        border-radius:8px;
        padding:10px 25px;
    }}

    /* RESULT CARD */
    .card {{
        background-color:#3a3a3a;
        padding:25px;
        border-radius:12px;
        margin-top:20px;
        color:white;
    }}

    .section-title {{
        font-size:22px;
        font-weight:600;
        margin-bottom:10px;
    }}

    /* KEYWORD TAG */
    .keyword {{
        display:inline-block;
        background:#555;
        padding:6px 12px;
        margin:5px;
        border-radius:6px;
        font-size:14px;
    }}

    </style>
    """

    st.markdown(bg_css, unsafe_allow_html=True)


set_bg("bg.jpg")


# ---------- HEADER ----------
st.markdown("""
<div class="header-box">

<div class="header-title">
📚 ScarPit 📚
</div>

<div class="header-sub">
Search any topic and extract structured knowledge from Wikipedia.
</div>

</div>
""", unsafe_allow_html=True)


# ---------- SEARCH ----------
topic = st.text_input("🔎 Enter Wikipedia Topic", placeholder="Type a topic like 'Artificial Intelligence'")
search = st.button("Search")


# ---------- MAIN PROCESS ----------
if search and topic:

    try:

        html = fetch_wikipedia_page(topic)

        article = parse_article(html)

        text = article["text"]

        facts = extract_key_facts(text)
        concepts = extract_concepts(text)
        keywords = extract_keywords(text)


        # ARTICLE TITLE
        st.markdown(f"""
        <div class="card">
        <div class="section-title">📄 Article Title</div>
        {article["title"]}
        </div>
        """, unsafe_allow_html=True)


        # SUMMARY
        st.markdown(f"""
        <div class="card">
        <div class="section-title">📝 Summary</div>
        {article["summary"]}
        </div>
        """, unsafe_allow_html=True)


        # KEY FACTS
        facts_html = ""
        for f in facts:
            facts_html += f"<p>• {f}</p>"

        st.markdown(f"""
        <div class="card">
        <div class="section-title">⭐ Key Facts</div>
        {facts_html}
        </div>
        """, unsafe_allow_html=True)


        # IMPORTANT CONCEPTS
        concepts_html = ""
        for c in concepts:
            concepts_html += f"<p>• {c}</p>"

        st.markdown(f"""
        <div class="card">
        <div class="section-title">🧠 Important Concepts</div>
        {concepts_html}
        </div>
        """, unsafe_allow_html=True)


        # KEYWORDS
        keyword_html = ""
        for k in keywords:
            keyword_html += f'<span class="keyword">{k}</span>'

        st.markdown(f"""
        <div class="card">
        <div class="section-title">🏷 Keywords</div>
        {keyword_html}
        </div>
        """, unsafe_allow_html=True)


    except Exception as e:

        st.error(str(e))