from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/echo")
def echo(msg: str = "hello"):
    return {"echo": msg}
