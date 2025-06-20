from pydantic import BaseModel


class LoginUser(BaseModel):
    email: str
    phrase: str
