from fastapi import FastAPI, Body
import uvicorn

app = FastAPI()
_state = {"status": "idle"}

@app.post("/robot/command")
async def cmd(c: dict = Body(...)):
    global _state
    _state = {"status": f"received {c['command']}"}
    return {"echo": c}

@app.get("/robot/state")
async def state():
    return _state

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
