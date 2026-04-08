# 🔮 学术赛博算命 (Academic Oracle)

面向硕博研究生和青年学者的「学术情绪安抚与决策辅助工具」。

融合《周易》六爻与 LangGraph 多智能体工作流，将学术焦虑转化为硬核实操建议，包装成赛博玄学签文。

## 🚀 快速开始

### 本地运行
```bash
git clone <repository-url>
cd academic-oracle

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 填入你的 DEEPSEEK_API_KEY

# 启动应用
streamlit run app.py
```

### 在线体验
访问：[https://academic-oracle.streamlit.app](https://academic-oracle.streamlit.app)

## 🧠 技术架构

- **前端**: Streamlit (极简 UI)
- **后端**: LangGraph 四节点工作流
- **大模型**: DeepSeek-Chat (兼容 OpenAI API)
- **占卜核心**: 纯 Python 六爻模拟 (硬编码 8 卦)

## 🔄 工作流节点

1. **Node A**: 意图识别 - 分析学术焦虑类型
2. **Node B**: 六爻占卜 - 伪随机卦象抽取
3. **Node C**: 学术军师 - 生成 3 条实操建议
4. **Node D**: 签文包装 - 玄学语气 + 学术黑话

## 📁 项目结构
```
code/
├── app.py                 # Streamlit 前端
├── engine.py              # 主入口
├── core/                  # 核心定义与工具
├── nodes/                 # LangGraph 节点
├── config/                # 全局配置
├── workflow/              # 工作流组装
├── .env.example           # 环境变量模板
└── requirements.txt       # 依赖清单
```

## 🎯 功能特性

- ✅ 模块化架构，易于扩展新卦象/节点
- ✅ 纯 Python 占卜，无 LLM 幻觉风险
- ✅ 高压科研语境 Prompt 设计
- ✅ 黑色幽默 + 学术黑话风格
- ✅ 环境变量隔离，生产就绪

## ⚠️ 注意事项

- 所有建议仅供娱乐与灵感启发
- DeepSeek API 按 token 计费，请合理使用
- 卦象结果基于伪随机算法，非真实占卜

## 📄 许可证

MIT License