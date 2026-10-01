"""ダッシュボード関連ツール"""
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_business_overview(period: str = "monthly", reference_date: Optional[str] = None) -> Any:
        """事業全体のKPIとアラートを取得する。

        Args:
            period: 集計期間 (weekly/monthly/quarterly)。デフォルトは monthly。
            reference_date: 参照日 (YYYY-MM-DD)。省略時は今日。過去の週・月を見るときに指定する。
        """
        return await api_client.get("/dashboard/overview", params={"period": period, "reference_date": reference_date})

    @mcp.tool()
    async def get_project_kpis(period: str = "monthly", reference_date: Optional[str] = None) -> Any:
        """プロジェクト別のKPI（ACT/DMR/TOSS）の目標と実績・達成率を取得する。

        Args:
            period: 集計期間 (weekly/monthly/quarterly)。デフォルトは monthly。
            reference_date: 参照日 (YYYY-MM-DD)。省略時は今日。過去の週・月を見るときに指定する。
        """
        return await api_client.get("/dashboard/kpi", params={"period": period, "reference_date": reference_date})

    @mcp.tool()
    async def get_toss_details(project_id: str, period: str = "monthly", reference_date: Optional[str] = None) -> Any:
        """プロジェクトの TOSS（商談化）明細を取得する。KPI の TOSS 実績の内訳確認に使う。

        Args:
            project_id: プロジェクトID (UUID)
            period: 集計期間 (weekly/monthly/quarterly)。デフォルトは monthly。
            reference_date: 参照日 (YYYY-MM-DD)。省略時は今日。過去の週・月を見るときに指定する。
        """
        return await api_client.get(f"/dashboard/kpi/{project_id}/toss-details", params={
            "period": period, "reference_date": reference_date,
        })

    @mcp.tool()
    async def get_resource_utilization() -> Any:
        """リソース（エージェント）の稼働率を取得する。"""
        return await api_client.get("/dashboard/resources")

    @mcp.tool()
    async def get_supply_demand() -> Any:
        """エージェント供給（稼働可能時間）とプロジェクト需要の需給バランスを取得する。"""
        return await api_client.get("/dashboard/supply-demand")

    @mcp.tool()
    async def get_project_efficiency(period: str = "monthly", reference_date: Optional[str] = None) -> Any:
        """プロジェクト別の効率指標（時間あたり活動数・商談数など）を取得する。

        Args:
            period: 集計期間 (weekly/monthly/quarterly)。デフォルトは monthly。
            reference_date: 参照日 (YYYY-MM-DD)。省略時は今日。過去の週・月を見るときに指定する。
        """
        return await api_client.get("/dashboard/efficiency", params={"period": period, "reference_date": reference_date})

    @mcp.tool()
    async def get_business_metrics(year: Optional[int] = None) -> Any:
        """事業数値（月次売上）を取得する。

        Args:
            year: 対象年。省略時は今年。
        """
        return await api_client.get("/dashboard/business-metrics", params={"year": year})

    @mcp.tool()
    async def get_project_activity(project_id: str, start_date: Optional[str] = None, end_date: Optional[str] = None) -> Any:
        """プロジェクトの活動実績（MMP Activity 由来）を期間指定で取得する。

        Args:
            project_id: プロジェクトID (UUID)
            start_date: 開始日 (YYYY-MM-DD)。省略時は今月1日。
            end_date: 終了日 (YYYY-MM-DD)。省略時は今日。
        """
        return await api_client.get(f"/dashboard/activity/{project_id}", params={
            "start_date": start_date, "end_date": end_date,
        })

    @mcp.tool()
    async def get_daily_activity(start_date: Optional[str] = None, end_date: Optional[str] = None) -> Any:
        """全プロジェクトの日次活動データを取得する。

        Args:
            start_date: 開始日 (YYYY-MM-DD)。省略時は今月1日。
            end_date: 終了日 (YYYY-MM-DD)。省略時は今日。
        """
        return await api_client.get("/dashboard/activity/daily", params={"start_date": start_date, "end_date": end_date})

    @mcp.tool()
    async def get_depot_data(from_date: Optional[str] = None, to_date: Optional[str] = None) -> Any:
        """Momentum Depot（AI-SDR）側の活動・成果データを取得する。

        Args:
            from_date: 期間開始日 (YYYY-MM-DD)
            to_date: 期間終了日 (YYYY-MM-DD)
        """
        return await api_client.get("/dashboard/depot", params={"from_date": from_date, "to_date": to_date})

    @mcp.tool()
    async def get_individual_kpi(year: int, month: int) -> Any:
        """個人KPI（主担当PJごとの個人目標TOSSと実績TOSS）を取得する。

        Args:
            year: 年 (例: 2026)
            month: 月 (1-12)
        """
        return await api_client.get("/dashboard/individual-kpi", params={"year": year, "month": month})

    @mcp.tool()
    async def get_sub_project_kpi(year: int, month: int) -> Any:
        """サブPJアサインごとのTOSS実績とインセンティブを取得する。

        Args:
            year: 年 (例: 2026)
            month: 月 (1-12)
        """
        return await api_client.get("/dashboard/sub-project-kpi", params={"year": year, "month": month})
