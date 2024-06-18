from typing import Literal

from pydantic import BaseModel, UUID4, PositiveInt, EmailStr


class User(BaseModel):
    user_id: UUID4
    name: str
    gender: Literal["male", "female"]
    age: PositiveInt
    email: EmailStr
