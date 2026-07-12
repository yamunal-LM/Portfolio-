
app_py_content = '''import streamlit as st
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Yamuna L - Data Science Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to hide Streamlit default elements
hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Read HTML file
html_file = Path("yamuna_portfolio.html")

# Check if file exists, if not use embedded HTML
if html_file.exists():
    html_content = html_file.read_text(encoding="utf-8")
else:
    # Fallback: embedded HTML content
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Yamuna L - Portfolio</title>
        <style>
            :root {
                --primary: #0ea5e9;
                --secondary: #6366f1;
                --accent: #f59e0b;
                --dark: #0f172a;
                --light: #f8fafc;
                --glass: rgba(255,255,255,0.08);
                --border: rgba(255,255,255,0.1);
            }
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', system-ui, sans-serif;
                background: var(--dark);
                color: var(--light);
                overflow-x: hidden;
                line-height: 1.6;
            }
            .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
            
            .bg-animation {
                position: fixed;
                top: 0; left: 0; width: 100%; height: 100%;
                z-index: -1;
                background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
                overflow: hidden;
            }
            .bg-animation::before {
                content: '';
                position: absolute;
                width: 200%; height: 200%;
                background: radial-gradient(circle at 20% 50%, rgba(14,165,233,0.15) 0%, transparent 50%),
                            radial-gradient(circle at 80% 80%, rgba(99,102,241,0.15) 0%, transparent 50%),
                            radial-gradient(circle at 40% 20%, rgba(245,158,11,0.1) 0%, transparent 50%);
                animation: bgMove 20s ease-in-out infinite;
            }
            @keyframes bgMove {
                0%,100% { transform: translate(0,0); }
                50% { transform: translate(-5%, -5%); }
            }
            
            .particles { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; }
            .particle {
                position: absolute;
                width: 4px; height: 4px;
                background: var(--primary);
                border-radius: 50%;
                opacity: 0.5;
                animation: float 15s infinite;
            }
            @keyframes float {
                0%,100% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
                10% { opacity: 0.5; }
                90% { opacity: 0.5; }
                100% { transform: translateY(-10vh) rotate(720deg); opacity: 0; }
            }
            
            nav {
                position: fixed;
                top: 0; width: 100%;
                padding: 20px 0;
                z-index: 1000;
                backdrop-filter: blur(20px);
                background: rgba(15,23,42,0.8);
                border-bottom: 1px solid var(--border);
                transition: all 0.3s ease;
            }
            nav .container { display: flex; justify-content: space-between; align-items: center; }
            .logo { font-size: 1.5rem; font-weight: 800; background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
            .nav-links { display: flex; gap: 30px; list-style: none; }
            .nav-links a { color: var(--light); text-decoration: none; font-weight: 500; position: relative; transition: color 0.3s; }
            .nav-links a::after { content: ''; position: absolute; bottom: -5px; left: 0; width: 0; height: 2px; background: var(--primary); transition: width 0.3s; }
            .nav-links a:hover::after { width: 100%; }
            .nav-links a:hover { color: var(--primary); }
            .mobile-menu-btn { display: none; background: none; border: none; color: var(--light); font-size: 1.5rem; cursor: pointer; }
            
            .hero {
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                position: relative;
                padding-top: 80px;
            }
            .hero-content { position: relative; z-index: 2; }
            .hero-badge {
                display: inline-block;
                padding: 8px 20px;
                background: var(--glass);
                border: 1px solid var(--border);
                border-radius: 50px;
                font-size: 0.9rem;
                color: var(--primary);
                margin-bottom: 20px;
                animation: fadeInUp 0.6s ease;
            }
            .hero h1 {
                font-size: clamp(2.5rem, 6vw, 4.5rem);
                font-weight: 800;
                margin-bottom: 10px;
                line-height: 1.1;
            }
            .hero h1 span { background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
            .hero .subtitle {
                font-size: clamp(1.2rem, 3vw, 1.8rem);
                color: #94a3b8;
                margin-bottom: 20px;
                animation: fadeInUp 0.8s ease;
            }
            .hero p {
                max-width: 600px;
                margin: 0 auto 30px;
                color: #64748b;
                font-size: 1.1rem;
                animation: fadeInUp 1s ease;
            }
            .hero-btns { display: flex; gap: 15px; justify-content: center; flex-wrap: wrap; animation: fadeInUp 1.2s ease; }
            .btn {
                padding: 12px 30px;
                border-radius: 50px;
                text-decoration: none;
                font-weight: 600;
                transition: all 0.3s ease;
                display: inline-flex;
                align-items: center;
                gap: 8px;
                cursor: pointer;
                border: none;
                font-size: 1rem;
            }
            .btn-primary { background: linear-gradient(135deg, var(--primary), var(--secondary)); color: white; box-shadow: 0 10px 30px rgba(14,165,233,0.3); }
            .btn-primary:hover { transform: translateY(-3px); box-shadow: 0 15px 40px rgba(14,165,233,0.4); }
            .btn-outline { background: transparent; color: var(--light); border: 2px solid var(--border); }
            .btn-outline:hover { border-color: var(--primary); color: var(--primary); transform: translateY(-3px); }
            
            .hero-profile {
                width: 180px; height: 180px;
                border-radius: 50%;
                margin: 0 auto 30px;
                border: 4px solid var(--primary);
                box-shadow: 0 0 40px rgba(14,165,233,0.3), 0 0 80px rgba(99,102,241,0.2);
                animation: fadeInUp 0.4s ease, pulse 3s infinite;
                object-fit: cover;
            }
            @keyframes pulse {
                0%,100% { box-shadow: 0 0 40px rgba(14,165,233,0.3), 0 0 80px rgba(99,102,241,0.2); }
                50% { box-shadow: 0 0 60px rgba(14,165,233,0.5), 0 0 100px rgba(99,102,241,0.3); }
            }
            
            @keyframes fadeInUp {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            section { padding: 100px 0; position: relative; }
            .section-title {
                text-align: center;
                font-size: 2.5rem;
                font-weight: 800;
                margin-bottom: 50px;
                position: relative;
                display: inline-block;
                left: 50%; transform: translateX(-50%);
            }
            .section-title::after {
                content: '';
                position: absolute;
                bottom: -10px; left: 50%;
                transform: translateX(-50%);
                width: 60px; height: 4px;
                background: linear-gradient(135deg, var(--primary), var(--secondary));
                border-radius: 2px;
            }
            
            .about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: center; }
            .about-text { font-size: 1.1rem; color: #94a3b8; line-height: 1.8; }
            .about-text strong { color: var(--primary); }
            .about-stats { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
            .stat-card {
                background: var(--glass);
                border: 1px solid var(--border);
                border-radius: 16px;
                padding: 25px;
                text-align: center;
                transition: all 0.3s ease;
            }
            .stat-card:hover { transform: translateY(-5px); border-color: var(--primary); }
            .stat-card .number { font-size: 2.5rem; font-weight: 800; color: var(--primary); }
            .stat-card .label { color: #64748b; font-size: 0.9rem; margin-top: 5px; }
            
            .skills-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
            .skill-card {
                background: var(--glass);
                border: 1px solid var(--border);
                border-radius: 20px;
                padding: 30px;
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
            }
            .skill-card::before {
                content: '';
                position: absolute;
                top: 0; left: 0; width: 100%; height: 3px;
                background: linear-gradient(90deg, var(--primary), var(--secondary));
                transform: scaleX(0);
                transform-origin: left;
                transition: transform 0.3s ease;
            }
            .skill-card:hover::before { transform: scaleX(1); }
            .skill-card:hover { transform: translateY(-5px); border-color: var(--primary); }
            .skill-icon { font-size: 2.5rem; margin-bottom: 15px; }
            .skill-card h3 { font-size: 1.3rem; margin-bottom: 15px; }
            .skill-bar { height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; overflow: hidden; margin-bottom: 10px; }
            .skill-progress {
                height: 100%;
                background: linear-gradient(90deg, var(--primary), var(--secondary));
                border-radius: 4px;
                transition: width 1.5s ease;
                position: relative;
            }
            .skill-progress::after {
                content: attr(data-percent);
                position: absolute;
                right: 0; top: -25px;
                font-size: 0.85rem;
                color: var(--primary);
                font-weight: 600;
            }
            
            .projects-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; }
            .project-card {
                background: var(--glass);
                border: 1px solid var(--border);
                border-radius: 20px;
                overflow: hidden;
                transition: all 0.3s ease;
                position: relative;
            }
            .project-card:hover { transform: translateY(-10px); border-color: var(--primary); }
            .project-header {
                padding: 30px 30px 20px;
                background: linear-gradient(135deg, rgba(14,165,233,0.1), rgba(99,102,241,0.1));
            }
            .project-icon { font-size: 3rem; margin-bottom: 15px; }
            .project-card h3 { font-size: 1.4rem; margin-bottom: 10px; }
            .project-tags { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 15px; }
            .tag {
                padding: 4px 12px;
                background: rgba(14,165,233,0.2);
                color: var(--primary);
                border-radius: 50px;
                font-size: 0.8rem;
                font-weight: 500;
            }
            .project-body { padding: 0 30px 30px; color: #94a3b8; }
            .project-links { display: flex; gap: 10px; padding: 0 30px 30px; }
            .project-links .btn { padding: 8px 20px; font-size: 0.9rem; }
            
            .timeline { position: relative; max-width: 800px; margin: 0 auto; }
            .timeline::before {
                content: '';
                position: absolute;
                left: 50%; transform: translateX(-50%);
                width: 2px; height: 100%;
                background: linear-gradient(to bottom, var(--primary), var(--secondary));
            }
            .timeline-item {
                position: relative;
                margin-bottom: 40px;
                width: 50%;
                padding: 0 40px;
            }
            .timeline-item:nth-child(odd) { left: 0; text-align: right; }
            .timeline-item:nth-child(even) { left: 50%; }
            .timeline-dot {
                position: absolute;
                width: 20px; height: 20px;
                background: var(--primary);
                border-radius: 50%;
                top: 5px;
                border: 4px solid var(--dark);
                box-shadow: 0 0 20px rgba(14,165,233,0.5);
            }
            .timeline-item:nth-child(odd) .timeline-dot { right: -10px; }
            .timeline-item:nth-child(even) .timeline-dot { left: -10px; }
            .timeline-content {
                background: var(--glass);
                border: 1px solid var(--border);
                border-radius: 16px;
                padding: 25px;
                transition: all 0.3s ease;
            }
            .timeline-content:hover { border-color: var(--primary); transform: scale(1.02); }
            .timeline-year { color: var(--primary); font-weight: 700; font-size: 0.9rem; margin-bottom: 5px; }
            .timeline-content h3 { font-size: 1.2rem; margin-bottom: 5px; }
            .timeline-content p { color: #94a3b8; font-size: 0.95rem; }
            
            .cert-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 25px; }
            .cert-card {
                background: var(--glass);
                border: 1px solid var(--border);
                border-radius: 16px;
                padding: 25px;
                display: flex;
                align-items: flex-start;
                gap: 15px;
                transition: all 0.3s ease;
            }
            .cert-card:hover { border-color: var(--accent); transform: translateX(5px); }
            .cert-icon { font-size: 2rem; flex-shrink: 0; }
            .cert-card h4 { font-size: 1rem; margin-bottom: 5px; }
            .cert-card p { color: #64748b; font-size: 0.85rem; }
            
            .contact-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
            .contact-card {
                background: var(--glass);
                border: 1px solid var(--border);
                border-radius: 16px;
                padding: 25px;
                text-align: center;
                transition: all 0.3s ease;
                text-decoration: none;
                color: var(--light);
                display: block;
            }
            .contact-card:hover { border-color: var(--primary); transform: translateY(-5px); }
            .contact-icon { font-size: 2rem; margin-bottom: 10px; }
            .contact-card h4 { margin-bottom: 5px; }
            .contact-card p { color: #94a3b8; font-size: 0.9rem; }
            
            footer {
                text-align: center;
                padding: 40px 0;
                border-top: 1px solid var(--border);
                color: #64748b;
            }
            
            .reveal { opacity: 0; transform: translateY(30px); transition: all 0.6s ease; }
            .reveal.active { opacity: 1; transform: translateY(0); }
            
            @media (max-width: 768px) {
                .nav-links { display: none; position: absolute; top: 70px; left: 0; width: 100%; background: rgba(15,23,42,0.95); flex-direction: column; padding: 20px; gap: 15px; }
                .nav-links.active { display: flex; }
                .mobile-menu-btn { display: block; }
                .about-grid { grid-template-columns: 1fr; }
                .timeline::before { left: 20px; }
                .timeline-item { width: 100%; left: 0 !important; padding-left: 50px; padding-right: 0; text-align: left !important; }
                .timeline-dot { left: 10px !important; right: auto !important; }
                .projects-grid { grid-template-columns: 1fr; }
            }
            
            .typing-text::after {
                content: '|';
                animation: blink 1s infinite;
                color: var(--primary);
            }
            @keyframes blink { 0%,100% { opacity: 1; } 50% { opacity: 0; } }
        </style>
    </head>
    <body>
        <div class="bg-animation"></div>
        <div class="particles" id="particles"></div>

        <nav id="navbar">
            <div class="container">
                <div class="logo">Yamuna L</div>
                <button class="mobile-menu-btn" onclick="toggleMenu()">&#9776;</button>
                <ul class="nav-links" id="navLinks">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#skills">Skills</a></li>
                    <li><a href="#projects">Projects</a></li>
                    <li><a href="#education">Education</a></li>
                    <li><a href="#certificates">Certificates</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </div>
        </nav>

        <section class="hero" id="home">
            <div class="hero-content">
                <div class="hero-badge">&#127891; B.Tech IT Student | Data Science Enthusiast</div>
                <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&h=400&fit=crop&crop=face" alt="Yamuna L" class="hero-profile" id="profileImg">
                <h1>Hello, I'm <span>Yamuna L</span></h1>
                <p class="subtitle"><span class="typing-text" id="typing"></span></p>
                <p>Detail-oriented Data Science aspirant with a strong foundation in data analysis, machine learning, and visualization. Passionate about transforming raw data into meaningful insights using Python and Excel.</p>
                <div class="hero-btns">
                    <a href="#projects" class="btn btn-primary">&#128202; View My Projects</a>
                    <a href="#contact" class="btn btn-outline">&#128231; Contact Me</a>
                </div>
            </div>
        </section>

        <section id="about">
            <div class="container">
                <h2 class="section-title reveal">About Me</h2>
                <div class="about-grid">
                    <div class="about-text reveal">
                        <p>I'm a <strong>passionate Data Science student</strong> currently pursuing my B.Tech in Information Technology at Varuvan Vadivelan Institute of Technology, Dha
