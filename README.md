# RBPaaS MCP Server

Claude Desktop から RBPaaS Operation Hub のデータにアクセスするための MCP サーバーです。

## セットアップ

### 1. APIトークンの発行

RBPaaS Operation Hub に管理者でログインし、APIトークンを発行してもらってください。

スコープは用途に合わせて選びます。

| スコープ | 取れるもの |
|---|---|
| `read` | ダッシュボード・プロジェクト・レポート・フィードバック・シフトなど、ログインユーザーなら誰でも見られるデータ |
| `admin` | 上記に加え、稼動モニタリング・活動停滞アラート・出勤率・CAレベル判定・CA報酬連絡票・最適化結果・ZoomPhone・Platform営業の提案書リンクなど IO/管理者向けのデータ |

権限が足りないツールは `{"error": true, "status": 403, ...}` を返し、Claude がその旨を説明します。

### 2. Claude Desktop 設定

Claude Desktop の設定ファイルに以下を追加します。

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "rbpaas-operation-hub": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/mm-gtm/rbpaas-mcp", "rbpaas-mcp"],
      "env": {
        "RBPAAS_API_URL": "https://your-api.run.app/api",
        "RBPAAS_API_TOKEN": "roh_xxxxx..."
      }
    }
  }
}
```

`RBPAAS_API_URL` と `RBPAAS_API_TOKEN` を実際の値に置き換えてください。

### 3. 前提条件

[uv](https://docs.astral.sh/uv/getting-started/installation/) がインストールされている必要があります。

```bash
# macOS
brew install uv
```

## 使えるツール

すべて読み取り専用です（データを書き換えるツールはありません）。Claude Desktop のチャットで自然に質問するだけで、適切なツールが呼ばれます。

| 領域 | ツール | 質問例 |
|---|---|---|
| 事業・KPI | get_business_overview<br>get_business_metrics<br>get_project_kpis<br>get_toss_details<br>get_project_efficiency<br>get_resource_utilization<br>get_supply_demand | 「今月の事業概況は？」「今年の月次売上推移」 |
| 活動データ | get_project_activity<br>get_daily_activity<br>get_depot_data | 「○○PJの今月の活動実績」 |
| 個人KPI | get_member_kpis<br>get_member_daily_kpis<br>get_individual_kpi<br>get_sub_project_kpi | 「○○PJのメンバー別KPIは？」 |
| プロジェクト | get_project_list<br>get_project_detail<br>get_project_monthly_summary<br>get_project_monthly_target<br>get_project_target_change_logs<br>get_project_groups<br>get_project_group_detail<br>get_project_aggregates<br>get_resource_simulation_base | 「9月の月次目標と実績の一覧」 |
| 契約・財務 | get_projects_with_deals<br>get_true_os_deals<br>get_deals_by_projects<br>get_project_financials<br>get_contracted_amounts<br>get_target_alignment | 「9月に赤字のPJはどこ？」 |
| レポート | get_reports<br>get_report_detail<br>get_daily_reports<br>get_daily_report_detail<br>get_voc_reports<br>get_voc_report_detail<br>get_penetration_dimensions<br>get_penetration | 「○○PJの直近の週次レポートを要約して」 |
| 顧客フィードバック | get_customer_feedbacks<br>get_overdue_feedbacks<br>get_customer_feedback_detail | 「期限超過のフィードバックある？」 |
| 稼動・勤怠 | get_work_monitor<br>get_ca_activity_grid<br>get_activity_stall_alerts<br>get_attendance_rate<br>get_monthly_contract_hours<br>get_work_time_summary<br>get_daily_work_time<br>get_user_work_time_history<br>get_daily_work_records | 「今週の活動停滞アラートは？」「今月の出勤率」 |
| シフト・アサイン | get_schedules<br>get_schedule_change_requests<br>get_schedule_deadline_info<br>get_schedule_deadline_extensions<br>get_optimization_history<br>get_optimization_result<br>get_daily_assignments<br>suggest_dispatch_candidates | 「来月○○PJに入れられる候補は？」 |
| 人 | get_agents<br>get_users<br>get_user_detail<br>get_experience_matrix<br>get_experience_detail | 「退職者も含めたCA一覧」 |
| CA評価・報酬 | get_ca_evaluation_summary<br>get_ca_evaluation_history<br>get_ca_evaluation_detail<br>preview_ca_deal_targets<br>get_ca_promotion_candidates<br>get_ca_demotion_candidates<br>get_ca_raise_candidates<br>get_ca_level_change_history<br>get_ca_salary_change_history<br>get_ca_planning_alerts<br>get_ca_level_review_events<br>get_ca_level_review_detail<br>get_ca_compensation_sheets<br>get_ca_compensation_sheet_detail | 「今月の昇格候補は？」「9月の報酬連絡票の明細」 |
| ZoomPhone | get_zoom_phone_numbers<br>get_zoom_phone_users<br>get_zoom_phone_histories<br>get_zoom_phone_sync_status | 「○○PJに割り当てている番号は？」 |
| Platform営業 | get_proposal_links<br>get_proposal_link_detail<br>get_form_outreach_messages | 「今週発行した提案書リンクの反応」 |

含めていないもの（いずれも Operation Hub の画面上の業務データではないため）:

- 本人専用の画面（マイページ・CA個人ダッシュボード・打刻・自分のシフト）: APIトークンには「本人」がいないため呼べない
- 設定・連携の内部情報（APIトークン、システム設定、BigQuery設定、MMPアカウント紐付け、TRUE OS 紐付け候補など）
- 他ツールと同じ中身のもの（連絡票CSV＝連絡票明細と同内容、1件だけ取るAPIなど）と、社外向けの公開提案書URL

## 開発者向け

### ローカル実行

```bash
cd rbpaas-mcp
RBPAAS_API_URL=http://localhost:8080/api RBPAAS_API_TOKEN=roh_xxx uv run rbpaas-mcp
```

### Operation Hub 側の API と合っているか確かめる

全ツールが叩くパスを Operation Hub の実ルート（末尾スラッシュ込み）と照合する。
FastAPI は末尾スラッシュが違うと 307 を返し、転送先で Authorization が落ちるため、ずれると 401 になる。
Operation Hub に API を足したり変えたりしたら、このリポジトリのツールも合わせて直すこと。

### MCP Inspector でデバッグ

```bash
RBPAAS_API_URL=http://localhost:8080/api RBPAAS_API_TOKEN=roh_xxx npx @modelcontextprotocol/inspector uv run rbpaas-mcp
```
