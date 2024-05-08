import requests

url = 'http://localhost:5000/api/users'

user_info = {
    'username': 'serafina',
    'password': 'serafina',
    'email': 'serafina@gmail.com'
}

headers = {
    'Content-Type': 'Application/json',
}

response = requests.post(url, json=user_info, headers=headers)

print(response.json())


# def say_hello(name: str) -> str:
#     return f"Hello, {name}!"

# # Path: test/test.py
# def say_goodbye(name: str) -> str:
#     return f"Goodbye, {name}!"

# # Path: test/test.py
# def say_hello_and_goodbye(name: str) -> str:
#     return f"{say_hello(name)} {say_goodbye(name)}"

# # Path: test/test.py
# def say_hello_and_goodbye_twice(name: str) -> str:
#     return f"{say_hello_and_goodbye(name)} {say_hello_and_goodbye(name)}"

# # Path: test/test.py
# def say_hello_and_goodbye_thrice(name: str) -> str:
#     return f"{say_hello_and_goodbye_twice(name)} {say_hello_and_goodbye(name)}"

# square = lambda x : x ** 2

# print(square(5))