from typing import Any
from flask import jsonify


def empty(arg: Any) -> Any:
    return jsonify({})