
---

```markdown
# 🔮 学术赛博算命 (Academic Oracle) - AI 开发系统指令

## 1. 项目概述 (Project Context)
你现在是一位资深的 Python 全栈工程师和 AI Agent 架构师。我们需要开发一款面向硕博研究生和青年学者的“学术情绪安抚与决策辅助工具”。
该产品将中国传统的“六爻占卜”与大模型分析相结合，用户输入学术焦虑（如：发顶刊、申基金、套磁），系统通过 LangGraph 多智能体工作流，输出带有“赛博算命”包装的专业学术实操建议。

### 技术栈 (Tech Stack)
- **前端:** Streamlit (极致轻量化，无定制 CSS 要求)
- **后端框架:** LangGraph, Langchain-OpenAI
- **大模型 API:** DeepSeek-Chat (完全兼容 OpenAI 接口)
- **环境配置:** python-dotenv

---

## 2. 目录结构 (Directory Structure)
请按照以下极简结构构建项目，不要过度设计：
```text
academic_oracle/
├── .env                # 环境变量 (存储 DEEPSEEK_API_KEY)
├── .gitignore          # 忽略 venv 和 .env
├── requirements.txt    # 依赖清单
├── engine.py           # 核心后端：包含排盘算法与 LangGraph 图结构
└── app.py              # 前端界面：Streamlit 交互逻辑
```

---

## 3. 核心架构设计 (Architecture: LangGraph)

### 3.1 状态定义 (Agent State)
在 `engine.py` 中，定义全局状态字典 `AgentState`：
- `user_query` (str): 用户的原始输入。
- `academic_intent` (str): 意图分类（如：投稿、导学关系、实验、找工作等）。
- `hexagram_raw` (dict): Python 生成的卦象数据（包含卦名、基本吉凶、古籍释义）。
- `draft_strategy` (str): 学术军师 Agent 结合卦象给出的纯硬核学术建议。
- `final_output` (str): 包装成玄学口吻的最终幽默签文。

### 3.2 节点定义 (Nodes)
系统包含 4 个核心节点（3个 LLM 节点，1个普通 Tool 节点）：
1. **Node A: intent_analyzer (LLM)**
   - 输入：`user_query`
   - 任务：精准识别用户的学术痛点场景，输出简短分类词。
2. **Node B: divination_tool (Python Function)**
   - 任务：根据当前时间戳生成一个伪随机的六爻本卦。
   - 要求：由于是 MVP，请在代码中硬编码一个包含 8-10 个常见学术卦象的微型字典（如：屯卦=初期艰难/数据不跑，升卦=顺利/适宜投递），从中随机抽取并返回。
3. **Node C: academic_strategist (LLM)**
   - 输入：`academic_intent` + `hexagram_raw`
   - 任务：忽略玄学用语，给出 3 条极具实操性的学术建议（如：检查多源数据融合算法的收敛性，优化 Cover Letter）。
4. **Node D: tone_polisher (LLM)**
   - 输入：`user_query` + `draft_strategy` + `hexagram_raw`
   - 任务：扮演一位懂周易的硬核理工科博士师兄，用犀利、幽默、带点“学术黑话”的语气，把实操建议包装成不超过 200 字的签文。

---

## 4. AI 执行步骤 (Step-by-Step Execution Plan)
⚠️ **注意：请不要一次性生成所有代码！请严格按照以下 Phase 逐一向我确认，完成一个再进行下一个。**

### Phase 1: 基础设施搭建
1. 生成 `requirements.txt`。
2. 编写 `.env.example` 模板。
3. 在 `engine.py` 中，定义 `AgentState` 的 `TypedDict`，并写好 Node B (`divination_tool`) 的纯 Python 占卜模拟函数。

### Phase 2: LangGraph 节点与 Prompt 编写
1. 在 `engine.py` 中，初始化 `ChatOpenAI` (使用 DeepSeek 配置)。
2. 编写 Node A, Node C, Node D 的执行函数。
3. 为这三个节点编写极度精准的 System Prompt。**语气必须符合高压科研环境，带点黑色幽默，熟知 Reviewer 2、跑模型、套磁等梗。**

### Phase 3: 工作流组装与测试
1. 在 `engine.py` 中，使用 `StateGraph` 将上述 4 个节点连成工作流（A->B->C->D），并编译为 `app_graph`。
2. 暴露一个简单的入口函数 `run_oracle(query: str) -> dict` 供前端调用。

### Phase 4: Streamlit 前端开发
1. 在 `app.py` 中，实现极简 UI。
2. 包含：霸气的标题、一条输入框（“说出你的学术焦虑”）、一个“焚香起卦”按钮。
3. 点击按钮后，必须使用 `st.spinner("正在请示学术祖师爷与图灵神明...")`。
4. 调用 `engine.py` 的 `run_oracle` 函数。
5. 成功后，使用 Streamlit 的 Markdown 优美地展示 `final_output`。

---

## 5. 开发约束 (Crucial Constraints)
- **拒绝幻觉：** 占卜逻辑必须依赖 Node B 的 Python 硬编码，绝不能让 LLM 凭空捏造卦象。
- **状态管理：** Streamlit 每次按钮点击会重新加载页面，请谨慎使用 `st.session_state` 防止算出的结果消失。
- **无复杂前端：** 不要手写任何 CSS 或 JS，只用 Streamlit 的原生组件（`st.write`, `st.button`, `st.success` 等）。
```

---
