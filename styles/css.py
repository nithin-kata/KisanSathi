"""
KisanSathi - Global CSS styles
Agriculture-inspired premium UI with dual color palette
"""

MAIN_CSS = """
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── CSS Variables ── */
:root {
    --green-deep:   #2E7D32;
    --green-mid:    #388E3C;
    --green-leaf:   #66BB6A;
    --green-pale:   #C8E6C9;
    --brown-soil:   #8D6E63;
    --brown-light:  #BCAAA4;
    --cream-bg:     #F5F5DC;
    --cream-card:   #FFFEF5;
    --cream-dark:   #EFEFE0;
    --text-dark:    #1B3A1C;
    --text-mid:     #4A6741;
    --text-muted:   #7A8A78;
    --shadow-sm:    0 2px 12px rgba(46,125,50,0.08);
    --shadow-md:    0 6px 28px rgba(46,125,50,0.13);
    --shadow-lg:    0 12px 48px rgba(46,125,50,0.18);
    --radius-sm:    10px;
    --radius-md:    14px;
    --radius-lg:    20px;
}

/* ── Reset & Base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
    background-color: var(--cream-bg) !important;
    color: var(--text-dark) !important;
}

/* Remove default Streamlit padding */
.block-container {
    padding: 1.5rem 2rem 3rem 2rem !important;
    max-width: 900px !important;
}

/* Hide Streamlit branding */
#MainMenu, footer { visibility: hidden; }
header { background: transparent !important; }
.stDeployButton { display: none; }

/* ── Header ── */
.ks-header {
    background: linear-gradient(135deg, var(--green-deep) 0%, var(--green-mid) 60%, #43A047 100%);
    border-radius: var(--radius-lg);
    padding: 2.4rem 2.8rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow-lg);
}

.ks-header::before {
    content: "";
    position: absolute;
    top: -40px; right: -40px;
    width: 220px; height: 220px;
    background: rgba(255,255,255,0.05);
    border-radius: 50%;
}

.ks-header::after {
    content: "";
    position: absolute;
    bottom: -60px; left: 30%;
    width: 300px; height: 300px;
    background: rgba(102,187,106,0.12);
    border-radius: 50%;
}

.ks-header-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 2.6rem !important;
    font-weight: 700 !important;
    color: #ffffff !important;
    margin: 0 0 0.3rem 0 !important;
    letter-spacing: -0.5px;
    position: relative; z-index: 1;
}

.ks-header-tagline {
    font-size: 1.05rem !important;
    color: rgba(255,255,255,0.82) !important;
    font-weight: 300 !important;
    margin: 0 !important;
    position: relative; z-index: 1;
}

.ks-header-meta {
    margin-top: 1.2rem;
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    position: relative; z-index: 1;
}

.ks-badge {
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.25);
    color: #fff;
    padding: 0.3rem 0.9rem;
    border-radius: 50px;
    font-size: 0.78rem;
    font-weight: 500;
    backdrop-filter: blur(4px);
}

/* ── Section Headers ── */
.ks-section-label {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.35rem !important;
    color: var(--green-deep) !important;
    font-weight: 600 !important;
    margin: 2rem 0 1rem 0 !important;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.ks-divider {
    height: 2px;
    background: linear-gradient(to right, var(--green-pale), transparent);
    border: none;
    margin: 0.5rem 0 1.5rem 0;
}

/* ── Chat Card ── */
.ks-chat-card {
    background: var(--cream-card);
    border-radius: var(--radius-lg);
    padding: 1.8rem 2rem;
    border: 1px solid var(--green-pale);
    box-shadow: var(--shadow-md);
    margin-bottom: 1.5rem;
}

/* ── Message Bubbles ── */
.ks-msg-user {
    background: linear-gradient(135deg, var(--green-deep), var(--green-mid));
    color: #fff;
    border-radius: var(--radius-md) var(--radius-md) 4px var(--radius-md);
    padding: 0.9rem 1.2rem;
    margin: 0.6rem 0;
    max-width: 82%;
    margin-left: auto;
    font-size: 0.95rem;
    line-height: 1.55;
    box-shadow: var(--shadow-sm);
    word-wrap: break-word;
}

.ks-msg-bot {
    background: var(--cream-card);
    color: var(--text-dark);
    border-radius: var(--radius-md) var(--radius-md) var(--radius-md) 4px;
    padding: 1rem 1.2rem;
    margin: 0.6rem 0;
    max-width: 88%;
    font-size: 0.95rem;
    line-height: 1.65;
    border: 1px solid var(--green-pale);
    box-shadow: var(--shadow-sm);
    word-wrap: break-word;
}

.ks-msg-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
    opacity: 0.65;
}

.ks-msg-user .ks-msg-label { color: rgba(255,255,255,0.8); }
.ks-msg-bot .ks-msg-label  { color: var(--green-deep); }

/* Chat history container */
.ks-chat-history {
    max-height: 380px;
    overflow-y: auto;
    padding: 0.5rem 0;
    margin-bottom: 1.2rem;
    scrollbar-width: thin;
    scrollbar-color: var(--green-pale) transparent;
}

.ks-chat-history::-webkit-scrollbar { width: 5px; }
.ks-chat-history::-webkit-scrollbar-thumb { background: var(--green-pale); border-radius: 4px; }

/* Image upload zone */
.ks-upload-hint {
    background: var(--cream-dark);
    border: 2px dashed var(--green-pale);
    border-radius: var(--radius-sm);
    padding: 0.7rem 1rem;
    text-align: center;
    font-size: 0.82rem;
    color: var(--text-muted);
    margin-bottom: 0.8rem;
}

/* ── Expert Cards ── */
.ks-expert-card {
    background: var(--cream-card);
    border-radius: var(--radius-md);
    padding: 1.4rem 1.5rem;
    border: 1px solid var(--green-pale);
    box-shadow: var(--shadow-sm);
    height: 100%;
    transition: box-shadow 0.2s ease, transform 0.2s ease;
}

.ks-expert-card:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-2px);
}

.ks-expert-avatar {
    width: 52px; height: 52px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--green-deep), var(--green-leaf));
    display: flex; align-items: center; justify-content: center;
    font-size: 1.5rem;
    margin-bottom: 0.9rem;
    box-shadow: 0 4px 12px rgba(46,125,50,0.25);
}

.ks-expert-name {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.05rem !important;
    font-weight: 600 !important;
    color: var(--text-dark) !important;
    margin: 0 0 0.25rem 0 !important;
}

.ks-expert-specialty {
    font-size: 0.82rem;
    color: var(--brown-soil);
    font-weight: 500;
    margin-bottom: 0.4rem;
}

.ks-expert-tag {
    display: inline-block;
    background: var(--green-pale);
    color: var(--green-deep);
    border-radius: 50px;
    padding: 0.2rem 0.7rem;
    font-size: 0.73rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

/* ── Farmer Cards ── */
.ks-farmer-row {
    background: var(--cream-card);
    border-radius: var(--radius-sm);
    padding: 1rem 1.3rem;
    margin-bottom: 0.7rem;
    border: 1px solid var(--cream-dark);
    display: flex;
    align-items: center;
    gap: 1rem;
    box-shadow: var(--shadow-sm);
    transition: border-color 0.2s;
}

.ks-farmer-row:hover { border-color: var(--green-pale); }

.ks-farmer-icon {
    width: 40px; height: 40px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--brown-soil), var(--brown-light));
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem;
    flex-shrink: 0;
}

.ks-farmer-info { flex: 1; }

.ks-farmer-name {
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--text-dark);
    margin-bottom: 0.15rem;
}

.ks-farmer-meta {
    font-size: 0.78rem;
    color: var(--text-muted);
}

.ks-farmer-crop {
    display: inline-block;
    background: rgba(141,110,99,0.12);
    color: var(--brown-soil);
    border-radius: 50px;
    padding: 0.15rem 0.6rem;
    font-size: 0.72rem;
    font-weight: 600;
    margin-left: 0.4rem;
}

/* ── Streamlit Widget Overrides ── */
.stTextInput > div > div > input {
    background: var(--cream-dark) !important;
    border: 1.5px solid var(--green-pale) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-dark) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 0.6rem 1rem !important;
    transition: border-color 0.2s !important;
}

.stTextInput > div > div > input:focus {
    border-color: var(--green-deep) !important;
    box-shadow: 0 0 0 3px rgba(46,125,50,0.12) !important;
}

.stButton > button {
    background: linear-gradient(135deg, var(--green-deep), var(--green-mid)) !important;
    color: #fff !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    padding: 0.55rem 1.4rem !important;
    cursor: pointer !important;
    transition: opacity 0.2s, transform 0.15s !important;
    box-shadow: 0 3px 12px rgba(46,125,50,0.28) !important;
    width: 100% !important;
}

.stButton > button:hover {
    opacity: 0.92 !important;
    transform: translateY(-1px) !important;
}

.stButton > button:active { transform: translateY(0) !important; }

/* File uploader */
.stFileUploader > div {
    background: var(--cream-dark) !important;
    border: 2px dashed var(--green-pale) !important;
    border-radius: var(--radius-sm) !important;
}

/* Spinner */
.stSpinner > div { border-top-color: var(--green-deep) !important; }

/* Alerts */
.stSuccess {
    background: var(--green-pale) !important;
    border-left: 4px solid var(--green-deep) !important;
    border-radius: var(--radius-sm) !important;
}

.stWarning {
    background: #FFF8E1 !important;
    border-left: 4px solid #F9A825 !important;
    border-radius: var(--radius-sm) !important;
}

/* ── Footer ── */
.ks-footer {
    text-align: center;
    padding: 1.5rem 0 0.5rem;
    font-size: 0.78rem;
    color: var(--text-muted);
    border-top: 1px solid var(--cream-dark);
    margin-top: 2.5rem;
}
</style>
"""
