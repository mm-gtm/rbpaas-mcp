"""勤務時間関連ツール"""
from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_work_time_summary(year: int, month: int) -> list:
        """勤務時間サマリーを取得する。

        Args:
            year: 年 (例: 2026)
            month: 月 (1-12)
        """
        return await api_client.get("/work-time/snapshots", params={
            "year": year,
            "month": month,
        })
