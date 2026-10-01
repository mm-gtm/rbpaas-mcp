"""勤務時間関連ツール"""
from typing import Any

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_work_time_summary(year: int, month: int) -> Any:
        """freee 勤怠由来の月次勤務時間スナップショット（全ユーザー）を取得する。

        Args:
            year: 年 (例: 2026)
            month: 月 (1-12)
        """
        return await api_client.get("/work-time/snapshots", params={"year": year, "month": month})

    @mcp.tool()
    async def get_daily_work_time(start_date: str, end_date: str) -> Any:
        """指定期間の日次勤務時間をユーザーごとに集計して取得する。

        Args:
            start_date: 開始日 (YYYY-MM-DD)
            end_date: 終了日 (YYYY-MM-DD)
        """
        return await api_client.get("/work-time/daily-summary", params={"start_date": start_date, "end_date": end_date})
