from pydantic import BaseModel


class Account(BaseModel):
    name: str
    description: str | None = None
    balance: float
    active: bool = True


class AccountResponse(BaseModel):
    name: str
    description: str | None = None
    balance: float
    active: bool = True


class AccountDeleteResponse(BaseModel):
    msg: str = "Successful"
    

class HealthStatusResponse(BaseModel):
    status: bool = True