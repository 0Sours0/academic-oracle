"""
节点模块：包含 LangGraph 工作流的各个节点。
"""
from .intent_analyzer import intent_analyzer, INTENT_SYSTEM_PROMPT
from .strategist import academic_strategist, STRATEGIST_SYSTEM_PROMPT
from .polisher import tone_polisher, POLISHER_SYSTEM_PROMPT

__all__ = [
    "intent_analyzer",
    "INTENT_SYSTEM_PROMPT",
    "academic_strategist",
    "STRATEGIST_SYSTEM_PROMPT",
    "tone_polisher",
    "POLISHER_SYSTEM_PROMPT",
]