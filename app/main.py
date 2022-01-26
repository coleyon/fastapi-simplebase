from fastapi import FastAPI
from asyncio import sleep
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.get("/")
async def root():
    await sleep(1)
    return {"message": "Hello World"}


@app.get("/info")
async def info():
    await sleep(2)
    return {"message": "Info"}


@app.get("/login")
async def login():
    await sleep(3)
    return {"message": "Login"}


@app.get("/help")
async def help():
    await sleep(4)
    return {"message": "Help"}
