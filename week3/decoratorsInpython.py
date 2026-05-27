import time
from functools import wraps


def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Total time is {end - start} secs")

        return result

    return wrapper


def login(is_authenticated):

    def decorator(func):

        def wrapper(*args, **kwargs):

            print("Function Started")

            if is_authenticated:

                result = func(*args, **kwargs)

            else:

                print("Not Authenticated")
                return

            print("Function Ended")

            return result

        return wrapper

    return decorator

def retry(func):

    def wrapper(*args, **kwargs):

        last_exception = None

        for attempt in range(3):

            try:

                return func(*args, **kwargs)

            except Exception as e:

                last_exception = e

                print(f"Retry {attempt + 1} failed")
                time.sleep(5)

        raise last_exception

    return wrapper

def cache(func):

    value_cache={}
    def wrapper(*args,**kwargs):
            key=(args,tuple(kwargs.items()))
            if key in value_cache :
                print("Returning from cache")
                return value_cache[key]
            else :
                result=func(*args,**kwargs)
                value_cache[key]=result
                print("Computed and cached")
            
            return result
    return wrapper

def rate_limit(func):
    limit_counter=0
    def wrapper(*args,**kwargs):
        nonlocal limit_counter
        if limit_counter >= 3:
            print("Limit Exceeded")
            return
        else:
            result=func(*args,**kwargs)
            limit_counter+=1
        return result
    return wrapper




def debug(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"function calling with name {func.__name__} with {args} {kwargs}")
        result= func(*args,**kwargs)
        print(f"Result of the function is {result}")
        return result
    return wrapper

    

def validate_input(func):

    def wrapper(*args, **kwargs):

        if not args:

            print("Missing input")
            return

        value = args[0]

        if not isinstance(value, (int, float)):

            print("Only numeric input allowed")
            return

        if value <= 0:

            print("Negative or Zero values not allowed")
            return

        return func(*args, **kwargs)

    return wrapper

audit_logs = []

def audit_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        audit_logs.append({
            "function": func.__name__,
            "args": args,
            "kwargs": kwargs,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

        return func(*args, **kwargs)

    return wrapper

    
def permission_required(required_role):

    def decorator(func):

        def wrapper(user_role, *args, **kwargs):

            if user_role != required_role:

                print("Insufficient access")
                return

            return func(user_role, *args, **kwargs)

        return wrapper

    return decorator


@debug
@validate_input
@rate_limit
@audit_log
@cache
def rememberLastData(x):

    return 100/x



@retry
def unstable_api():
    return 1990/0
@permission_required("accounts")
@login(False)
def viewProfile(user_role):
    print("Ur profle looks good")

@timer
@permission_required("admin")
@login(True)
def transferMoney(user_role):
    print("Money transferred")



print(transferMoney("admin"))
print(viewProfile("admin"))
# print(unstable_api())
print(rememberLastData(0))
print(rememberLastData(20))
print(rememberLastData(20))
print(rememberLastData(20))
print(audit_logs)


