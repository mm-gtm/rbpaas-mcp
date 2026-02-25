"""契約・ディール関連ツール"""
from typing import Optional

from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.api_client import api_client


def register(mcp: FastMCP):
    @mcp.tool()
    async def get_projects_with_deals(
        status: Optional[str] = None,
        is_active: Optional[bool] = True,
        skip: int = 0,
        limit: int = 100,
    ) -> dict:
        """プロジェクト一覧に TRUE OS ディール（契約金額）情報を結合して取得する。

        各プロジェクトの deal フィールドに契約金額 (total_amount)、顧客名、
        契約期間等が含まれる。deal が null の場合はディール未紐づけ。

        Args:
            status: ステータスでフィルタ (planning/active/completed/on_hold/cancelled)
            is_active: アクティブなプロジェクトのみ取得するか (デフォルト: True)
            skip: スキップ件数
            limit: 取得件数上限
        """
        return await api_client.get("/projects/with-deals", params={
            "status": status,
            "is_active": is_active,
            "skip": skip,
            "limit": limit,
        })

    @mcp.tool()
    async def get_true_os_deals(
        status: Optional[str] = None,
        product: Optional[str] = "Revenue BPaaS",
        phase: Optional[str] = "invoice",
    ) -> dict:
        """TRUE OS 上の全ディール（契約）一覧を取得する。

        プロジェクトとの紐づけに関係なく、TRUE OS Gateway に登録されている
        ディール情報を返す。契約金額・ステータス・フェーズ等を確認できる。

        Args:
            status: ステータスでフィルタ (draft/contracted/agreed/negotiating/paid/cancelled/invoiced)
            product: 商品名フィルタ (デフォルト: Revenue BPaaS)
            phase: フェーズフィルタ (estimate/invoice/application、デフォルト: invoice)
        """
        return await api_client.get("/true-os/deals", params={
            "status": status,
            "product": product,
            "phase": phase,
        })
