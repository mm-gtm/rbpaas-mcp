"""ZoomPhone（電話番号管理）関連ツール"""
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_zoom_phone_numbers(
        status: Optional[str] = None,
        site_name: Optional[str] = None,
        project_id: Optional[str] = None,
        assignee_type: Optional[str] = None,
        reusable: Optional[bool] = None,
        skip: int = 0,
        limit: int = 100,
    ) -> Any:
        """ZoomPhone の電話番号一覧（割当先PJ・状態）を取得する。

        Args:
            status: ステータスで絞る
            site_name: サイト名で絞る
            project_id: プロジェクトIDで絞る (UUID)
            assignee_type: アサインタイプで絞る
            reusable: 再利用可否で絞る
            skip: スキップ件数
            limit: 取得件数上限 (最大1000)
        """
        return await api_client.get("/zoom-phone/numbers", params={
            "status": status,
            "site_name": site_name,
            "project_id": project_id,
            "assignee_type": assignee_type,
            "reusable": reusable,
            "skip": skip,
            "limit": limit,
        })

    @mcp.tool()
    async def get_zoom_phone_users(search: Optional[str] = None, skip: int = 0, limit: int = 100) -> Any:
        """ZoomPhone のユーザー一覧を取得する。

        Args:
            search: メール・表示名で検索
            skip: スキップ件数
            limit: 取得件数上限 (最大1000)
        """
        return await api_client.get("/zoom-phone/users", params={"search": search, "skip": skip, "limit": limit})

    @mcp.tool()
    async def get_zoom_phone_histories(
        phone_number: Optional[str] = None,
        target_user_id: Optional[str] = None,
        project_id: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        skip: int = 0,
        limit: int = 100,
    ) -> Any:
        """ZoomPhone 電話番号のアサイン履歴を取得する。

        Args:
            phone_number: 電話番号で絞る
            target_user_id: ZoomユーザーIDで絞る
            project_id: プロジェクトIDで絞る (UUID)
            from_date: 開始日時 (YYYY-MM-DDTHH:MM:SS)
            to_date: 終了日時 (YYYY-MM-DDTHH:MM:SS)
            skip: スキップ件数
            limit: 取得件数上限 (最大1000)
        """
        return await api_client.get("/zoom-phone/histories", params={
            "phone_number": phone_number,
            "target_user_id": target_user_id,
            "project_id": project_id,
            "from_date": from_date,
            "to_date": to_date,
            "skip": skip,
            "limit": limit,
        })

    @mcp.tool()
    async def get_zoom_phone_sync_status() -> Any:
        """ZoomPhone との同期ステータス（最終同期日時など）を取得する。"""
        return await api_client.get("/zoom-phone/sync/status")
