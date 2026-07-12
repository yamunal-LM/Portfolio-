
app_py_final = '''import streamlit as st
import os

st.set_page_config(
    page_title="Yamuna L - Data Science Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;}
</style>
""", unsafe_allow_html=True)

# Read HTML file from same directory
html_path = os.path.join(os.path.dirname(__file__), "yamuna_portfolio.html")

try:
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=800, scrolling=True)
except FileNotFoundError:
    st.error("yamuna_portfolio.html not found! Please make sure it's uploaded to your GitHub repo.")
'''

with open('/mnt/agents/output/app.py', 'w', encoding='utf-8') as f:
    f.write(app_py_final)

print("Fixed app.py created successfully!")
print("File saved to: /mnt/agents/output/app.py")
