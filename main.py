# main.py  
from time import time
from fastapi import FastAPI  
from openai import OpenAI

client = OpenAI(
    api_key="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",
)

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

@app.post("/chat")
def chat(text: str):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
        model="gpt-3.5-turbo",
    )
    
    return response.choices[0].message.content
















#response = client.chat.completions.create(
#    messages=[
#        {
#            "role": "user",
#            "content": "안녕하세요 서울의 겨울 날씨가 어떤지 알고 싶어요. ",
#        }
#    ],
#    model="gpt-3.5-turbo",
#)

# print(response)

# print(response.choices[0].message.content)



