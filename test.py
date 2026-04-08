import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 1. 加载 .env 文件中的环境变量
load_dotenv()

# 2. 读取 DeepSeek API Key
deepseek_key = os.getenv("DEEPSEEK_API_KEY")

if not deepseek_key:
    print("❌ 错误：未找到 DEEPSEEK_API_KEY！请检查 .env 文件是否配置正确。")
    exit()

print("✅ 成功读取 API Key，正在向 DeepSeek 发送学术召唤阵...")

# 3. 初始化大模型 (利用 OpenAI 的兼容接口调用 DeepSeek)
try:
    llm = ChatOpenAI(
        model="deepseek-chat",               # DeepSeek V3 的标准模型名称
        api_key=deepseek_key,                # 传入你的 Key
        base_url="https://api.deepseek.com", # 关键：将请求地址指向 DeepSeek 的服务器
        max_tokens=150,                      # 限制一下输出长度，省点 token
        temperature=0.7                      # 稍微给一点创造力，让说话更有趣
    )

    # 4. 发送测试指令
    prompt = "你好！请用一句简短的话证明你是一位既懂硬核岩土工程，又精通易经算命的博士师兄。"
    
    # 5. 获取结果
    response = llm.invoke(prompt)
    
    print("\n=================================")
    print("🔮 DeepSeek 师兄的回复：")
    print("---------------------------------")
    print(response.content)
    print("=================================\n")
    print("🎉 测试成功！你的大模型接口已经完全打通，可以开始构建 LangGraph 节点了！")

except Exception as e:
    print("\n❌ 召唤失败，请检查网络或 API Key 余额。报错信息如下：")
    print(e)
