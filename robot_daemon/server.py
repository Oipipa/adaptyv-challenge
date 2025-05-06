from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

def create_app(robot):
    app = FastAPI()

    class Command(BaseModel):
        command: str
        args: dict | None = None

    @app.post("/command")
    async def command(cmd: Command):
        try:
            return {"result": robot.send_command(cmd.dict())}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.get("/status")
    async def status():
        st = robot.last_state()
        return {"state": st}

    return app
