from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "get your temperature"}


@app.get("/gettemp")
async def gettemp():
    return {"temp": 27.5, "humidity": 70.0}
