import time, threading

class Heartbeat(threading.Thread):
    def __init__(self, robot, interval: int):
        super().__init__(daemon=True)
        self.robot = robot
        self.interval = interval
        self._stop = threading.Event()

    def run(self) -> None:
        while not self._stop.is_set():
            try:
                self.robot.get_state()
            except Exception:
                pass
            time.sleep(self.interval)

    def stop(self):
        self._stop.set()
