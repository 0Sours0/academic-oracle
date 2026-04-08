from typing import TypedDict


# ============================================================
# 全局状态定义 (Agent State)
# ============================================================
class AgentState(TypedDict):
    user_query: str        # 用户的原始输入
    academic_intent: str   # 意图分类（如：投稿、导学关系、实验、找工作）
    hexagram_raw: dict     # 卦象数据（卦名、吉凶、古籍释义）
    draft_strategy: str    # 学术军师给出的硬核实操建议
    final_output: str      # 包装成玄学口吻的最终幽默签文


# ============================================================
# 硬编码的学术卦象微型字典（8 卦）
# ============================================================
HEXAGRAM_DICT = {
    "屯卦": {
        "symbol": "☳☵",
        "verdict": "凶中带吉",
        "theme": "初期艰难，数据跑不动",
        "ancient_text": "屯，刚柔始交而难生。动乎险中，大亨贞。",
        "academic_hint": "当前处于项目初期最困难阶段，坚持即是胜利。",
    },
    "升卦": {
        "symbol": "☴☷",
        "verdict": "大吉",
        "theme": "扶摇直上，适宜投递",
        "ancient_text": "升，元亨，用见大人，勿恤，南征吉。",
        "academic_hint": "时机成熟，适合提交论文或发出申请。",
    },
    "困卦": {
        "symbol": "☵☱",
        "verdict": "凶",
        "theme": "Reviewer 2 刁难，陷入泥沼",
        "ancient_text": "困，亨，贞，大人吉，无咎。有言不信。",
        "academic_hint": "当前处于被围困状态，需要多方寻求突破口。",
    },
    "井卦": {
        "symbol": "☵☴",
        "verdict": "中平",
        "theme": "积累深耕，坚持挖掘",
        "ancient_text": "井，改邑不改井，无丧无得，往来井井。",
        "academic_hint": "根基尚在，需要持续积累，勿轻易放弃方向。",
    },
    "革卦": {
        "symbol": "☱☲",
        "verdict": "吉",
        "theme": "推倒重来，方法需变革",
        "ancient_text": "革，己日乃孚，元亨利贞，悔亡。",
        "academic_hint": "现有方法已到瓶颈，适合大胆转换技术路线。",
    },
    "讼卦": {
        "symbol": "☰☵",
        "verdict": "凶",
        "theme": "与导师意见相左，内耗严重",
        "ancient_text": "讼，有孚，窒，惕，中吉，终凶。",
        "academic_hint": "正面冲突不利，建议迂回沟通，用数据说话。",
    },
    "既济卦": {
        "symbol": "☵☲",
        "verdict": "大吉",
        "theme": "大功告成，适合收尾提交",
        "ancient_text": "既济，亨小，利贞，初吉终乱。",
        "academic_hint": "主体工作已完成，当前最适合整理收尾并提交。",
    },
    "未济卦": {
        "symbol": "☲☵",
        "verdict": "中平",
        "theme": "尚未完成，曙光在前",
        "ancient_text": "未济，亨，小狐汔济，濡其尾，无攸利。",
        "academic_hint": "距离终点尚有一步之遥，切忌此刻松懈。",
    },
}