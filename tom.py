from fastapi import FastAPI
from requests import get

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/bye")
async def root():
    return {"message": "Goodbye World"}
