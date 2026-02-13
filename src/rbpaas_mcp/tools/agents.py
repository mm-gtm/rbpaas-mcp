"""エージェント関連ツール"""
from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_agents() -> dict:
        """コールエージェント一覧を取得する。"""
        return await api_client.get("/users/agents")
