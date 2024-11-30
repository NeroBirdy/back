import logging
import aiohttp


from urllib.parse import urljoin, quote_plus, urlparse
from typing import List, Dict, Optional
import schemas as api_integration_schemas

__all__ = [
    "VKS",
    "VKSException",
    "VKSConnectionException",
]


import aiohttp
import logging
from urllib.parse import urljoin
from typing import Dict, Optional

class VKSException(Exception):
    """Кастомное исключение для ошибок VKS API"""
    pass

class VKSConnectionException(Exception):
    """Кастомное исключение для ошибок соединения"""
    pass

class VKS:

    def __init__(
        self,
        url: str = "https://test.vcc.uriit.ru/api/",
        timeout: int = 10,
    ):
        self.__url = url
        self.__sess = None
        self.__time = timeout

    async def init_session(self):
        if self.__sess is None or self.__sess.closed:
            self.__sess = aiohttp.ClientSession()
            logging.debug("Initialized aiohttp.ClientSession")

    async def close_session(self, *_):
        if self.__sess and not self.__sess.closed:
            await self.__sess.close()
            logging.debug("Closed aiohttp.ClientSession")

    @staticmethod
    def check_response(content: Dict) -> Dict:
        error_map = {
            401: "Unauthorized: Please check your credentials.",
            403: "No permission: Access denied.",
            404: "Object not found: The requested resource doesn't exist.",
            409: "Conflict: User with the specified login or email already exists.",
            410: "Gone: The resource has expired or is no longer available.",
            422: "Validation Error: Check the input data.",
        }

        if content.get("result") == "reject":
            raise VKSException(content.get("reason", "Request was rejected by the server."))
        if not content.get("success"):
            error_code = content.get("code")
            message = content.get("message", "Unknown error occurred.")
            if error_code and error_code in error_map:
                raise VKSException(error_map[error_code])
            raise VKSException(message)

        return content.get("data", {})

    def build_url(self, selector: str) -> str:
        return urljoin(f"{self.__url}", selector)

    async def request(
        self,
        selector: str,
        data: Optional[Dict] = None,
    ) -> Dict:
        await self.init_session()
        try:
            url = self.build_url(selector)
            if self.__sess is None:
                raise VKSConnectionException("Session is not initialized")
            async with self.__sess.post(
                url, json=data or {}, timeout=self.__time
            ) as response:
                logging.debug("Sending request to %s with data %s", url, data)
                json = await response.json()
                logging.debug("Received response: %s", json)
                return self.check_response(json)

        except aiohttp.ClientError:
            raise VKSConnectionException("API unavailable")

    async def __aenter__(self):
        await self.init_session()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close_session()
