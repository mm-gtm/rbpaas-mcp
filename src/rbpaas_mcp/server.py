"""MCP Server セットアップ"""
from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.tools import dashboard, projects, members, feedbacks, optimization, schedules, work_time, agents

mcp = FastMCP(
    "RBPaaS Operation Hub",
    instructions="Revenue BPaaS オペレーション管理システムのデータにアクセスするMCPサーバー。事業KPI、プロジェクト、エージェント、スケジュール、フィードバック等を照会できます。",
)

# ツール登録
dashboard.register(mcp)
projects.register(mcp)
members.register(mcp)
feedbacks.register(mcp)
optimization.register(mcp)
schedules.register(mcp)
work_time.register(mcp)
agents.register(mcp)


def main():
    mcp.run(transport="stdio")
