import json


def json_cache(func: callable) -> callable:
    with open(f"{func.__name__}.json", 'r') as log:
        data = json.load(log)

    def wrapper(*args, **kwargs) -> None:
        temp_dict = {'args': args, 'kwargs': kwargs, 'result': func(*args, **kwargs)}
        data.append(temp_dict)
        with open(f"{func.__name__}.json", 'w') as log:
            json.dump(data, log, indent=4)

    return wrapper

@json_cache
def test(*args, **kwargs):
    return sum(args)

test(222, 444, 666)