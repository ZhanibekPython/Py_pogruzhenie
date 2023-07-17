def count_starts(num):
    count_lst = []

    def dcrtr(func: callable) -> callable:
        def inner_func(*args, **kwargs):
            for _ in range(num):
                count_lst.append(func(*args, **kwargs))
            return count_lst
        return inner_func
    return dcrtr

@count_starts(10)
def check(*args, **kwargs):
    return args




