"""
In Python, keyword arguments are arguments that are preceded by an identifier (the parameter’s name) when you call a function.
They make your code easier to read and allow you to change the order of arguments when calling a function.
"""

def hello(greeting, title, first, last):
    print(greeting, title, first, last)


hello("Hello", "Mr.", "Even", "Burlingame")

hello("Even", "Hello", "Burlingame", "Mr")

hello(first = "Even", greeting = "Hello", last = "Burlingame", title = "Mr.")

#Note: you can mix, but positionalargs must be first
hello("Hello", "Mr.", last="Burlingame", first="Even")