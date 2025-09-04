from typing import Dict, Any
from app.schema import Account


accounts: Dict[int, dict[str, Any]] = dict()


async def get_account(account_id: int) -> Account |  Dict[str, Any] | None:
    if account_id in accounts:
        return accounts[account_id]
    else:
        return None


async def modify_account(account_id: int, account: Account) -> Account | Dict[str, Any] | None:
    if account_id in accounts:
        accounts[account_id] = account.model_dump()
        return accounts[account_id]
    else:
        return None


async def add_account(account_id: int, account: Account) -> Account | Dict[str, Any] | None:
    if account_id in accounts:
        return None
    else:
        accounts[account_id] = account.model_dump()
        return accounts[account_id]
    

async def delete_account(account_id: int) -> bool | None:
    response = accounts.pop(account_id, None)
    return None if response == None else True