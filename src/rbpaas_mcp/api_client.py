"""FastAPI HTTPクライアント"""
import os
from typing import Any, Optional

import httpx


class ApiClient:
    """RBPaaS Operation Hub APIクライアント"""

    def __init__(self):
        self.base_url = os.environ.get("RBPAAS_API_URL", "http://localhost:8080/api")
        self.token = os.environ.get("RBPAAS_API_TOKEN", "")
        self._client: Optional[httpx.AsyncClient] = None

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                headers={"Authorization": f"Bearer {self.token}"},
                timeout=30.0,
            )
        return self._client

    async def get(self, path: str, params: Optional[dict[str, Any]] = None) -> dict:
        """GETリクエスト"""
        client = await self._get_client()
        # None値のパラメータを除外
        if params:
            params = {k: v for k, v in params.items() if v is not None}
        response = await client.get(path, params=params)
        response.raise_for_status()
        return response.json()

    async def close(self):
        if self._client and not self._client.is_closed:
            await self._client.aclose()


# シングルトン
api_client = ApiClient()
