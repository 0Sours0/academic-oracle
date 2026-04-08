import random
from datetime import datetime
from typing import Dict, Any
from .state import AgentState, HEXAGRAM_DICT


def divination_tool(state: AgentState) -> AgentState:
    """
    Node B: 根据当前时间戳生成伪随机六爻卦象。
    纯 Python 实现，结果完全可复现，不依赖 LLM。
    """
    seed = int(datetime.now().timestamp())
    random.seed(seed)
    hexagram_name = random.choice(list(HEXAGRAM_DICT.keys()))
    hexagram_data = HEXAGRAM_DICT[hexagram_name].copy()
    hexagram_data["name"] = hexagram_name

    return {**state, "hexagram_raw": hexagram_data}