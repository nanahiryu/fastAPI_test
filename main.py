from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/fib")
async def fib(n: int=None):
    validate(n)
    ans: int = calc_fib(n)
    return {"result": ans}

def validate(n: int):
    if n is None:
        raise HTTPException(status_code=400, detail="クエリパラメータnが必要です")
    if n < 1:
        raise HTTPException(status_code=400, detail="nは1以上である必要があります")

def calc_fib(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return calc_fib(n - 1) + calc_fib(n - 2)