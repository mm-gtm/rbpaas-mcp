"""エージェント・ユーザー関連ツール"""
from typing import Any

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_agents(include_inactive: bool = False) -> Any:
        """コールエージェント（CA）一覧を取得する。

        Args:
            include_inactive: 退職・休職中のCAも含める（admin スコープのトークンが必要）
        """
        return await api_client.get("/users/agents/all" if include_inactive else "/users/agents")

    @mcp.tool()
    async def get_users(include_inactive: bool = False) -> Any:
        """全ユーザー（CA・IO・管理者）の一覧を取得する。

        Args:
            include_inactive: 非アクティブ（退職・休職）ユーザーも含める
        """
        return await api_client.get("/users/", params={"include_inactive": include_inactive})

    @mcp.tool()
    async def get_user_detail(user_id: str) -> Any:
        """ユーザーの詳細を取得する。

        Args:
            user_id: ユーザーID (UUID)
        """
        return await api_client.get(f"/users/{user_id}")

    @mcp.tool()
    async def get_experience_matrix() -> Any:
        """経験マトリクス（エージェント×プロジェクトの経験・習熟度）を取得する。"""
        return await api_client.get("/experiences/matrix")

    @mcp.tool()
    async def get_experience_detail(experience_id: int) -> Any:
        """経験マトリクスの1件（エージェント×プロジェクトの経験）の詳細を取得する。

        Args:
            experience_id: 経験ID (整数)
        """
        return await api_client.get(f"/experiences/{experience_id}")
