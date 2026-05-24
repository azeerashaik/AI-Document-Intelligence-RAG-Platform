from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class UserRegister(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str