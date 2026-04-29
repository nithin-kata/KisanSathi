"""
KisanSathi - Chat Component
Main AI chat interface with image upload support
"""

import streamlit as st
from utils.groq_client import get_ai_response


def _build_prompt(user_query: str, image_uploaded: bool, image_name: str = "") -> str:
    """Construct the full prompt, optionally incorporating image context."""
    if image_uploaded and image_name:
        return (
            f"I have uploaded an image named '{image_name}' showing a farming issue. "
            f"Please analyze this crop/field situation and answer my question: {user_query}"
        )
    return user_query


def render_chat_history():
    """Render all messages in the chat history."""
    history = st.session_state.get("chat_history", [])
    if not history:
        st.markdown(
            "<div style='text-align:center; padding:2rem 0; color:var(--text-muted); font-size:0.9rem;'>"
            "🌱 Ask me anything about your crops, soil, pests, or farming techniques!"
            "</div>",
            unsafe_allow_html=True,
        )
        return

    for msg in history:
        if msg["role"] == "user":
            st.markdown(
                f"<div class='ks-msg-user'>"
                f"<div class='ks-msg-label'>👨‍🌾 You</div>"
                f"{msg['content']}"
                f"</div>",
                unsafe_allow_html=True,
            )
        else:
            # Escape HTML in bot response to avoid injection, render newlines
            content = msg["content"].replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>")
            st.markdown(
                f"<div class='ks-msg-bot'>"
                f"<div class='ks-msg-label'>🌱 KisanSathi</div>"
                f"{content}"
                f"</div>",
                unsafe_allow_html=True,
            )


def render_chat_section():
    """Render the full chat card including input, upload, and history."""
    # Section header
    st.markdown("<div class='ks-section-label'>💬 Ask KisanSathi</div>", unsafe_allow_html=True)
    st.markdown("<hr class='ks-divider'>", unsafe_allow_html=True)

    # Chat card wrapper
    st.markdown("<div class='ks-chat-card'>", unsafe_allow_html=True)

    # ── Chat history ──
    st.markdown("<div class='ks-chat-history'>", unsafe_allow_html=True)
    render_chat_history()
    st.markdown("</div>", unsafe_allow_html=True)

    # ── Image upload (optional) ──
    st.markdown(
        "<div class='ks-upload-hint'>📸 Optional: Upload a photo of your crop or soil problem</div>",
        unsafe_allow_html=True,
    )
    uploaded_file = st.file_uploader(
        label="Upload crop/soil image",
        type=["jpg", "jpeg", "png", "webp"],
        label_visibility="collapsed",
        key="image_upload",
    )

    # ── Text input ──
    # Pre-fill if triggered from Experts or Farmers section
    default_query = st.session_state.pop("prefill_query", "")
    user_input = st.text_input(
        label="Your question",
        value=default_query,
        placeholder="e.g. My wheat leaves are turning yellow, what should I do?",
        label_visibility="collapsed",
        key="chat_input",
    )

    # ── Ask button ──
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        ask_clicked = st.button("🌾 Ask", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)  # close ks-chat-card

    # ── Handle submission ──
    if ask_clicked:
        query = user_input.strip()
        if not query:
            st.warning("Please enter your question before clicking Ask.")
            return

        # Build prompt (include image context if uploaded)
        image_name = uploaded_file.name if uploaded_file else ""
        final_prompt = _build_prompt(query, bool(uploaded_file), image_name)

        # Add user message to history
        st.session_state.setdefault("chat_history", []).append(
            {"role": "user", "content": query + (" 📸 [image attached]" if uploaded_file else "")}
        )

        # Get AI response
        with st.spinner("KisanSathi is thinking… 🌱"):
            response = get_ai_response(final_prompt)

        # Add bot response to history
        st.session_state["chat_history"].append(
            {"role": "assistant", "content": response}
        )

        # Rerun to refresh chat display and clear input
        st.rerun()
