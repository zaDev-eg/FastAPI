from fastapi import FastAPI
from enum import Enum

## intiate the app instance 
app = FastAPI()

## stable instances for path parameter
class Items(str, Enum): 
    item1 = "Machine Learning"
    item2 = "Deep Learning"
    item3 = "Data Analysis"

## the intial EndPoint(Test Server Connection)
@app.get("/")
def test_server_connection(): 
    return {
        "message": "The server is up and running ✅"
    }
    
@app.get("/print-item/{item}")
def pitem(item: Items): 
    if item == Items.item1: 
        return {"item": item}
    elif item == Items.item2: 
        return {"item": item}
    else: 
        return {"item": item}