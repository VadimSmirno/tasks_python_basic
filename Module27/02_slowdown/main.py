import time

def decorator_taime(func):
    def wrapped_func(*args,**kwargs):
        time.sleep(5)
        res = func(*args,**kwargs)
        return res
    return wrapped_func

@decorator_taime
def main_function(name:str):
    return f'Привет, {name}'

print (main_function('Вася'))