"""FastAPI HTTPクライアント"""
import os
from typing import Any, Optional

import httpx


class ApiClient:
    """RBPaaS Operation Hub APIクライアント"""

    def __init__(self):
        self.base_url = os.environ.get("RBPAAS_API_URL", "http://localhost:8080/api").rstrip("/")
        self.token = os.environ.get("RBPAAS_API_TOKEN", "")
        self._client: Optional[httpx.AsyncClient] = None

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                headers={"Authorization": f"Bearer {self.token}"},
                timeout=60.0,
            )
        return self._client

    async def get(self, path: str, params: Optional[dict[str, Any]] = None) -> Any:
        """GETリクエスト

        パスは Operation Hub のルート定義と末尾スラッシュまで一致させること。
        不一致だと 307 リダイレクトになり、転送先で Authorization が落ちる。

        HTTPエラーは例外にせず {"error": ...} を返す。403（権限不足）などを
        Claude が利用者にそのまま説明できるようにするため。
        """
        client = await self._get_client()
        # None値のパラメータを除外
        if params:
            params = {k: v for k, v in params.items() if v is not None}
        response = await client.get(path, params=params)
        if response.is_error:
            try:
                detail = response.json().get("detail")
            except ValueError:
                detail = response.text[:500]
            hint = None
            if response.status_code == 401:
                hint = "APIトークンが無効または期限切れです。管理者に再発行を依頼してください。"
            elif response.status_code == 403:
                hint = "このデータはトークンの権限では取得できません。admin スコープのトークンが必要です。"
            return {
                "error": True,
                "status": response.status_code,
                "path": path,
                "detail": detail,
                "hint": hint,
            }
        return response.json()

    async def close(self):
        if self._client and not self._client.is_closed:
            await self._client.aclose()


# シングルトン
api_client = ApiClient()
