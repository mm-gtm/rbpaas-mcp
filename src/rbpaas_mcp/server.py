"""MCP Server セットアップ"""
from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.tools import dashboard, projects, members, feedbacks, optimization, schedules, work_time, agents

mcp = FastMCP(
    "RBPaaS Operation Hub",
    description="Revenue BPaaS オペレーション管理システムのデータにアクセスするMCPサーバー",
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
