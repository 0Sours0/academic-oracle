from langchain_core.messages import SystemMessage, HumanMessage
from config.llm import llm
from core.state import AgentState


# ============================================================
# Node A: intent_analyzer — 识别学术痛点意图
# ============================================================
INTENT_SYSTEM_PROMPT = """你是一位在高压科研环境中摸爬滚打多年的学术老油条。
你的任务是精准识别研究生的学术焦虑类型，输出一个简短的分类词（不超过10个汉字）。

可选类别如下（选最匹配的一个，或自行概括）：
- 投稿/审稿
- 导学关系
- 实验/数据
- 套磁/申请
- 基金申请
- 毕业/答辩
- 找工作/求职
- 科研焦虑

规则：
1. 只输出分类词本身，不要任何解释、标点或额外文字。
2. 例：用户说"Reviewer 2 把我审哭了" → 输出：投稿/审稿
3. 例：用户说"导师让我重复劳动半年" → 输出：导学关系"""


def intent_analyzer(state: AgentState) -> AgentState:
    """Node A: 识别用户学术焦虑的意图类型。"""
    messages = [
        SystemMessage(content=INTENT_SYSTEM_PROMPT),
        HumanMessage(content=state["user_query"]),
    ]
    response = llm.invoke(messages)
    return {**state, "academic_intent": response.content.strip()}