# 🌱 KisanSathi — AI Agriculture Assistant

A premium MVP web app for Indian farmers powered by Groq AI (LLaMA 3 70B).

---

## 🚀 Quick Start

### 1. Clone / extract the project
```bash
cd kisansathi
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
```bash
cp .env.example .env
```
Open `.env` and replace `your_groq_api_key_here` with your actual key.
Get a **free** key at: https://console.groq.com

### 5. Run the app
```bash
streamlit run app.py
```

The app opens at **http://localhost:8501** 🎉

---

## 📁 Project Structure

```
kisansathi/
├── app.py                  # Main entry point & page orchestrator
├── components/
│   ├── chat.py             # AI chat UI + message history
│   ├── experts.py          # Expert cards with prefill
│   └── farmers.py          # Nearby farmers list with prefill
├── utils/
│   └── groq_client.py      # Groq API wrapper & error handling
├── styles/
│   └── css.py              # All custom CSS (agriculture theme)
├── .env.example            # API key template
├── requirements.txt
└── README.md
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 💬 AI Chat | Ask farming questions, get practical advice |
| 📸 Image Upload | Attach crop/soil photos for contextual advice |
| 👨‍🔬 Experts | 3 specialist cards that prefill relevant questions |
| 🚜 Nearby Farmers | 4 farmer profiles with instant chat prefill |
| 🎨 Premium UI | Agriculture-themed design with green/brown palette |

---

## 🎨 Design System

| Token | Value | Usage |
|---|---|---|
| Deep Green | `#2E7D32` | Primary brand, buttons |
| Soil Brown | `#8D6E63` | Farmer cards, accents |
| Light Cream | `#F5F5DC` | Page background |
| Leaf Green | `#66BB6A` | Tags, highlights |

---

## 🔑 Groq API

- Model: `llama3-70b-8192` (fast, accurate, free tier available)
- Free tier: 14,400 requests/day, 6,000 tokens/min
- Upgrade: https://console.groq.com/settings/billing
