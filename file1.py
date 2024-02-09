def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        value = original_func(*args, **kwargs)
        return list(map(lambda x: pow(x, 2), value))
    return wrapper_func


def decorator_func1(original_func):
    def wrapper_func(*args, **kwargs):
        value = original_func(*args, **kwargs)
        even_num = []
        for i in value:
            if i % 2 == 0:
                even_num.append(i)
        return even_num
    return wrapper_func


@decorator_func
@decorator_func1
def get_item(item):
    return item


print(get_item([i for i in range(1, 11)]))