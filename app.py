import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 如果你还没有准备好 engine 模块，请先注释掉下一行，并使用下方的 Mock Data 来测试 UI
from engine import run_oracle 

# ============================================================
# Page config
# ============================================================
st.set_page_config(
    page_title="Academic Oracle",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ============================================================
# 🍎 Apple-Style CSS 
# ============================================================
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');

  :root {
    /* 极致还原 Apple 的字体栈 */
    --font: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", 
            "Inter", "Helvetica Neue", "Noto Sans SC", sans-serif;
    --bg: #fbfbfd;         
    --card: #ffffff;
    --text-1: #1d1d1f;     
    --text-2: #86868b;     
    --text-3: #86868b;
    --accent: #0071e3;     
    --shadow-subtle: 0 4px 24px rgba(0, 0, 0, 0.04);
    --shadow-hover: 0 10px 40px rgba(0, 0, 0, 0.08);
  }

  html, body, [class*="css"] {
    font-family: var(--font) !important;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  .stApp { 
    background-color: var(--bg) !important; 
  }

  /* 隐藏 Streamlit 默认的顶部和底部元素 */
  #MainMenu, footer, header, 
  div[data-testid="stDecoration"],
  div[data-testid="stToolbar"] { display: none !important; }

  /* 限制最大宽度并居中，增加两边呼吸空间 */
  .block-container {
    max-width: 680px !important;
    padding: 2rem 1.5rem !important;
  }

  /* ── Hero Section ── */
  .ao-hero {
    text-align: center;
    padding: 60px 0 40px;
  }
  .ao-eyebrow {
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 8px;
  }
  .ao-title {
    font-size: 48px;
    font-weight: 700;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text-1);
    margin: 0 0 16px;
  }
  .ao-subtitle {
    font-size: 20px;
    color: var(--text-2);
    line-height: 1.4;
    font-weight: 400;
    max-width: 80%;
    margin: 0 auto;
  }
  @media (max-width: 600px) {
    .ao-title { font-size: 36px; }
    .ao-subtitle { font-size: 16px; width: 100%; }
  }

  /* ── Textarea (终极输入框质感优化) ── */
  div[data-testid="stTextArea"] {
    margin-bottom: 28px;
  }
  div[data-testid="stTextArea"] label { 
    display: none !important; 
  }
  
  /* 彻底干掉 Streamlit 底层包装盒的边框和背景干扰 */
  div[data-testid="stTextArea"] > div,
  div[data-testid="stTextArea"] > div > div {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    outline: none !important;
  }

  /* 核心输入区域 */
  div[data-testid="stTextArea"] textarea {
    background-color: rgba(0, 0, 0, 0.02) !important; 
    border: 1px solid rgba(0, 0, 0, 0.03) !important;
    border-radius: 20px !important; 
    font-family: var(--font) !important;
    font-size: 16px !important; 
    line-height: 1.6 !important;
    color: var(--text-1) !important;
    padding: 24px !important;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.01) !important; 
    transition: all 0.35s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
    resize: none !important; 
  }

  /* 鼠标悬停时稍微加深背景 */
  div[data-testid="stTextArea"] textarea:hover {
    background-color: rgba(0, 0, 0, 0.04) !important;
  }

  /* 聚焦时的灵魂交互：变白、浮起、发光 */
  div[data-testid="stTextArea"] textarea:focus {
    background-color: #ffffff !important; 
    border-color: rgba(0, 113, 227, 0.4) !important; 
    box-shadow: 0 0 0 4px rgba(0, 113, 227, 0.12), 
                0 8px 24px rgba(0, 0, 0, 0.06) !important; 
    outline: none !important;
  }

  div[data-testid="stTextArea"] textarea::placeholder {
    color: #a1a1a6 !important;
    font-weight: 400 !important;
  }

  /* 隐藏底部可能出现的字数限制或提示语 */
  div[data-testid="InputInstructions"] {
    display: none !important;
  }

  /* ── Button (药丸形按钮) ── */
  div.stButton > button {
    background-color: var(--text-1) !important; 
    color: #ffffff !important;
    border: none !important;
    border-radius: 980px !important; 
    font-family: var(--font) !important;
    font-size: 16px !important;
    font-weight: 500 !important;
    padding: 14px 32px !important;
    width: 100% !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.1) !important;
  }
  div.stButton > button:hover {
    background-color: #333336 !important;
    transform: scale(1.02) !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.15) !important;
  }
  div.stButton > button:active {
    transform: scale(0.98) !important;
  }

  /* Secondary Button (重置) */
  .ao-reset div.stButton > button {
    background-color: transparent !important;
    color: var(--accent) !important;
    box-shadow: none !important;
    font-size: 15px !important;
  }
  .ao-reset div.stButton > button:hover {
    background-color: rgba(0, 113, 227, 0.05) !important;
    transform: none !important;
  }

  /* ── Result Cards ── */
  .ao-card {
    background: var(--card);
    border-radius: 24px;
    box-shadow: var(--shadow-subtle);
    padding: 32px;
    margin-bottom: 24px;
    transition: box-shadow 0.3s ease;
    overflow: hidden;
  }
  .ao-card:hover {
    box-shadow: var(--shadow-hover);
  }
  .ao-card-label {
    font-size: 13px;
    font-weight: 600;
    letter-spacing: -0.01em;
    color: var(--text-2);
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  
  /* 卦象展示优化 */
  .ao-hex-row {
    display: flex;
    align-items: baseline;
    gap: 12px;
    margin-bottom: 24px;
  }
  .ao-hex-name {
    font-size: 32px;
    font-weight: 700;
    color: var(--text-1);
    letter-spacing: -0.02em;
  }
  .ao-hex-sym {
    font-size: 28px;
    color: var(--text-1);
  }
  .ao-hex-tag {
    margin-left: auto;
    font-size: 13px;
    font-weight: 600;
    background: rgba(0, 113, 227, 0.1);
    color: var(--accent);
    padding: 6px 14px;
    border-radius: 8px;
  }
  
  .ao-hex-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    margin-bottom: 24px;
    background: #fbfbfd;
    padding: 20px;
    border-radius: 16px;
  }
  .ao-hex-key {
    font-size: 12px;
    font-weight: 500;
    color: var(--text-2);
    margin-bottom: 6px;
  }
  .ao-hex-val {
    font-size: 15px;
    font-weight: 500;
    color: var(--text-1);
    line-height: 1.5;
  }
  .ao-hex-ancient {
    font-size: 15px;
    color: var(--text-2);
    line-height: 1.6;
    padding-top: 20px;
    border-top: 1px solid rgba(0,0,0,0.06);
  }

  /* 文本正文 */
  .ao-body {
    font-size: 16px;
    line-height: 1.7;
    color: var(--text-1);
    font-weight: 400;
  }


  /* ── 赛博签文排版优化 ── */
  .ao-oracle-text {
    font-size: 17px;
    line-height: 1.7;
    color: var(--text-1); 
    font-weight: 400;
    letter-spacing: 0.01em;
  }
  .ao-oracle-text p {
    margin-bottom: 16px;
  }
  .ao-oracle-text p:last-child {
    margin-bottom: 0;
  }

  /* ── 进度条/加载状态优化 ── */
  div[data-testid="stSpinner"] > div {
    font-family: var(--font) !important;
    color: var(--accent) !important;
  }

  /* ── Footer ── */
  .ao-footer {
    text-align: center;
    padding: 40px 0;
    font-size: 13px;
    color: var(--text-3);
    line-height: 1.5;
  }
