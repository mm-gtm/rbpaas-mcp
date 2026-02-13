"""ダッシュボード関連ツール"""
from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_business_overview(period: str = "monthly") -> dict:
        """事業全体のKPIとアラートを取得する。

        Args:
            period: 集計期間 (daily/weekly/monthly)。デフォルトはmonthly。
        """
        return await api_client.get("/dashboard/overview", params={"period": period})

    @mcp.tool()
    async def get_project_kpis(period: str = "monthly") -> dict:
        """プロジェクト別のKPI達成率を取得する。

        Args:
            period: 集計期間 (daily/weekly/monthly)。デフォルトはmonthly。
        """
        return await api_client.get("/dashboard/kpi", params={"period": period})

    @mcp.tool()
    async def get_resource_utilization() -> dict:
        """リソース（エージェント）の稼働率を取得する。"""
        return await api_client.get("/dashboard/resources")

    @mcp.tool()
    async def get_project_efficiency(period: str = "monthly") -> dict:
        """プロジェクト別の効率指標を取得する。

        Args:
            period: 集計期間 (daily/weekly/monthly)。デフォルトはmonthly。
        """
        return await api_client.get("/dashboard/efficiency", params={"period": period})
