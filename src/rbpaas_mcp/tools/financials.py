"""プロジェクト財務関連ツール"""
from typing import Any

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_project_financials(year: int, month: int) -> Any:
        """対象月のプロジェクト別財務サマリ（売上・人件費・粗利）を取得する。粗利の昇順（赤字が上）。

        Args:
            year: 年 (例: 2026)
            month: 月 (1-12)
        """
        return await api_client.get("/project-financials/", params={"year": year, "month": month})

    @mcp.tool()
    async def get_contracted_amounts(year: int, month: int) -> Any:
        """対象月の全プロジェクトの月次契約額を取得する。

        Args:
            year: 年 (例: 2026)
            month: 月 (1-12)
        """
        return await api_client.get("/project-financials/contracted-amounts", params={"year": year, "month": month})

    @mcp.tool()
    async def get_target_alignment(year: int, month: int) -> Any:
        """PJ目標と個人目標の合計が一致しているかを点検する。

        Args:
            year: 年 (例: 2026)
            month: 月 (1-12)
        """
        return await api_client.get("/project-financials/target-alignment", params={"year": year, "month": month})
