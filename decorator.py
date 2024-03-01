# A decorator is a function that extends the functionality of another
# function wihtout directly modifying that function


def say_bye_after_greet(fn):
    def wrapper(*args, **kwargs):
        print("Before hello!!!!")
        fn(*args, **kwargs)
        print("Byeee!!!!")

    return wrapper


@say_bye_after_greet
def greet(name):
    print(f"Hello!!!! {name}")


greet("John")
# say_bye_after_greet(greet)
# returned_wrapper_function = say_bye_after_greet(greet)
# returned_wrapper_function()
