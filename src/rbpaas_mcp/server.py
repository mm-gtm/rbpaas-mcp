"""MCP Server セットアップ"""
from mcp.server.fastmcp import FastMCP

from rbpaas_mcp.tools import (
    agents,
    ca_levels,
    contracts,
    dashboard,
    feedbacks,
    financials,
    members,
    operations,
    optimization,
    platform_sales,
    projects,
    reports,
    schedules,
    work_time,
)

mcp = FastMCP(
    "RBPaaS Operation Hub",
    instructions=(
        "Revenue BPaaS オペレーション管理システム（Operation Hub）のデータを読み取り専用で照会するMCPサーバー。"
        "事業KPI・売上、プロジェクトと月次目標、PJ別粗利、定例/デイリー/VoCレポート、顧客フィードバック、"
        "CAの稼動・出勤率・活動停滞アラート、シフト、アサイン最適化、CAレベル判定、Platform営業の提案書リンクを扱う。"
        "プロジェクトIDやユーザーIDが分からないときは、まず get_project_list / get_users で確認する。"
        "KPI用語: ACT=活動数（電話+受電+メール+スレッド+その他）、DMR=接触、TOSS=商談化。"
        "結果に error: true が含まれる場合は status と hint を利用者にそのまま伝える。"
    ),
)

# ツール登録
for module in (
    dashboard,
    projects,
    members,
    contracts,
    financials,
    reports,
    feedbacks,
    operations,
    work_time,
    schedules,
    optimization,
    agents,
    ca_levels,
    platform_sales,
):
    module.register(mcp)


def main():
    mcp.run(transport="stdio")