</style>
""", unsafe_allow_html=True)

# ============================================================
# Session state
# ============================================================
if "result" not in st.session_state:
    st.session_state.result = None
if "query" not in st.session_state:
    st.session_state.query = ""

# ============================================================
# Hero Section
# ============================================================
st.markdown("""
<div class="ao-hero">
  <div class="ao-eyebrow">Academic Oracle</div>
  <div class="ao-title">学术赛博算命</div>
  <div class="ao-subtitle">描述你的科研困境，得一卦，破一局。</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# Input section
# ============================================================
user_input = st.text_area(
    label="描述困境",
    value=st.session_state.query,
    height=140,
    placeholder="例如：论文被拒3次、实验死活跑不通、导师失联一周了、套磁毫无回音……描述越具体越准。",
    label_visibility="collapsed",
)

# Button 布局 (居中留白)
st.write("") 
col1, col2, col3 = st.columns([1, 1.5, 1])
with col2:
    button_clicked = st.button("开始推演", type="primary", use_container_width=True)

# ============================================================
# Run logic
# ============================================================
if button_clicked:
    if not user_input.strip():
        st.warning("请先描述你的困境，再行起卦。")
    else:
        st.session_state.query = user_input
        st.session_state.result = None
        with st.spinner("正在推演天机与数据..."):
            try:
                result = run_oracle(user_input)
                st.session_state.result = result
            except Exception as e:
                st.error(f"出了点问题：{str(e)}")
                st.caption("请检查网络连接与 API 配置后重试。")

