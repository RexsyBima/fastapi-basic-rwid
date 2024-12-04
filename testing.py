from pydantic import BaseModel


class User(BaseModel):
    name: str


# u1 = User(name=123)
# print(u1)
