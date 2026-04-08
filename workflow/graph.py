from langgraph.graph import StateGraph, END
from core.state import AgentState
from nodes.intent_analyzer import intent_analyzer
from core.divination import divination_tool
from nodes.strategist import academic_strategist
from nodes.polisher import tone_polisher


def create_workflow() -> StateGraph:
    """创建并配置 LangGraph 工作流图"""
    # 创建工作流图
    graph = StateGraph(AgentState)

    # 添加四个节点
    graph.add_node("intent_analyzer", intent_analyzer)
    graph.add_node("divination_tool", divination_tool)
    graph.add_node("academic_strategist", academic_strategist)
    graph.add_node("tone_polisher", tone_polisher)

    # 设置节点连接顺序：A -> B -> C -> D -> END
    graph.set_entry_point("intent_analyzer")
    graph.add_edge("intent_analyzer", "divination_tool")
    graph.add_edge("divination_tool", "academic_strategist")
    graph.add_edge("academic_strategist", "tone_polisher")
    graph.add_edge("tone_polisher", END)

    return graph


# 编译为可执行应用
app_graph = create_workflow().compile()


def run_oracle(query: str) -> dict:
    """
    对外暴露的极简入口函数。
    传入用户焦虑文本，返回包含完整结果的字典。
    """
    initial_state: AgentState = {
        "user_query": query,
        "academic_intent": "",
        "hexagram_raw": {},
        "draft_strategy": "",
        "final_output": "",
    }

    result = app_graph.invoke(initial_state)
    return {
        "intent": result["academic_intent"],
        "hexagram": result["hexagram_raw"],
        "strategy": result["draft_strategy"],
        "final": result["final_output"],
        "full_state": result,
    }