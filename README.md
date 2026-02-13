# RBPaaS MCP Server

Claude Desktop から RBPaaS Operation Hub のデータにアクセスするための MCP サーバーです。

## セットアップ

### 1. APIトークンの発行

RBPaaS Operation Hub に管理者でログインし、APIトークンを発行してもらってください。

### 2. Claude Desktop 設定

Claude Desktop の設定ファイルに以下を追加します。

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "rbpaas-operation-hub": {
      "command": "uvx",
      "args": ["--from", "git+ssh://git@github.com/mm-gtm/rbpaas-mcp", "rbpaas-mcp"],
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

Claude Desktop のチャットで自然に質問するだけで、適切なツールが自動的に呼び出されます。

| ツール | 説明 | 質問例 |
|--------|------|--------|
| `get_business_overview` | 事業全体KPI・アラート | 「今月の事業概況を教えて」 |
| `get_project_kpis` | PJ別KPI達成率 | 「各プロジェクトのKPI達成状況は？」 |
| `get_resource_utilization` | リソース稼働率 | 「エージェントの稼働率を見せて」 |
| `get_project_efficiency` | PJ別効率指標 | 「プロジェクトごとの効率はどう？」 |
| `get_project_list` | プロジェクト一覧 | 「アクティブなプロジェクト一覧」 |
| `get_project_detail` | プロジェクト詳細 | 「○○プロジェクトの詳細を教えて」 |
| `get_member_kpis` | メンバー別KPI | 「○○PJのメンバー別KPIは？」 |
| `get_customer_feedbacks` | フィードバック一覧 | 「顧客フィードバックの状況は？」 |
| `get_overdue_feedbacks` | 期限超過FB | 「期限超過のフィードバックある？」 |
| `get_optimization_history` | 最適化履歴 | 「最適化の実行履歴を見せて」 |
| `get_optimization_result` | 最適化結果詳細 | 「直近の最適化結果の詳細」 |
| `get_schedules` | スケジュール | 「今週のスケジュールを教えて」 |
| `get_work_time_summary` | 勤務時間 | 「今月の勤務時間サマリー」 |
| `get_agents` | エージェント一覧 | 「コールエージェントの一覧」 |

## 開発者向け

### ローカル実行

```bash
cd rbpaas-mcp
RBPAAS_API_URL=http://localhost:8080/api RBPAAS_API_TOKEN=roh_xxx uv run rbpaas-mcp
```

### MCP Inspector でデバッグ

```bash
RBPAAS_API_URL=http://localhost:8080/api RBPAAS_API_TOKEN=roh_xxx npx @modelcontextprotocol/inspector uv run rbpaas-mcp
```
