MAIN_CSS = """
<style>

/* ── GLOBAL LAYOUT FIX ── */
.block-container {
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    max-width: 100% !important;
}

/* Full-width banner */
.ks-banner {
    width: 100vw;
    margin-left: calc(-50vw + 50%);
    border-radius: 0px !important;
    background: linear-gradient(135deg, #2E7D32, #388E3C);
    color: white;
    padding: 2rem;
    margin-bottom: 1.5rem;
}

/* ── BASE COLORS ── */
:root {
    --green-deep: #2E7D32;
    --green-mid: #388E3C;
    --green-light: #66BB6A;
    --green-pale: #C8E6C9;
    --bg: #F6F9F6;
    --card: #FFFEF5;
    --text: #1B3A1C;
    --muted: #6B7C6B;
}

/* ── BASE UI ── */
html, body, [class*="css"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: system-ui, sans-serif !important;
}

/* ── CHAT CARD ── */
.ks-chat-card {
    background: var(--card);
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 6px 20px rgba(46,125,50,0.1);
}

/* ── INPUT ── */
.stTextInput input {
    border-radius: 12px !important;
    border: 1px solid #ddd !important;
    padding: 0.6rem !important;
}

/* ── BUTTON (IMPROVED) ── */
.stButton button {
    border-radius: 10px !important;
    background: linear-gradient(135deg, #2E7D32, #388E3C) !important;
    color: white !important;
    border: none !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 12px rgba(46,125,50,0.25);
    transition: all 0.2s ease;
}

.stButton button:hover {
    transform: translateY(-2px);
    opacity: 0.95;
}

/* ── FARMER ROW ── */
.ks-farmer-row {
    background: var(--card);
    padding: 1rem;
    border-radius: 12px;
    margin-bottom: 0.5rem;
    border: 1px solid #eee;
}

/* ── EXPERT CARD (RESTORED DESIGN) ── */
.ks-expert-card {
    background: var(--card);
    padding: 1.4rem;
    border-radius: 16px;
    border: 1px solid var(--green-pale);
    box-shadow: 0 6px 20px rgba(46,125,50,0.12);
    transition: all 0.2s ease;
}

.ks-expert-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 30px rgba(46,125,50,0.2);
}

/* Avatar */
.ks-expert-avatar {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    background: linear-gradient(135deg, #2E7D32, #66BB6A);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.4rem;
    margin-bottom: 0.8rem;
}

/* Name */
.ks-expert-name {
    font-size: 1.05rem;
    font-weight: 600;
    color: var(--text);
}

/* Specialty */
.ks-expert-specialty {
    font-size: 0.85rem;
    color: var(--muted);
    margin-bottom: 0.3rem;
}

/* Tag */
.ks-expert-tag {
    display: inline-block;
    background: var(--green-pale);
    color: var(--green-deep);
    border-radius: 50px;
    padding: 0.25rem 0.7rem;
    font-size: 0.75rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
}

/* ── FOOTER ── */
.ks-footer {
    text-align: center;
    padding: 1rem;
    color: var(--muted);
}

</style>
"""
