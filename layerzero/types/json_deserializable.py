import json

from typing import Dict, Any


class JsonDeserializable:
    raw = None

    @classmethod
    def de_json(cls, raw_json: Any):
        raise NotImplementedError

    @staticmethod
    def check_json(raw_json: Any) -> Dict:
        if type(raw_json) == dict:
            return raw_json
        elif type(raw_json) == str:
            return json.loads(raw_json)
        else:
            raise ValueError("raw_json should be a json dict or string.")