# ============================================================
# Mock Data for testing UI (纯看UI可以取消注释下面这段)
# ============================================================
# st.session_state.result = {
#     "hexagram": {
#         "name": "水雷屯",
#         "symbol": "䷂",
#         "verdict": "大凶转吉",
#         "theme": "万事开头难，静待时机",
#         "academic_hint": "暂缓猛攻，需重新审视基础数据",
#         "ancient_text": "屯：元亨利贞，勿用有攸往，利建侯。初九：磐桓；利居贞，利建侯。"
#     },
#     "strategy": "立刻整理你近5年代表作，按IF和引用数排序，用Excel做个表格，重点标出独立通讯作者文章和领域内顶刊。\n这周就联系3个已经拿到海外优青的师兄师姐，直接问他们申请材料里“研究计划”那部分怎么写最加分。\n下个月开始，在你目标申报单位的学术会议上至少做2次口头报告，结束后主动找该单位的杰青/长江学者交流15分钟。",
#     "final": "屯卦说“动乎险中”，你这35岁前冲海外优青的念头，本质上就是一场hard deadline下的高风险学术冲刺。\n卦象凶中带吉，翻译过来就是：你现有的发表记录可能还欠点火候，但操作得当还能抢救。\n立刻打开Excel，把你近五年的代表作按IF和引用数排个序——海外优青评审可不会帮你做消融实验。这周就套磁三个已上岸的师兄师姐，直接问他们研究计划那部分的“炼丹配方”。\n屯卦所谓“刚柔始交”，说的就是这种高风险社交：脸刷够了，后续的大修意见才可能带点人情味。"
# }

