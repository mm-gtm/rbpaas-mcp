"""スケジュール関連ツール"""
from typing import Optional

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_schedules(
        start_date: str,
        end_date: str,
        user_id: Optional[str] = None,
    ) -> dict:
        """スケジュール一覧を取得する。

        Args:
            start_date: 開始日 (YYYY-MM-DD形式、必須)
            end_date: 終了日 (YYYY-MM-DD形式、必須)
            user_id: ユーザーIDでフィルタ (UUID)
        """
        return await api_client.get("/schedules", params={
            "start_date": start_date,
            "end_date": end_date,
            "user_id": user_id,
        })
