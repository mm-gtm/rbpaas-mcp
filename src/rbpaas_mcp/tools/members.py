"""メンバーKPI関連ツール"""
from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_member_kpis(project_name: str, period: str = "monthly") -> dict:
        """メンバー別のKPIを取得する。

        Args:
            project_name: プロジェクト名（必須）
            period: 集計期間 (daily/weekly/monthly)。デフォルトはmonthly。
        """
        return await api_client.get("/dashboard/members", params={
            "project_name": project_name,
            "period": period,
        })
