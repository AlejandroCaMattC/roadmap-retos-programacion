""" Python decorators"""


def print_call(func):
    def print_function():
        print(f"The function '{func.__name__}' was called")
        return func
    return print_function


@print_call
def example_function():
    pass


@print_call
def example_function2():
    pass


@print_call
def example_function3():
    pass


example_function()
example_function2()
example_function3()


"""Exercise"""


def call_counter(func):
    def counter():
        counter.calls += 1
        print(
            f"The function '{func.__name__}' was called {counter.calls} times")
        return func

    counter.calls = 0
    return counter


@call_counter
def example_function4():
    pass


@call_counter
def example_function5():
    pass


example_function4()
example_function4()
example_function4()
example_function5()
example_function5()
example_function4()
