
app_py_simple = '''import streamlit as st
from pathlib import Path

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

html_file = Path("yamuna_portfolio.html")
if html_file.exists():
    html_content = html_file.read_text(encoding="utf-8")
    st.components.v1.html(html_content, height=800, scrolling=True)
else:
    st.error("yamuna_portfolio.html file not found! Please upload it to your GitHub repo.")
'''

with open('/mnt/agents/output/app.py', 'w', encoding='utf-8') as f:
    f.write(app_py_simple)

print("Simplified app.py created successfully!")
print("File saved to: /mnt/agents/output/app.py")
