# main.py  
from time import time
from fastapi import FastAPI  

app = FastAPI() # This is what will be refrenced in config

@app.get('/ping')
async def hello():
    return {'res': 'pong', "time": time()}

@app.get('/test-api')
async def test_api():
    return {"Hello": "World"}
