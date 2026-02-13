"""プロジェクト関連ツール"""
from typing import Optional

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_project_list(
        status: Optional[str] = None,
        is_active: Optional[bool] = True,
        skip: int = 0,
        limit: int = 100,
    ) -> dict:
        """プロジェクト一覧を取得する。

        Args:
            status: ステータスでフィルタ (planning/active/completed/on_hold/cancelled)
            is_active: アクティブなプロジェクトのみ取得するか (デフォルト: True)
            skip: スキップ件数
            limit: 取得件数上限
        """
        return await api_client.get("/projects", params={
            "status": status,
            "is_active": is_active,
            "skip": skip,
            "limit": limit,
        })

    @mcp.tool()
    async def get_project_detail(project_id: str) -> dict:
        """プロジェクトの詳細情報を取得する。

        Args:
            project_id: プロジェクトID (UUID)
        """
        return await api_client.get(f"/projects/{project_id}")
