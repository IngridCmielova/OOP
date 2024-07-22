from _datetime import datetime
# The decorator function
def add_asterisks(func):
    def wrapper():
        print("***************************")
        func()
        print("***************************")
    return wrapper

# The function to display the current time
def display_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)

# Decorating the function without using @ syntax
decorated_display_time = add_asterisks(display_time)

# Calling the decorated function
decorated_display_time()