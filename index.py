from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="AF Product")

class Product(BaseModel):
    id:int
    name: str
    price: int

products: List[Product] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to Automaion Feed Product suite"}

@app.get("/products")
def get_products():
    return products

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product
    return {"error": "Product not found"}

@app.delete("/product/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            deleted = products.pop(index)
            return deleted
    return {"error": "Product not found"}
