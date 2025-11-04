from fastapi import FastAPI
from API.routers import symbol_data

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(symbol_data.router)