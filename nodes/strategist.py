from langchain_core.messages import SystemMessage, HumanMessage
from config.llm import llm
from core.state import AgentState


# ============================================================
# Node C: academic_strategist — 硬核学术实操建议
# ============================================================
STRATEGIST_SYSTEM_PROMPT = """你是一位经历过顶刊大修、导师PUA、基金被毙、套磁石沉的博士师兄，现在终于熬出来了。
你会收到三样东西：
1. 用户的原始吐槽（这是最重要的，必须认真读）
2. 焦虑类型（辅助定向）
3. 一条卦象学术提示（只用来做灵感暗语，不要提玄学）

你的任务：
- 针对用户说的**具体情况**给出 3 条实操建议，每条以"• "开头
- 每条建议必须直接回应用户描述的问题，不能是泛泛的"坚持下去"或"多沟通"
- 建议要具体到可以立刻行动：比如"在 rebuttal 第二段直接列出实验数据反驳 Reviewer 2 第3条意见"
- 语气像一个靠谱的师兄，简洁直接，不废话，不鸡汤
- 严禁任何玄学词汇，这里是纯理性分析"""


def academic_strategist(state: AgentState) -> AgentState:
    """Node C: 结合用户具体情况与卦象，给出硬核实操学术建议。"""
    user_content = f"""用户原话：{state["user_query"]}

焦虑类型：{state["academic_intent"]}

卦象学术提示（仅供灵感参考）：{state["hexagram_raw"]["academic_hint"]}"""

    messages = [
        SystemMessage(content=STRATEGIST_SYSTEM_PROMPT),
        HumanMessage(content=user_content),
    ]
    response = llm.invoke(messages)
    return {**state, "draft_strategy": response.content.strip()}