# ============================================================
# Results Display
# ============================================================
if st.session_state.result:
    result = st.session_state.result
    h = result["hexagram"]

    # 给结果区上方加一点留白
    st.markdown('<div style="margin-top: 40px;"></div>', unsafe_allow_html=True)

    # 1. 卦象卡片
    st.markdown(f"""
    <div class="ao-card">
      <div class="ao-card-label">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
        本卦解析
      </div>
      <div class="ao-hex-row">
        <span class="ao-hex-name">{h["name"]}</span>
        <span class="ao-hex-sym">{h["symbol"]}</span>
        <span class="ao-hex-tag">{h["verdict"]}</span>
      </div>
      <div class="ao-hex-grid">
        <div>
          <div class="ao-hex-key">核心主题</div>
          <div class="ao-hex-val">{h["theme"]}</div>
        </div>
        <div>
          <div class="ao-hex-key">科研启示</div>
          <div class="ao-hex-val">{h["academic_hint"]}</div>
        </div>
      </div>
      <div class="ao-hex-ancient">“{h["ancient_text"]}”</div>
    </div>
    """, unsafe_allow_html=True)

    # 2. 实操建议 — 轮播卡片（带箭头 + 圆点）
    import streamlit.components.v1 as components
    raw_strategies = [s.strip() for s in result["strategy"].split('\n') if s.strip()]
    slides_html = ""
    dots_html = ""
    for i, step in enumerate(raw_strategies):
        clean_step = step.lstrip('0123456789.・• ')
        active = "active" if i == 0 else ""
        slides_html += f'<div class="slide {active}" data-i="{i}"><div class="step-label">STEP 0{i+1}</div><div class="step-text">{clean_step}</div></div>'
        dots_html += f'<span class="dot {active}" data-i="{i}"></span>'
    total = len(raw_strategies)

    carousel_component = f"""
    <html>
    <head>
    <style>
      * {{ margin:0; padding:0; box-sizing:border-box; }}
      body {{
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Inter", "Noto Sans SC", sans-serif;
        background: transparent;
        -webkit-font-smoothing: antialiased;
      }}
      .card {{
        background: #fff;
        border-radius: 24px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.04);
        padding: 32px;
        position: relative;
      }}
      .card-label {{
        font-size: 13px;
        font-weight: 600;
        color: #86868b;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 8px;
      }}
      .card-label svg {{ flex-shrink: 0; }}
      .slider {{
        position: relative;
        overflow: hidden;
        border-radius: 16px;
      }}
      .slides-track {{
        display: flex;
        transition: transform 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
      }}
      .slide {{
        flex: 0 0 100%;
        background: #fbfbfd;
        border-radius: 16px;
        padding: 24px;
        min-height: 120px;
      }}
      .step-label {{
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.1em;
        color: #0071e3;
        text-transform: uppercase;
        margin-bottom: 14px;
      }}
      .step-text {{
        font-size: 15px;
        line-height: 1.75;
        color: #1d1d1f;
      }}
      /* Arrows */
      .arrow {{
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        width: 36px; height: 36px;
        border-radius: 50%;
        background: rgba(255,255,255,0.9);
        box-shadow: 0 2px 8px rgba(0,0,0,0.12);
        border: none;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.25s ease;
        z-index: 10;
      }}
      .slider:hover .arrow {{ opacity: 1; }}
      .arrow:hover {{ background: #fff; box-shadow: 0 2px 12px rgba(0,0,0,0.18); }}
      .arrow-left {{ left: 8px; }}
      .arrow-right {{ right: 8px; }}
      .arrow svg {{ width: 16px; height: 16px; stroke: #1d1d1f; fill: none; stroke-width: 2; }}
      .arrow.hidden {{ display: none; }}
      /* Dots */
      .dots {{
        display: flex;
        justify-content: center;
        gap: 8px;
        margin-top: 16px;
      }}
      .dot {{
        width: 7px; height: 7px;
        border-radius: 50%;
        background: #d2d2d7;
        cursor: pointer;
        transition: all 0.25s ease;
      }}
      .dot.active {{
        background: #1d1d1f;
        width: 20px;
        border-radius: 4px;
      }}
    </style>
    </head>
    <body>
    <div class="card">
      <div class="card-label">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
        破局行动指南
      </div>
      <div class="slider">
        <div class="slides-track" id="track">{slides_html}</div>
        <button class="arrow arrow-left hidden" id="al" onclick="go(-1)">
          <svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg>
        </button>
        <button class="arrow arrow-right" id="ar" onclick="go(1)">
          <svg viewBox="0 0 24 24"><polyline points="9 6 15 12 9 18"/></svg>
        </button>
      </div>
      <div class="dots" id="dots">{dots_html}</div>
    </div>
    <script>
      var cur = 0, total = {total};
      var track = document.getElementById('track');
      var al = document.getElementById('al');
      var ar = document.getElementById('ar');
      var dots = document.querySelectorAll('.dot');

      function go(d) {{
        cur = Math.max(0, Math.min(total - 1, cur + d));
        update();
      }}
      function jumpTo(i) {{
        cur = i;
        update();
      }}
      function update() {{
        track.style.transform = 'translateX(-' + (cur * 100) + '%)';
        al.className = 'arrow arrow-left' + (cur === 0 ? ' hidden' : '');
        ar.className = 'arrow arrow-right' + (cur === total - 1 ? ' hidden' : '');
        dots.forEach(function(d, i) {{
          d.className = 'dot' + (i === cur ? ' active' : '');
        }});
      }}
      dots.forEach(function(d, i) {{
        d.addEventListener('click', function() {{ jumpTo(i); }});
      }});
    </script>
    </body>
    </html>
    """
    components.html(carousel_component, height=280, scrolling=False)

    # 3. 最终签文 (按段落排版，提升阅读体验)
    oracle_paragraphs = "".join([f"<p>{p.strip()}</p>" for p in result["final"].split('\n') if p.strip()])
    
    st.markdown(f"""
    <div class="ao-card">
      <div class="ao-card-label">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
        赛博签文
      </div>
      <div class="ao-oracle-text">{oracle_paragraphs}</div>
    </div>
    """, unsafe_allow_html=True)

    # Reset Button
    st.markdown('<div class="ao-reset">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("重新推演", use_container_width=True):
            st.session_state.result = None
            st.session_state.query = ""
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# Footer
# ============================================================
st.markdown("""
<div class="ao-footer">
  Powered by I Ching & Multi-Agent AI.<br>
  All insights are generated for reference.
</div>
""", unsafe_allow_html=True)