import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# ============================================================
# LLM 初始化 (DeepSeek via OpenAI-compatible API)
# ============================================================
llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    temperature=0.7,
    max_tokens=512,
)