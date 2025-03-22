import requests
from fastapi import FastAPI,Query

solver = FastAPI()

@solver.get("/")
def p():
    return "test"

@solver.get("/solve")
def solve(query:str=Query(...,description="send prompt")):
    ollamaurl = "http://localhost:11434/api/generate"

    payload = {
        "model":"qwen:2.5",
        "prompt":query,
        "stream":False
    }
    response = requests.post(ollamaurl,json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
            return {"error":{response.status_code}}

