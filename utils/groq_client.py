"""
KisanSathi - Groq API Client
Handles all interactions with the Groq LLM API
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# System prompt for the agriculture advisor persona
SYSTEM_PROMPT = """You are KisanSathi, an expert agriculture advisor for Indian farmers. 
Your role is to help farmers with practical, actionable advice.

Guidelines:
- Use simple, clear language that farmers can easily understand
- Focus on LOW-COST, LOCALLY AVAILABLE solutions
- Mention specific Indian crop names, fertilizers, and techniques when relevant
- Consider Indian seasons (Kharif, Rabi, Zaid) and regional climates
- Recommend government schemes (PM-Kisan, soil health card, etc.) when appropriate
- Keep responses concise — 3 to 5 short paragraphs max
- Use bullet points for step-by-step instructions
- Be warm, encouraging, and respectful
- If an image is described, address those specific visual concerns
- Always end with one encouraging line for the farmer"""


def get_groq_client() -> Groq:
    """Initialize and return a Groq client using API key from environment."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found. Please add it to your .env file."
        )
    return Groq(api_key=api_key)


def get_ai_response(prompt: str) -> str:
    """
    Send a prompt to Groq and return the AI response.
    
    Args:
        prompt: The user's question or query (may include image context)
    
    Returns:
        AI-generated response string, or an error message
    """
    if not prompt or not prompt.strip():
        return "Please enter a question so I can help you! 🌱"

    try:
        client = get_groq_client()
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": prompt.strip()},
            ],
            model="llama-3.1-8b-instant",
            temperature=0.65,
            max_tokens=900,
        )
        return chat_completion.choices[0].message.content
    except ValueError as e:
        return f"⚠️ Configuration error: {e}"
    except Exception as e:
        err = str(e).lower()
        if "rate limit" in err:
            return "⏳ Too many requests right now. Please wait a moment and try again."
        elif "authentication" in err or "api key" in err:
            return "🔑 Invalid API key. Please check your GROQ_API_KEY in the .env file."
        elif "connection" in err or "network" in err:
            return "📡 Network issue. Please check your internet connection and try again."
        else:
            return f"❌ Something went wrong: {e}\n\nPlease try again."
