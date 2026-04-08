"""
学术赛博算命 (Academic Oracle) 主入口文件。
提供简洁的 API 接口供前端调用。
"""

from workflow.graph import run_oracle


# ============================================================
# 快速本地测试（直接运行此文件时执行）
# ============================================================
if __name__ == "__main__":
    print("=== 学术赛博算命 - 模块化架构测试 ===\n")

    query = "我的论文被 Reviewer 2 骂得体无完肤，不知道怎么办"
    print(f"📝 用户焦虑：{query}")
    print()

    print("🔮 正在启动学术赛博算命工作流...")
    result = run_oracle(query)

    print("\n✅ 工作流完成！结果摘要：")
    print(f"   意图识别：{result['intent']}")
    print(f"   卦象：{result['hexagram']['name']} {result['hexagram']['symbol']} ({result['hexagram']['verdict']})")
    print(f"   主题：{result['hexagram']['theme']}")
    print(f"   古籍：{result['hexagram']['ancient_text']}")
    print()
    print("📋 实操建议：")
    print(result['strategy'])
    print()
    print("🎊 最终签文：")
    print("=" * 50)
    print(result['final'])
    print("=" * 50)