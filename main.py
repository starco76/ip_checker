from typing import Union

from fastapi import FastAPI,Response
from pydantic import BaseModel
import platform ,subprocess
import uvicorn

async def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '5', host]
    return subprocess.call(command) == 0


app = FastAPI()

class data(BaseModel):
    password:str
    ip:str
@app.post("/")
async def read_root(data:data):
    res=False
    if data.password!='Xa4]:K%3OD0s':return Response('404',404)
    res=await ping(data.ip)
    return {"status": res}

if __name__ == "__main__":
    uvicorn.run(app,host='0.0.0.0',port=5050)
