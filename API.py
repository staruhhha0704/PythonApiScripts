import uvicorn

from fastapi import FastAPI, Response
from fastapi.params import Body

app = FastAPI(debug=True)

@app.get("/")
def root():
    return {"message" : "Hello, students"}

@app.get("/hello/{name}")
def say_hello_by_name(name: str):
    return {"message" : f"Hello {name}"}



if __name__ == "__main__":
    uvicorn.run(app, port=8001)