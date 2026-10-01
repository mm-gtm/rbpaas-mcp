"""プロジェクト関連ツール"""
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_project_list(
        status: Optional[str] = None,
        is_active: Optional[bool] = True,
        skip: int = 0,
        limit: int = 100,
    ) -> Any:
        """プロジェクト一覧を取得する。

        Args:
            status: ステータスでフィルタ (new=新規立ち上げ / stable=安定運用 / at_risk=リスクあり / closing=終了予定)
            is_active: アクティブなプロジェクトのみ取得するか (デフォルト: True)
            skip: スキップ件数
            limit: 取得件数上限 (最大1000)
        """
        return await api_client.get("/projects", params={
            "status": status, "is_active": is_active, "skip": skip, "limit": limit,
        })

    @mcp.tool()
    async def get_project_detail(project_id: str) -> Any:
        """プロジェクトの詳細情報を取得する。

        Args:
            project_id: プロジェクトID (UUID)
        """
        return await api_client.get(f"/projects/{project_id}")

    @mcp.tool()
    async def get_project_monthly_summary(year: int, month: int) -> Any:
        """全プロジェクトの月次サマリー（月次目標・実績）を取得する。

        Args:
            year: 年 (例: 2026)
            month: 月 (1-12)
        """
        return await api_client.get("/projects/monthly-summary", params={"year": year, "month": month})

    @mcp.tool()
    async def get_project_monthly_target(project_id: str, year: int, month: int) -> Any:
        """プロジェクトの月次目標（ACT/DMR/TOSS など）を取得する。

        Args:
            project_id: プロジェクトID (UUID)
            year: 年 (例: 2026)
            month: 月 (1-12)
        """
        return await api_client.get(f"/projects/{project_id}/monthly-targets/{year}/{month}")

    @mcp.tool()
    async def get_project_target_change_logs(project_id: str) -> Any:
        """プロジェクトの月次目標の変更履歴を取得する。

        Args:
            project_id: プロジェクトID (UUID)
        """
        return await api_client.get(f"/projects/{project_id}/monthly-target-change-logs")

    @mcp.tool()
    async def get_project_groups() -> Any:
        """プロジェクトグループ（同一顧客の複数PJをまとめた単位）の一覧を取得する。"""
        return await api_client.get("/project-groups/")

    @mcp.tool()
    async def get_project_group_detail(group_id: str) -> Any:
        """プロジェクトグループの詳細を取得する。

        Args:
            group_id: プロジェクトグループID (UUID)
        """
        return await api_client.get(f"/project-groups/{group_id}")

    @mcp.tool()
    async def get_project_aggregates() -> Any:
        """合算表示（複数PJをまとめて見る単位）の一覧を取得する。"""
        return await api_client.get("/project-aggregates")

    @mcp.tool()
    async def get_resource_simulation_base(months: int = 6) -> Any:
        """リソースシミュレーションの基礎データ（月別の人員・稼働・需要）を取得する。

        Args:
            months: 取得する月数（当月含む、最大24）
        """
        return await api_client.get("/resource-simulation/base-data", params={"months": months})
