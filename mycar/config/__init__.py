import pathlib
import json

with open(pathlib.Path(__file__).parent / "env.json") as f:
    env=json.load(f)