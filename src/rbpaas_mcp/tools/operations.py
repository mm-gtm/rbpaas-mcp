"""稼動・勤怠モニタリング関連ツール"""
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_work_monitor(year: Optional[int] = None, month: Optional[int] = None) -> Any:
        """CA（コールエージェント）ごとの月間の想定稼動・実稼動・想定活動数・実活動数を取得する。

        Args:
            year: 年。省略時は今年。
            month: 月 (1-12)。省略時は今月。
        """
        return await api_client.get("/work-monitor/overview", params={"year": year, "month": month})

    @mcp.tool()
    async def get_ca_activity_grid(
        user_id: str,
        year: Optional[int] = None,
        month: Optional[int] = None,
        project_id: Optional[str] = None,
    ) -> Any:
        """CA1人の「日×時間帯(8-20時)」の活動グリッドを取得する。稼動の偏りや空白時間の確認に使う。

        Args:
            user_id: ユーザーID (UUID)
            year: 年。省略時は今年。
            month: 月 (1-12)。省略時は今月。
            project_id: 指定時はそのPJのみ。省略時は全PJ合算。
        """
        return await api_client.get(f"/work-monitor/{user_id}/activity-grid", params={
            "year": year, "month": month, "project_id": project_id,
        })

    @mcp.tool()
    async def get_activity_stall_alerts(
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        user_id: Optional[str] = None,
        project_id: Optional[str] = None,
        only_open: bool = False,
        include_dismissed: bool = False,
        limit: int = 200,
    ) -> Any:
        """活動停滞アラート（シフト中なのに活動が止まっている検知）の一覧を取得する。

        Args:
            start_date: 開始日 (YYYY-MM-DD)。省略時は7日前。
            end_date: 終了日 (YYYY-MM-DD)。省略時は今日。
            user_id: ユーザーIDでフィルタ
            project_id: プロジェクトIDでフィルタ
            only_open: 未対応のみ
            include_dismissed: 対象外にしたもの（休暇申請・シフト取消・誤検知）も含める
            limit: 取得件数上限 (最大1000)
        """
        return await api_client.get("/activity-stall-alerts", params={
            "start_date": start_date,
            "end_date": end_date,
            "user_id": user_id,
            "project_id": project_id,
            "only_open": only_open,
            "include_dismissed": include_dismissed,
            "limit": limit,
        })

    @mcp.tool()
    async def get_attendance_rate(year: Optional[int] = None, month: Optional[int] = None) -> Any:
        """出勤率（対・当初シフト／対・変更後シフトの2系統）を取得する。

        Args:
            year: 年。省略時は今年。
            month: 月 (1-12)。省略時は今月。
        """
        return await api_client.get("/attendance-rate", params={"year": year, "month": month})

    @mcp.tool()
    async def get_monthly_contract_hours(year: int, month: int) -> Any:
        """アクティブな CA / IO の月別契約稼働時間を取得する。

        Args:
            year: 年 (例: 2026)
            month: 月 (1-12)
        """
        return await api_client.get("/user-monthly-work-hours", params={"year": year, "month": month})
