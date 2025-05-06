import yaml, pathlib, sys

BASE = pathlib.Path(getattr(sys, "_MEIPASS", pathlib.Path(__file__).parent.parent))
def load_config(path: str = "config.yaml") -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)
