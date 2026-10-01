"""CAレベル判定関連ツール"""
from typing import Any

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_ca_level_review_events() -> Any:
        """CAレベル判定イベント（判定の回）の一覧を取得する。"""
        return await api_client.get("/ca-level-reviews/events")

    @mcp.tool()
    async def get_ca_level_review_detail(event_id: str) -> Any:
        """CAレベル判定イベントの詳細（対象者ごとの自動判定・確定結果）を取得する。

        Args:
            event_id: 判定イベントID (UUID)
        """
        return await api_client.get(f"/ca-level-reviews/events/{event_id}")
