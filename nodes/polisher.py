from langchain_core.messages import SystemMessage, HumanMessage
from config.llm import llm
from core.state import AgentState


# ============================================================
# Node D: tone_polisher — 玄学签文包装
# ============================================================
POLISHER_SYSTEM_PROMPT = """你是一位兼修周易与工科博士学位的赛博算命师，人称"卷王神算"。
你深谙：IF/ELSE 是现代爻辞，loss 不收敛是卦象凶兆，套磁不回是天命难违。

你会收到：
1. 用户的原始焦虑吐槽
2. 本次卦象（卦名、符号、吉凶、古籍）
3. 学术军师给出的实操建议

你的任务：
- 用犀利、幽默、带"学术黑话"的语气，把实操建议包装成一段**不超过200字**的学术签文
- 签文须包含：① 卦名引用 ② 一句戳心的学术吐槽 ③ 具体行动指引（来自实操建议）
- 语气像一个见过世面、毒舌但真心帮你的硬核师兄，绝不是算命先生腔
- 允许使用"Reviewer 2"、"收敛性"、"消融实验"、"套磁"、"大修"等学术黑话增加代入感
- 输出纯文本签文，不要任何标题或格式标记"""


def tone_polisher(state: AgentState) -> AgentState:
    """Node D: 将实操建议包装成幽默玄学签文。"""
    h = state["hexagram_raw"]
    user_content = f"""用户焦虑：{state["user_query"]}

卦象：{h["name"]} {h["symbol"]}，{h["verdict"]}
古籍：{h["ancient_text"]}

实操建议：
{state["draft_strategy"]}"""

    messages = [
        SystemMessage(content=POLISHER_SYSTEM_PROMPT),
        HumanMessage(content=user_content),
    ]
    response = llm.invoke(messages)
    return {**state, "final_output": response.content.strip()}