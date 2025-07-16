import json
import os
import pathlib
from typing import Any

BASE_PATH = pathlib.Path(__file__).parent.parent


def load_json(path: str) -> dict[str, Any]:
    with open(os.path.join(BASE_PATH, path)) as f:
        return json.load(f)
