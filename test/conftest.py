from httpx import ASGITransport, AsyncClient
from collections.abc import AsyncIterator
from fastapi import FastAPI
from app.main import app
import pytest_asyncio
from asgi_lifespan import LifespanManager
    

@pytest_asyncio.fixture()
async def client() -> AsyncIterator[AsyncClient]:
    async with LifespanManager(app):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as _client:
            try:
                yield _client
            except Exception as exc:
                print(exc)
            finally:
                pass
