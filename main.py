# main.py  
from time import time
from fastapi import FastAPI  

app = FastAPI() # This is what will be refrenced in config

database = {}

@app.get('/ping')
async def hello():
    return {'res': 'pong', "time": time()}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id in database:
        return {"item_id": item_id, "item_str": database[item_id]}
    else:
        return {"Response": "Nothing there..."}

@app.post("/items/{item_id}")
def upload_item(item_id: int, item_str: str):
    # database {item_id: item_str}
    database[item_id] = item_str
    return {"Response": "Upload Successful"}
