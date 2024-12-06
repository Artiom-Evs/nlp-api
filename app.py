from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hello")
async def hello_world():
    return {"message": "Hello, World!"}
