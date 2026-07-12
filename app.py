
# Read the HTML file first
with open('/mnt/agents/output/yamuna_portfolio.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Escape the HTML content for Python string
# Replace triple quotes with escaped versions
html_escaped = html_content.replace('\\', '\\\\').replace('"""', '\\"""').replace("'''", "\\'''")

# Create app.py with the HTML embedded using a different approach
app_py_embedded = f'''import streamlit as st

st.set_page_config(
    page_title="Yamuna L - Data Science Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}
header {{visibility: hidden;}}
.stDeployButton {{display:none;}}
</style>
""", unsafe_allow_html=True)

html_content = """{html_escaped}"""

st.components.v1.html(html_content, height=800, scrolling=True)
'''

with open('/mnt/agents/output/app.py', 'w', encoding='utf-8') as f:
    f.write(app_py_embedded)

print("app.py with embedded HTML created successfully!")
print(f"File size: {len(app_py_embedded)} characters")
