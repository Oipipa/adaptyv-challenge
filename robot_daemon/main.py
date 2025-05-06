import sys, threading, uvicorn
from .config import load_config
from .robot_api import RobotAPI
from .heartbeat import Heartbeat
from .server import create_app

def main() -> None:
    cfg = load_config(sys.argv[1] if len(sys.argv) > 1 else "config.yaml")
    robot = RobotAPI(cfg["robot"])
    hb = Heartbeat(robot, cfg["daemon"].get("heartbeat_interval", 30))
    hb.start()
    app = create_app(robot)
    uvicorn.run(app,
                host=cfg["daemon"].get("host", "0.0.0.0"),
                port=cfg["daemon"]["port"])

if __name__ == "__main__":
    main()
