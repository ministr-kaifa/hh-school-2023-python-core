from datetime import datetime
import time

def log_call(target_function):
    def inner(*args, **kwargs):
        execution_start = time.perf_counter()
        print(f'info: {target_function.__name__} call at {datetime.now()}')
        result = target_function(*args, **kwargs)
        print(f'info: {target_function.__name__} execution time {time.perf_counter() - execution_start} seconds')
        return result
    
    return inner
