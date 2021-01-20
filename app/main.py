from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from databases import Database
from pydantic import BaseModel
import aiosqlite
database = Database('sqlite:///./app.db')
app = FastAPI()



@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


@app.get('/')
async def fetch_data():
    query = "SELECT * FROM product"
    results = await database.fetch_all(query=query)
    return  results


@app.get("/Emi/")
async def emi_calculator(product_name: str,tenure: int,interest: int):
    query = 'SELECT * FROM product'
    results = await database.fetch_all(query=query)
    leng = len(results)
    print(leng)
    product_price = None
    for i in range(leng):
        if results[i]['product_name']== product_name:
            product_price = results[i]['price']
    if product_price is None:
        return "Invalid Product Details"
    r = (interest/12)/100
    Emi = round((product_price*r*(1+r)**tenure)/((1+ r)**tenure - 1),2)
    data = [{"product_name": product_name,"tenure": tenure,"Interest":interest,"Emi": Emi}]
    return data
