from fastapi import APIRouter, Request, status
from app.schema import Account, AccountDeleteResponse, AccountResponse
from app.exceptions import AccountExist, AccountNotFound
from app.services import get_account, add_account, modify_account, delete_account


router = APIRouter()


@router.get("/accounts/{account_id}", 
         response_model=AccountResponse, 
         status_code=status.HTTP_200_OK)
async def read_account(account_id: int):
    res = await get_account(account_id)
    if res is None:
        raise AccountNotFound()
    else:
        return res
    

@router.post("/accounts/{account_id}", 
         status_code=status.HTTP_201_CREATED, 
         response_model=AccountResponse)
async def create_account(account_id: int, account: Account):
    res = await add_account(account_id, account)
    if res is None:
        raise AccountExist()
    else:
        return res
    

@router.patch("/accounts/{account_id}", 
        status_code=status.HTTP_202_ACCEPTED, 
        response_model=AccountResponse)
async def update_account(account_id: int, account: Account):
    res = await modify_account(account_id, account)
    if res is None:
        raise AccountNotFound()
    else:
        return res


@router.delete("/accounts/{account_id}", 
            status_code=status.HTTP_200_OK,
            response_model=AccountDeleteResponse)
async def remove_account(account_id: int):
    res = await delete_account(account_id)
    if res is None:
        raise AccountNotFound()
    else:
        return AccountDeleteResponse()
