"""スケジュール関連ツール"""
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_schedules(
        start_date: str,
        end_date: str,
        user_id: Optional[str] = None,
        include_inactive: bool = False,
    ) -> Any:
        """シフト（スケジュール）一覧を取得する。

        Args:
            start_date: 開始日 (YYYY-MM-DD形式、必須)
            end_date: 終了日 (YYYY-MM-DD形式、必須)
            user_id: ユーザーIDでフィルタ (UUID)
            include_inactive: 退社済みユーザーも含める
        """
        return await api_client.get("/schedules/", params={
            "start_date": start_date,
            "end_date": end_date,
            "user_id": user_id,
            "include_inactive": include_inactive,
        })

    @mcp.tool()
    async def get_schedule_change_requests(year: int, month: int, user_id: Optional[str] = None) -> Any:
        """シフト変更依頼の一覧を取得する。

        Args:
            year: 年 (例: 2026)
            month: 月 (1-12)
            user_id: ユーザーIDでフィルタ (UUID)
        """
        return await api_client.get("/schedules/change-requests", params={
            "year": year, "month": month, "user_id": user_id,
        })
