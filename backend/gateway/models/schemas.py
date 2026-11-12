from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class SignupSchema(BaseModel):
    fullname: str
    phone: str
    email: EmailStr
    password: str

class SigninSchema(BaseModel):
    username: str
    password: str

class UserInfoResponse(BaseModel):
    code: int
    fullname: Optional[str] = None
    role: Optional[int] = None
    menulist: Optional[list] = None

class SigninResponse(BaseModel):
    code: int
    jwt: Optional[str] = None
    role: Optional[int] = None
    message: Optional[str] = None