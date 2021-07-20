from typing import Any
from flask import jsonify


def data(arg: Any) -> Any:
    return jsonify({"data": arg})