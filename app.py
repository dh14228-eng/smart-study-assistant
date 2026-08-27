"""
Smart Study Assistant - AI-Powered Learning Application
Bilingual Edition (Arabic & English) with RTL / LTR layout and automatic language detection.
"""

import os
from typing import Optional, Tuple
import streamlit as st
from dotenv import load_dotenv
from translations import TRANSLATIONS

# Load environment variables from .env file if present
load_dotenv()

# =====================================================================
# Configuration & Page Setup
# =====================================================================
st.set_page_config(
    page_title="Smart Study Assistant | المساعد الدراسي الذكي",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================================
# Language Selection & Layout Direction (RTL / LTR)
# =====================================================================
if "app_language" not in st.session_state:
    st.session_state["app_language"] = "English"

# Render sidebar language selector first to determine layout
with st.sidebar:
    selected_language = st.selectbox(
        "🌐 Language / اللغة",
        ["English", "العربية"],
        index=0 if st.session_state["app_language"] == "English" else 1,
        key="app_language_selector"
    )
    st.session_state["app_language"] = selected_language

current_lang = st.session_state["app_language"]
t = TRANSLATIONS[current_lang]
is_rtl = (current_lang == "العربية")

# Clean, stable CSS for RTL / LTR layout
if is_rtl:
    st.markdown(
        """
        <style>
            .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], .stMarkdown {
                direction: rtl;
                text-align: right;
            }
            .stSelectbox, .stRadio, .stTextArea, .stTextInput, .stSlider {
                direction: rtl;
                text-align: right;
            }
            .stButton>button {
                direction: rtl;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
            .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], .stMarkdown {
                direction: ltr;
                text-align: left;
            }
            .stSelectbox, .stRadio, .stTextArea, .stTextInput, .stSlider {
                direction: ltr;
                text-align: left;
            }
            .stButton>button {
                direction: ltr;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

# =====================================================================
# State Initialization (Persistent Across Reruns)
# =====================================================================
if "qa_result" not in st.session_state:
    st.session_state["qa_result"] = ""
if "qa_warning" not in st.session_state:
    st.session_state["qa_warning"] = ""

if "summary_result" not in st.session_state:
    st.session_state["summary_result"] = ""
if "summary_warning" not in st.session_state:
    st.session_state["summary_warning"] = ""

if "explain_result" not in st.session_state:
    st.session_state["explain_result"] = ""
if "explain_warning" not in st.session_state:
    st.session_state["explain_warning"] = ""

if "quiz_result" not in st.session_state:
    st.session_state["quiz_result"] = ""
if "quiz_warning" not in st.session_state:
    st.session_state["quiz_warning"] = ""


# =====================================================================
# Helper & Security Functions
# =====================================================================
def get_api_config() -> Tuple[Optional[str], str, str]:
    """
    Retrieve API key, base URL, and provider name securely.
    Supports standard OpenAI keys, OpenRouter keys (sk-or-v1-...), and custom endpoints.
    """
    env_key = os.getenv("OPENAI_API_KEY")
    key = env_key.strip() if (env_key and env_key.strip()) else None
    
    if not key:
        session_key = st.session_state.get("user_openai_api_key", "")
        if session_key and session_key.strip():
            key = session_key.strip()

    custom_base_url = os.getenv("OPENAI_BASE_URL")
    if custom_base_url and custom_base_url.strip():
        return key, custom_base_url.strip(), "Custom"
    
    if key and key.startswith("sk-or-"):
        return key, "https://openrouter.ai/api/v1", "OpenRouter"
    
    return key, "https://api.openai.com/v1", "OpenAI"


def validate_input(text: str, max_chars: int = 8000, field_name: str = "Input") -> Tuple[bool, str]:
    """
    Validate and sanitize user input.
    Ensures input is non-empty and does not exceed maximum character limits.
    """
    if not text or not text.strip():
        return False, t["warn_empty"].format(field_name=field_name)
    
    cleaned = text.strip()
    if len(cleaned) > max_chars:
        return False, t["warn_too_long"].format(field_name=field_name, count=len(cleaned), max_chars=max_chars)
    
    return True, cleaned


def call_openai_api(
    prompt: str,
    system_prompt: str = "",
    model: str = "gpt-4o-mini",
    temperature: float = 0.5,
    max_tokens: int = 1500
) -> str:
    """
    Safely invokes the AI API using openai client with multilingual awareness and error handling.
    """
    api_key, base_url, provider = get_api_config()
    if not api_key:
        return t["err_api_missing"]

    # Base system instructions with strict language matching
    base_instructions = (
        "You are Smart Study Assistant (المساعد الدراسي الذكي), an expert, encouraging, and accurate academic tutor.\n"
        "LANGUAGE RULE: Detect the language of the user's input/content. "
        "If the input is primarily in Arabic, respond in fluent, grammatically correct Modern Standard Arabic (العربية الفصحى) "
        "using proper Arabic formatting and terminology. If the input is in English, respond in clear English. "
        "Always maintain clarity, educational value, and structured markdown output."
    )
    full_system_prompt = f"{base_instructions}\n\n{system_prompt}" if system_prompt else base_instructions

    # Format model name for OpenRouter if needed
    effective_model = model
    if provider == "OpenRouter":
        if model in ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"]:
            effective_model = f"openai/{model}"

    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key, base_url=base_url)
        
        response = client.chat.completions.create(
            model=effective_model,
            messages=[
                {"role": "system", "content": full_system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content or "No response received."
    except Exception as e:
        err_msg = str(e)
        if "AuthenticationError" in err_msg or "invalid_api_key" in err_msg or "401" in err_msg:
            return t["err_auth_failed"].format(provider=provider)
        elif "RateLimitError" in err_msg or "429" in err_msg:
            return t["err_rate_limit"]
        elif "quota" in err_msg.lower() or "402" in err_msg:
            return t["err_quota"].format(provider=provider)
        else:
            clean_err = err_msg.split(' - ')[-1] if ' - ' in err_msg else err_msg
            return t["err_generic"].format(msg=clean_err)


# =====================================================================
# Sidebar Navigation & Settings
# =====================================================================
with st.sidebar:
    st.divider()
    st.title(t["sidebar_title"])
    st.caption(t["sidebar_caption"])
    
    # Feature selector
    feature_options = [
        t["nav_qa"],
        t["nav_summary"],
        t["nav_explain"],
        t["nav_quiz"]
    ]
    
    feature = st.radio(
        t["nav_label"],
        feature_options,
        index=0,
        key="sidebar_navigation_radio"
    )
    
    st.divider()
    st.subheader(t["settings_header"])
    
    loaded_key, active_base_url, active_provider = get_api_config()
    
    if loaded_key:
        st.success(t["api_key_active"].format(provider=active_provider))
    else:
        user_key = st.text_input(
            t["api_key_label"],
            type="password",
            placeholder=t["api_key_placeholder"],
            key="user_manual_api_key_input",
            help=t["api_key_help"]
        )
        if user_key:
            st.session_state["user_openai_api_key"] = user_key
            st.success(t["api_key_stored"])
        else:
            st.info(t["api_key_missing_info"])
            
    if active_provider == "OpenRouter":
        model_options = ["gpt-4o-mini", "gpt-4o", "google/gemini-2.5-flash", "anthropic/claude-3.5-haiku", "meta-llama/llama-3.3-70b-instruct"]
    else:
        model_options = ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"]

    model_choice = st.selectbox(
        t["model_label"],
        model_options,
        index=0,
        key="model_selector_dropdown",
        help=t["model_help"]
    )
    
    st.divider()
    st.caption(t["version_info"])


# =====================================================================
# Main Header
# =====================================================================
st.title(t["app_title"])
st.caption(t["app_caption"])


# =====================================================================
# Feature 1: Academic Q&A
# =====================================================================
if feature == t["nav_qa"]:
    st.header(t["qa_header"])
    st.write(t["qa_desc"])

    col1, col2 = st.columns([2, 1])
    with col1:
        subject = st.selectbox(
            t["qa_subject_label"],
            t["qa_subjects"],
            key="qa_subject_field"
        )
    with col2:
        depth = st.selectbox(
            t["qa_depth_label"],
            t["qa_depths"],
            key="qa_depth_field"
        )

    question_text = st.text_area(
        t["qa_input_label"],
        placeholder=t["qa_input_placeholder"],
        height=140,
        key="qa_question_input"
    )

    if st.button(t["qa_button"], type="primary", use_container_width=True, key="qa_submit_button"):
        valid, result = validate_input(question_text, max_chars=4000, field_name=t["qa_field_name"])
        if not valid:
            st.session_state["qa_warning"] = result
            st.session_state["qa_result"] = ""
        else:
            st.session_state["qa_warning"] = ""
            system_prompt = (
                f"Subject: {subject}. Explanation Style: {depth}. "
                "Provide a well-structured, clear, and encouraging explanation with examples or notation where appropriate."
            )
            user_prompt = f"Subject / المادة: {subject}\n\nQuestion / السؤال:\n{result}"
            st.session_state["qa_result"] = call_openai_api(user_prompt, system_prompt=system_prompt, model=model_choice)

    if st.session_state["qa_warning"]:
        st.warning(st.session_state["qa_warning"])

    if st.session_state["qa_result"]:
        st.subheader(t["qa_result_title"])
        st.markdown(st.session_state["qa_result"])


# =====================================================================
# Feature 2: Summarize Study Notes
# =====================================================================
elif feature == t["nav_summary"]:
    st.header(t["summary_header"])
    st.write(t["summary_desc"])

    col1, col2 = st.columns(2)
    with col1:
        summary_format = st.selectbox(
            t["summary_format_label"],
            t["summary_formats"],
            key="summary_format_field"
        )
    with col2:
        length_preference = st.select_slider(
            t["summary_length_label"],
            options=t["summary_lengths"],
            value=t["summary_lengths"][1],
            key="summary_length_field"
        )

    notes_text = st.text_area(
        t["summary_input_label"],
        placeholder=t["summary_input_placeholder"],
        height=200,
        key="summary_notes_input"
    )

    if st.button(t["summary_button"], type="primary", use_container_width=True, key="summary_submit_button"):
        valid, result = validate_input(notes_text, max_chars=8000, field_name=t["summary_field_name"])
        if not valid:
            st.session_state["summary_warning"] = result
            st.session_state["summary_result"] = ""
        else:
            st.session_state["summary_warning"] = ""
            system_prompt = (
                f"Format: {summary_format}. Length: {length_preference}. "
                "Extract the most critical definitions, insights, and core principles."
            )
            user_prompt = f"Please summarize the following content / يرجى تلخيص المحتوى التالي:\n\n{result}"
            st.session_state["summary_result"] = call_openai_api(user_prompt, system_prompt=system_prompt, model=model_choice)

    if st.session_state["summary_warning"]:
        st.warning(st.session_state["summary_warning"])

    if st.session_state["summary_result"]:
        st.subheader(t["summary_result_title"])
        st.markdown(st.session_state["summary_result"])


# =====================================================================
# Feature 3: Explain Difficult Concepts
# =====================================================================
elif feature == t["nav_explain"]:
    st.header(t["explain_header"])
    st.write(t["explain_desc"])

    col1, col2 = st.columns(2)
    with col1:
        concept_name = st.text_input(
            t["explain_concept_label"],
            placeholder=t["explain_concept_placeholder"],
            key="explain_concept_field"
        )
    with col2:
        target_audience = st.selectbox(
            t["explain_audience_label"],
            t["explain_audiences"],
            key="explain_audience_field"
        )

    extra_context = st.text_area(
        t["explain_context_label"],
        placeholder=t["explain_context_placeholder"],
        height=100,
        key="explain_context_field"
    )

    if st.button(t["explain_button"], type="primary", use_container_width=True, key="explain_submit_button"):
        valid, result = validate_input(concept_name, max_chars=500, field_name=t["explain_field_name"])
        if not valid:
            st.session_state["explain_warning"] = result
            st.session_state["explain_result"] = ""
        else:
            st.session_state["explain_warning"] = ""
            system_prompt = (
                f"Target Audience / Level: {target_audience}. "
                "Use relatable analogies, break down steps intuitively, and include a clear Key Takeaway / الخلاصة."
            )
            user_prompt = f"Concept / المفهوم: {result}\n"
            if extra_context and extra_context.strip():
                user_prompt += f"Context / السياق: {extra_context.strip()}\n"
            
            st.session_state["explain_result"] = call_openai_api(user_prompt, system_prompt=system_prompt, model=model_choice)

    if st.session_state["explain_warning"]:
        st.warning(st.session_state["explain_warning"])

    if st.session_state["explain_result"]:
        st.subheader(t["explain_result_title"])
        st.markdown(st.session_state["explain_result"])


# =====================================================================
# Feature 4: Quiz & Question Generator
# =====================================================================
elif feature == t["nav_quiz"]:
    st.header(t["quiz_header"])
    st.write(t["quiz_desc"])

    col1, col2, col3 = st.columns(3)
    with col1:
        quiz_type = st.selectbox(
            t["quiz_type_label"],
            t["quiz_types"],
            key="quiz_type_field"
        )
    with col2:
        num_questions = st.selectbox(t["quiz_num_label"], [3, 5, 8, 10], index=1, key="quiz_num_field")
    with col3:
        difficulty = st.selectbox(t["quiz_diff_label"], t["quiz_diffs"], index=1, key="quiz_diff_field")

    quiz_source = st.text_area(
        t["quiz_input_label"],
        placeholder=t["quiz_input_placeholder"],
        height=160,
        key="quiz_source_field"
    )

    if st.button(t["quiz_button"], type="primary", use_container_width=True, key="quiz_submit_button"):
        valid, result = validate_input(quiz_source, max_chars=6000, field_name=t["quiz_field_name"])
        if not valid:
            st.session_state["quiz_warning"] = result
            st.session_state["quiz_result"] = ""
        else:
            st.session_state["quiz_warning"] = ""
            system_prompt = (
                f"Quiz Format: {quiz_type}. Questions Count: {num_questions}. Difficulty: {difficulty}. "
                "Format each question clearly. Always provide correct answers and explanations."
            )
            user_prompt = f"Study Content / المحتوى الدراسي:\n{result}"
            st.session_state["quiz_result"] = call_openai_api(user_prompt, system_prompt=system_prompt, model=model_choice)

    if st.session_state["quiz_warning"]:
        st.warning(st.session_state["quiz_warning"])

    if st.session_state["quiz_result"]:
        st.subheader(t["quiz_result_title"])
        st.markdown(st.session_state["quiz_result"])


# =====================================================================
# Footer
# =====================================================================
st.divider()
st.caption(t["footer_text"])
