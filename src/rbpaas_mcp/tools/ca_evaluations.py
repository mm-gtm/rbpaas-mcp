"""CA評価・昇降格・報酬関連ツール"""
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_ca_evaluation_summary(year: int, month: int) -> Any:
        """指定月の全CAの評価サマリー（Deal/活動量の達成率・出勤率など）を取得する。

        Args:
            year: 年 (例: 2026)
            month: 月 (1-12)
        """
        return await api_client.get(f"/ca-evaluations/summary/{year}/{month}")

    @mcp.tool()
    async def get_ca_evaluation_history(user_id: str, skip: int = 0, limit: int = 12) -> Any:
        """CA1人の月次評価履歴を取得する。

        Args:
            user_id: ユーザーID (UUID)
            skip: スキップ件数
            limit: 取得件数 (最大60)
        """
        return await api_client.get(f"/ca-evaluations/{user_id}", params={"skip": skip, "limit": limit})

    @mcp.tool()
    async def get_ca_evaluation_detail(user_id: str, year: int, month: int) -> Any:
        """CA1人の特定月の評価詳細（インセンティブ明細・ROIチェック含む）を取得する。

        Args:
            user_id: ユーザーID (UUID)
            year: 年 (例: 2026)
            month: 月 (1-12)
        """
        return await api_client.get(f"/ca-evaluations/{user_id}/{year}/{month}")

    @mcp.tool()
    async def preview_ca_deal_targets(year: int, month: int) -> Any:
        """全アクティブCAの Deal 目標（人件費回収方式）をその場で計算して取得する。保存はされない。

        Args:
            year: 年 (例: 2026)
            month: 月 (1-12)
        """
        return await api_client.get("/ca-evaluations/deal-targets/preview", params={"year": year, "month": month})

    @mcp.tool()
    async def get_ca_promotion_candidates() -> Any:
        """昇格条件を満たすCA候補者の一覧を取得する。"""
        return await api_client.get("/ca-promotions/candidates")

    @mcp.tool()
    async def get_ca_demotion_candidates() -> Any:
        """3ヶ月連続未達の降格候補CAの一覧を取得する。"""
        return await api_client.get("/ca-demotions/candidates")

    @mcp.tool()
    async def get_ca_raise_candidates() -> Any:
        """定期昇給・成果昇給の候補CAの一覧を取得する。"""
        return await api_client.get("/ca-raises/candidates")

    @mcp.tool()
    async def get_ca_level_change_history(user_id: str) -> Any:
        """CA1人のレベル変更履歴を取得する。

        Args:
            user_id: ユーザーID (UUID)
        """
        return await api_client.get(f"/ca-level-changes/{user_id}")

    @mcp.tool()
    async def get_ca_salary_change_history(user_id: str) -> Any:
        """CA1人の時給変更履歴を取得する。

        Args:
            user_id: ユーザーID (UUID)
        """
        return await api_client.get(f"/ca-salary-changes/{user_id}")

    @mcp.tool()
    async def get_ca_planning_alerts(
        year: int,
        month: int,
        resolved: Optional[bool] = None,
        alert_type: Optional[str] = None,
    ) -> Any:
        """指定月のCA計画時アラート（目標設定・配置計画で注意が必要な点）を取得する。

        Args:
            year: 年 (例: 2026)
            month: 月 (1-12)
            resolved: 解決済みで絞る (True/False)。省略時はすべて。
            alert_type: アラート種別で絞る
        """
        return await api_client.get(f"/ca-planning-alerts/{year}/{month}", params={
            "resolved": resolved, "alert_type": alert_type,
        })

    @mcp.tool()
    async def get_ca_compensation_sheets(limit: int = 24) -> Any:
        """CA報酬管理の月次連絡票の一覧（月ごと・凍結状態つき）を取得する。

        Args:
            limit: 取得件数 (最大120)
        """
        return await api_client.get("/ca-compensation/sheets", params={"limit": limit})

    @mcp.tool()
    async def get_ca_compensation_sheet_detail(sheet_id: str) -> Any:
        """CA報酬管理の月次連絡票の明細（CAごとの支給計算）を取得する。

        Args:
            sheet_id: 連絡票ID (UUID)
        """
        return await api_client.get(f"/ca-compensation/sheets/{sheet_id}")
