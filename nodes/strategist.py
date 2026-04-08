from langchain_core.messages import SystemMessage, HumanMessage
from config.llm import llm
from core.state import AgentState


# ============================================================
# Node C: academic_strategist — 硬核学术实操建议
# ============================================================
STRATEGIST_SYSTEM_PROMPT = """你是一位同时精通学术硬核和江湖谋略的博士师兄，发过顶刊、熬过死线、拒过 Reviewer 2 的无理要求。
你会收到两样东西：
1. 用户当前的学术焦虑类型
2. 本次起卦的卦象信息（含卦名、吉凶、古籍原文、学术提示）

你的任务：
- 完全无视卦象的玄学包装，只参考其中的"学术提示"字段作为隐喻灵感
- 输出 3 条极具实操性的学术建议，每条以"• "开头
- 建议必须具体可执行（如：重新检查消融实验、修改 Cover Letter 第二段措辞），绝不说废话
- 语气简洁、专业，像一个不废话的学长在咖啡馆给你指路
- 严禁出现任何玄学、风水、命运之类的词汇，这一步是纯理性分析"""


def academic_strategist(state: AgentState) -> AgentState:
    """Node C: 结合意图与卦象，给出硬核实操学术建议。"""
    user_content = f"""焦虑类型：{state["academic_intent"]}

卦象信息：
- 卦名：{state["hexagram_raw"]["name"]}
- 吉凶：{state["hexagram_raw"]["verdict"]}
- 主题：{state["hexagram_raw"]["theme"]}
- 古籍原文：{state["hexagram_raw"]["ancient_text"]}
- 学术提示：{state["hexagram_raw"]["academic_hint"]}"""

    messages = [
        SystemMessage(content=STRATEGIST_SYSTEM_PROMPT),
        HumanMessage(content=user_content),
    ]
    response = llm.invoke(messages)
    return {**state, "draft_strategy": response.content.strip()}