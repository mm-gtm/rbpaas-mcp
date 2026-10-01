"""Platform営業（提案書・フォーム送信）関連ツール"""
from typing import Any

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_proposal_links(q: str = "", source: str = "all", page: int = 1, page_size: int = 50) -> Any:
        """発行済みの提案書リンク一覧（新しい順）を取得する。

        Args:
            q: 会社名・宛先・社内メモの部分一致
            source: 発行元で絞る (proposal=初期提案書 / form=フォーム送信 / all)
            page: ページ番号
            page_size: 1ページの件数
        """
        return await api_client.get("/proposal-links", params={
            "q": q, "source": source, "page": page, "page_size": page_size,
        })

    @mcp.tool()
    async def get_proposal_link_detail(proposal_id: str) -> Any:
        """提案書リンクの詳細（反応の履歴つき）を取得する。

        Args:
            proposal_id: 提案書リンクID
        """
        return await api_client.get(f"/proposal-links/{proposal_id}")

    @mcp.tool()
    async def get_form_outreach_messages(q: str = "", missing_body: bool = False, page: int = 1, page_size: int = 50) -> Any:
        """フォーム送信用に作成した投稿文の履歴（新しい順）を取得する。

        Args:
            q: 会社名・宛名・フォームURLの部分一致
            missing_body: 投稿文がまだ無い記録だけに絞る
            page: ページ番号
            page_size: 1ページの件数
        """
        return await api_client.get("/form-messages", params={
            "q": q, "missing_body": missing_body, "page": page, "page_size": page_size,
        })
