from typing import Annotated
from fastapi import FastAPI, Query, Path
import random
from pydantic import BaseModel

app = FastAPI()
# PATH parameter, QUERY parameter
# PATH parameter -> parameter yg dideklarasikan kedalam routing aplikasi kita


class User(BaseModel):
    name: str
    age: int


class Product(BaseModel):
    name: str
    description: str
    price: int  # rupiah
    quantity: int
    is_new: bool


#           0                       1               2                   3
datas = [
    User(name="John", age=23),
    User(name="Jane", age=28),
    User(name="Jack", age=26),
    User(name="Jill", age=30),
]

products = [
    Product(name="p1", description="desc1", price=1000, quantity=10, is_new=True),
]


@app.get("/")
def homepage():
    return {"Hellow": "Worldabc"}


@app.get("/hello/{name}")
def greet_name(name: Annotated[str, Path(min_length=3, max_length=6)]):
    return {"Hellow": name}


@app.get("/get/me")
def get_me():
    return {"me": "rwid"}


@app.get("/get/all")
def get_all():
    return datas


# PATH parameter -> parameter yg dideklarasikan kedalam routing aplikasi kita lalu ditembak ke dalam func call dibawahnya
# QUERY parameter -> parameter yg TIDAK dideklarasikan kedalam routing aplikasi kita, tapi dideklarasikan kedalam routing call function kita


@app.get("/get/{uid}")  # /me -> {"Hellow" : "me"} -> uid -> user id
def get_user(
    uid: Annotated[int, Path(description="The ID of the user to get", ge=0)],
    get_age: Annotated[
        bool,
        Query(
            alias="Do you want to get age?",
            description="This is to get the age of the user",
        ),
    ] = False,
):
    user = datas[uid]
    return {"Hellow": user.name, "age": user.age if get_age is True else None}


@app.post("/create/{name}")
def create_user(name: str):
    new_user = User(name=name, age=random.randint(10, 30))
    datas.append(new_user)
    return f"ok, user {new_user.name} added"


@app.post("/product/create/")
def create_product(product: Product | None = None):
    if product:
        products.append(product)
        return f"ok, product {product.name} added"
    else:
        return "product not added"


@app.get("/product/get_all_products")
def get_products():
    return products
