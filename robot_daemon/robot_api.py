import socket, requests, threading, json

class RobotAPI:
    def __init__(self, cfg: dict):
        self.cfg = cfg
        self._state_lock = threading.Lock()
        self._last_state: str | dict | None = None

    def send_command(self, cmd: dict):
        mode = self.cfg["mode"]
        if mode == "rest":
            return requests.post(self.cfg["rest"]["url"], json=cmd, timeout=5).json()
        with socket.create_connection((self.cfg["telnet"]["host"],
                                       self.cfg["telnet"]["port"]), timeout=5) as s:
            s.sendall((cmd["command"] + "\n").encode())
            return s.recv(4096).decode()

    def get_state(self):
        mode = self.cfg["mode"]
        if mode == "rest":
            state = requests.get(self.cfg["rest"]["state_url"], timeout=5).json()
        else:
            with socket.create_connection((self.cfg["telnet"]["host"],
                                           self.cfg["telnet"]["port"]), timeout=5) as s:
                s.sendall(b"STATE\n")
                state = s.recv(4096).decode()

        with self._state_lock:
            self._last_state = state
        return state


    def last_state(self):
        with self._state_lock:
            return self._last_state
