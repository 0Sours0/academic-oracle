import streamlit as st
import sys
import os

# 确保当前目录在路径中，以便导入 engine 模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from engine import run_oracle

# ============================================================
# 页面配置
# ============================================================
st.set_page_config(
    page_title="学术赛博算命 | Academic Oracle",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ============================================================
# 初始化 session_state
# ============================================================
if "result" not in st.session_state:
    st.session_state.result = None
if "query" not in st.session_state:
    st.session_state.query = ""

# ============================================================
# 标题区
# ============================================================
st.markdown(
    """
    <h1 style='text-align: center;'>
        🔮 学术赛博算命<br>
        <span style='font-size: 0.6em; color: #888;'>
            Academic Oracle — 焦虑转化器 · 硬核玄学 · Reviewer 2 克星
        </span>
    </h1>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# ============================================================
# 输入区
# ============================================================
st.markdown("### 📝 说出你的学术焦虑")
user_input = st.text_area(
    "例如：论文被拒、实验不收敛、导师PUA、基金申不上、套磁石沉大海...",
    value=st.session_state.query,
    height=120,
    key="input_area",
    placeholder="在此处详细描述你的科研困境，越具体越好...",
)

# ============================================================
# 起卦按钮
# ============================================================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    button_clicked = st.button(
        "🔥 焚香起卦",
        type="primary",
        use_container_width=True,
        disabled=not user_input.strip(),
    )

st.markdown("---")

# ============================================================
# 处理起卦请求
# ============================================================
if button_clicked and user_input.strip():
    st.session_state.query = user_input
    st.session_state.result = None

    with st.spinner("🕯️ 正在请示学术祖师爷与图灵神明..."):
        try:
            result = run_oracle(user_input)
            st.session_state.result = result
            st.success("🎉 卦成！请阅签文。")
        except Exception as e:
            st.error(f"❌ 召唤失败：{str(e)}")
            st.info("💡 请检查网络连接与 API 密钥，或稍后再试。")

# ============================================================
# 结果显示区
# ============================================================
if st.session_state.result:
    result = st.session_state.result
    hexagram = result["hexagram"]

    # 卦象卡片
    with st.container(border=True):
        st.markdown(f"### 📜 卦象：{hexagram['name']} {hexagram['symbol']}")
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("吉凶", hexagram["verdict"])
        with col_b:
            st.metric("主题", hexagram["theme"])
        st.caption(f"**古籍原文**：{hexagram['ancient_text']}")
        st.caption(f"**学术提示**：{hexagram['academic_hint']}")

    st.markdown("### 🛠️ 硬核实操建议")
    st.markdown(result["strategy"])

    st.markdown("### 🎊 赛博签文")
    st.info(result["final"])

    # 重置按钮
    st.markdown("---")
    if st.button("🔄 再算一卦", use_container_width=True):
        st.session_state.result = None
        st.session_state.query = ""
        st.rerun()

# ============================================================
# 页脚说明
# ============================================================
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #888; font-size: 0.9em;'>
        <i>
        🔮 本系统融合《周易》六爻与 LangGraph 多智能体工作流<br>
        💡 所有建议均由 DeepSeek 生成，仅供娱乐与灵感启发<br>
        ⚠️ 科研不易，卦象可戏，行动需实
        </i>
    </div>
    """,
    unsafe_allow_html=True,
)