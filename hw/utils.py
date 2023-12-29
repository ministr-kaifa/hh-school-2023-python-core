from datetime import datetime

def log_call(target_function):
    def inner(self, *args, **kwargs):
        print(f'info: {self.__class__.__name__}.{target_function.__name__} call at {datetime.now()}')
        return target_function(self, *args, **kwargs)
    
    return inner
