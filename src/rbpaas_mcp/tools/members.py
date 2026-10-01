"""メンバーKPI関連ツール"""
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_member_kpis(project_name: str, period: str = "monthly", reference_date: Optional[str] = None) -> Any:
        """プロジェクト内のメンバー別KPIを取得する。

        Args:
            project_name: プロジェクト名（必須。get_project_list で確認できる正式名）
            period: 集計期間 (weekly/monthly/quarterly)。デフォルトは monthly。
            reference_date: 参照日 (YYYY-MM-DD)。省略時は今日。
        """
        return await api_client.get("/dashboard/members", params={
            "project_name": project_name, "period": period, "reference_date": reference_date,
        })

    @mcp.tool()
    async def get_member_daily_kpis(project_name: str, period: str = "monthly", reference_date: Optional[str] = None) -> Any:
        """プロジェクト内のメンバー別KPIを日次の内訳つきで取得する。

        Args:
            project_name: プロジェクト名（必須）
            period: 集計期間 (weekly/monthly/quarterly)。デフォルトは monthly。
            reference_date: 参照日 (YYYY-MM-DD)。省略時は今日。
        """
        return await api_client.get("/dashboard/members/daily", params={
            "project_name": project_name, "period": period, "reference_date": reference_date,
        })
