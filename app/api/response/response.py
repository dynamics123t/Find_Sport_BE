
def make_response_json(data, status: int, message: str):
    return {
        "data": data,
        "meta": {
            "status": status,
            "detail": message
        }
    }


def make_response_json_4_param(data, count: int, status: int, message: str):
    return {
        "data": data,
        "count": count,
        "meta": {
            "status": status,
            "detail": message
        }
    }