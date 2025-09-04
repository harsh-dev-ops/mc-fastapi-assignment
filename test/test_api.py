from httpx import AsyncClient
import pytest
from pydantic import BaseModel
from fastapi import status


class SampleAccount(BaseModel):
    name: str = "test account"
    description: str | None = "test description"
    balance: float = 0.0
    active: bool = True
    

class TestHealthCheckApi:
    endpoint_url = '/api/v1/healthz'
    IS_APP_HEALTHY = True
    
    @pytest.mark.asyncio
    async def test_health(self, client: AsyncClient):
        response = await client.get(url=f"{self.endpoint_url}")
        data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert data['status'] == self.IS_APP_HEALTHY
        

class TestAccountsApi:
    enpoint_url = "/api/v1/accounts"
    accounts = {}
    account_data_columns = ['name', 'description', 'balance', 'active']
    account_id = 1
    sample_account = SampleAccount()
    random_account_id = 2

    @pytest.mark.asyncio
    async def test_create_account(self, client: AsyncClient):
        req_data = self.sample_account.model_dump(exclude_none=True)
        response = await client.post(url=f"{self.enpoint_url}/{self.account_id}", json=req_data)
        res_data = response.json() 
        assert response.status_code == status.HTTP_201_CREATED
        for col in self.account_data_columns:
            assert res_data[col] == req_data[col]
        self.accounts[self.account_id] = res_data

    @pytest.mark.asyncio
    async def test_create_duplicate_account(self, client: AsyncClient):
        req_data = self.sample_account.model_dump(exclude_none=True)
        response = await client.post(url=f"{self.enpoint_url}/{self.account_id}", json=req_data)
        assert response.status_code == status.HTTP_409_CONFLICT
        
    @pytest.mark.asyncio
    async def test_get_account(self, client: AsyncClient):
        req_data = self.sample_account.model_dump(exclude_none=True)
        response = await client.get(url=f"{self.enpoint_url}/{self.account_id}")
        assert response.status_code == status.HTTP_200_OK
        res_data = response.json() 
        assert response.status_code == status.HTTP_200_OK
        for col in self.account_data_columns:
            assert res_data[col] == req_data[col]
    
    @pytest.mark.asyncio
    async def test_account_not_found(self, client: AsyncClient):
        response = await client.get(url=f"{self.enpoint_url}/{self.random_account_id}")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        
    @pytest.mark.asyncio
    async def test_delete_account_not_found(self, client: AsyncClient):
        response = await client.delete(url=f"{self.enpoint_url}/{self.random_account_id}")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        
    @pytest.mark.asyncio
    async def test_update_account_not_found(self, client: AsyncClient):
        req_data = self.sample_account.model_dump(exclude_none=True)
        response = await client.patch(url=f"{self.enpoint_url}/{self.random_account_id}", json=req_data)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        
    @pytest.mark.asyncio
    async def test_update_account(self, client: AsyncClient):
        req_data = self.sample_account.model_dump(exclude_none=True)
        response = await client.patch(url=f"{self.enpoint_url}/{self.account_id}", json=req_data)
        assert response.status_code == status.HTTP_202_ACCEPTED

    @pytest.mark.asyncio
    async def test_delete_account(self, client: AsyncClient):
        response = await client.delete(url=f"{self.enpoint_url}/{self.account_id}")
        assert response.status_code == status.HTTP_200_OK
