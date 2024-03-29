def say_hello(name: str) -> str:
    return f"Hello, {name}!"

# Path: test/test.py
def say_goodbye(name: str) -> str:
    return f"Goodbye, {name}!"

# Path: test/test.py
def say_hello_and_goodbye(name: str) -> str:
    return f"{say_hello(name)} {say_goodbye(name)}"

# Path: test/test.py
def say_hello_and_goodbye_twice(name: str) -> str:
    return f"{say_hello_and_goodbye(name)} {say_hello_and_goodbye(name)}"

# Path: test/test.py
def say_hello_and_goodbye_thrice(name: str) -> str:
    return f"{say_hello_and_goodbye_twice(name)} {say_hello_and_goodbye(name)}"