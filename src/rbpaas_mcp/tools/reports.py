"""レポート（定例・デイリー・VoC）関連ツール"""
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_reports(project_id: Optional[str] = None, limit: int = 20, offset: int = 0) -> Any:
        """生成済みの定例レポート（日次/週次/月次）の一覧を取得する。本文は get_report_detail で取る。

        Args:
            project_id: プロジェクトIDでフィルタ (UUID)
            limit: 取得件数 (最大100)
            offset: オフセット
        """
        return await api_client.get("/reports", params={"project_id": project_id, "limit": limit, "offset": offset})

    @mcp.tool()
    async def get_report_detail(report_id: str) -> Any:
        """定例レポートの詳細（各モジュールの内容）を取得する。

        Args:
            report_id: レポートID (UUID)
        """
        return await api_client.get(f"/reports/{report_id}")

    @mcp.tool()
    async def get_penetration_dimensions(project_id: str) -> Any:
        """浸透率を集計できる軸（リスト区分などMMPの選択項目）の候補を取得する。get_penetration の前に呼ぶ。

        Args:
            project_id: プロジェクトID (UUID)
        """
        return await api_client.get("/reports/penetration/dimensions", params={"project_id": project_id})

    @mcp.tool()
    async def get_penetration(project_id: str, source: str, field_id: str, as_of: Optional[str] = None) -> Any:
        """指定した軸でリストの浸透率（接触済み・商談化の割合）を集計する。

        Args:
            project_id: プロジェクトID (UUID)
            source: get_penetration_dimensions が返す source
            field_id: get_penetration_dimensions が返す field_id
            as_of: 累積の基準日 (YYYY-MM-DD)。省略時は本日(JST)。
        """
        return await api_client.get("/reports/penetration", params={
            "project_id": project_id, "source": source, "field_id": field_id, "as_of": as_of,
        })

    @mcp.tool()
    async def get_daily_reports(project_id: Optional[str] = None, limit: int = 30, offset: int = 0) -> Any:
        """デイリー活動報告の履歴一覧を取得する。

        Args:
            project_id: プロジェクトIDでフィルタ (UUID)
            limit: 取得件数 (最大100)
            offset: オフセット
        """
        return await api_client.get("/daily-reports", params={"project_id": project_id, "limit": limit, "offset": offset})

    @mcp.tool()
    async def get_daily_report_detail(report_id: str) -> Any:
        """デイリー活動報告の詳細を取得する。

        Args:
            report_id: デイリー活動報告ID (UUID)
        """
        return await api_client.get(f"/daily-reports/{report_id}")

    @mcp.tool()
    async def get_voc_reports(project_id: str) -> Any:
        """プロジェクトの VoC（顧客の声）レポート一覧を取得する。本文は get_voc_report_detail で取る。

        Args:
            project_id: プロジェクトID (UUID)
        """
        return await api_client.get("/voc/reports", params={"project_id": project_id})

    @mcp.tool()
    async def get_voc_report_detail(report_id: str) -> Any:
        """VoC（顧客の声）レポートの本文を取得する。

        Args:
            report_id: VoCレポートID (UUID)
        """
        return await api_client.get(f"/voc/reports/{report_id}")
