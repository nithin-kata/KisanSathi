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

**Output Screens**
<img width="1455" height="765" alt="image" src="https://github.com/user-attachments/assets/20b3ad06-1b41-47a2-b6cd-617b00766a96" />
<img width="1902" height="799" alt="image" src="https://github.com/user-attachments/assets/538c1ddf-e0db-401d-8693-56e5f1227f57" />
<img width="1900" height="853" alt="image" src="https://github.com/user-attachments/assets/c5d67347-a3da-4d5f-8f1f-b20863b780ad" />
<img width="1133" height="865" alt="image" src="https://github.com/user-attachments/assets/f90435d7-86b7-4c25-9b1b-2cf4707d664e" />
<img width="1698" height="793" alt="image" src="https://github.com/user-attachments/assets/ac2c0b98-7f5f-428b-9d6b-cf68199c31ea" />
<img width="1284" height="817" alt="image" src="https://github.com/user-attachments/assets/7c9e3a74-1319-4277-958a-5153e733b226" />
<img width="1718" height="802" alt="image" src="https://github.com/user-attachments/assets/17e99c95-91b2-4202-a78b-0e637e2f9dff" />
<img width="579" height="709" alt="image" src="https://github.com/user-attachments/assets/3e29703c-df43-445c-94c1-2ab2b3733aa4" />
<img width="933" height="839" alt="image" src="https://github.com/user-attachments/assets/4ef4b9b6-b973-477f-af65-31a353a2573c" />



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
