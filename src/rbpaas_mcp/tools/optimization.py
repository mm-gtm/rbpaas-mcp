"""アサイン最適化関連ツール"""
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_optimization_history(
        target_month: Optional[str] = None,
        skip: int = 0,
        limit: int = 20,
    ) -> Any:
        """アサイン最適化の実行履歴を取得する。

        Args:
            target_month: 対象月でフィルタ (YYYY-MM形式)
            skip: スキップ件数
            limit: 取得件数上限
        """
        return await api_client.get("/assignments/history", params={
            "target_month": target_month, "skip": skip, "limit": limit,
        })

    @mcp.tool()
    async def get_optimization_result(run_id: str) -> Any:
        """最適化結果の詳細（全員の主/従アサイン）を取得する。

        Args:
            run_id: 最適化実行ID (UUID)
        """
        return await api_client.get(f"/assignments/{run_id}")

    @mcp.tool()
    async def get_daily_assignments(start_date: str, end_date: str) -> Any:
        """期間内の全ユーザーの日次アサイン（誰がどのPJに入るか）を取得する。

        Args:
            start_date: 開始日 (YYYY-MM-DD)
            end_date: 終了日 (YYYY-MM-DD)
        """
        return await api_client.get("/assignments/daily/all", params={"start_date": start_date, "end_date": end_date})

    @mcp.tool()
    async def suggest_dispatch_candidates(project_id: str, target_month: str, top_n: int = 10) -> Any:
        """指定PJに向くエージェント候補をスコア順に取得する（ディスパッチ提案）。

        Args:
            project_id: プロジェクトID (UUID)
            target_month: 対象月 (YYYY-MM)
            top_n: 候補数 (最大50)
        """
        return await api_client.get("/assignments/dispatch/suggest", params={
            "project_id": project_id, "target_month": target_month, "top_n": top_n,
        })
