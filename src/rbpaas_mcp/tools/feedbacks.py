"""顧客フィードバック関連ツール"""
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_customer_feedbacks(
        project_id: Optional[str] = None,
        status: Optional[str] = None,
        category: Optional[str] = None,
        assignee_id: Optional[str] = None,
        overdue_only: bool = False,
    ) -> Any:
        """顧客フィードバック一覧を取得する。

        Args:
            project_id: プロジェクトIDでフィルタ
            status: ステータスでフィルタ (pending_review/open/in_progress/resolved/wont_do)
            category: カテゴリでフィルタ (feature_request/bug_report/inquiry/complaint/action_item)
            assignee_id: 担当者IDでフィルタ
            overdue_only: 期限超過のみ取得 (デフォルト: False)
        """
        return await api_client.get("/customer-feedbacks/", params={
            "project_id": project_id,
            "status": status,
            "category": category,
            "assignee_id": assignee_id,
            "overdue_only": overdue_only,
        })

    @mcp.tool()
    async def get_overdue_feedbacks() -> Any:
        """期限超過の顧客フィードバックを取得する。"""
        return await api_client.get("/customer-feedbacks/overdue")

    @mcp.tool()
    async def get_customer_feedback_detail(feedback_id: str) -> Any:
        """顧客フィードバックの詳細を取得する。

        Args:
            feedback_id: フィードバックID (UUID)
        """
        return await api_client.get(f"/customer-feedbacks/{feedback_id}")
