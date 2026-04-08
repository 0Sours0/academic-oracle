import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Support both local .env and Streamlit Cloud Secrets
try:
    import streamlit as st
    api_key = st.secrets.get("DEEPSEEK_API_KEY") or os.getenv("DEEPSEEK_API_KEY")
except Exception:
    api_key = os.getenv("DEEPSEEK_API_KEY")

# ============================================================
# LLM 初始化 (DeepSeek via OpenAI-compatible API)
# ============================================================
llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=api_key,
    base_url="https://api.deepseek.com",
    temperature=0.7,
    max_tokens=512,
)