"""最適化関連ツール"""
from typing import Optional

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_optimization_history(
        target_month: Optional[str] = None,
        skip: int = 0,
        limit: int = 20,
    ) -> dict:
        """アサイン最適化の実行履歴を取得する。

        Args:
            target_month: 対象月でフィルタ (YYYY-MM形式)
            skip: スキップ件数
            limit: 取得件数上限
        """
        return await api_client.get("/assignments/history", params={
            "target_month": target_month,
            "skip": skip,
            "limit": limit,
        })

    @mcp.tool()
    async def get_optimization_result(run_id: str) -> dict:
        """最適化結果の詳細を取得する。

        Args:
            run_id: 最適化実行ID (UUID)
        """
        return await api_client.get(f"/assignments/{run_id}")
