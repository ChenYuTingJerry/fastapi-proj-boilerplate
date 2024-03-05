from typing import Literal

from pydantic import BaseModel, EmailStr, UUID4, PositiveInt


class User(BaseModel):
    user_id: UUID4
    name: str
    gender: Literal["male", "female"]
    age: PositiveInt
    email: EmailStr
