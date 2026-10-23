"""
There are two types of arbitrary arguments in Python:

*args — for positional arguments (regular arguments)
**kwargs — for keyword arguments (arguments with names)
"""

#*args
#When you define a function using *args, Python will pack all the extra positional arguments into a tuple.

#no *args
def add(a, b):
    return a + b

def add_args(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add_args(1, 2, 3, 4, 5, 6))
print(add_args(1, 2, 3))

#side note: another place * shows up:
number = [1, 2, 3, 4, 5]
first, second, *rest = numbers
print(first)
print(second)
print(rest)

def print_class(teacher, *students):
    print(f"{teacher} is the teacher of the fallowing students")
    for s in students:
        print(s)

print_class("Mr. Christian lehman", "Jace", "Even", "Zach", "John", "Isaac", "K-luh")

#Arbitrary keyword arguments:
## ** tells python to pack all keyword arguments (those that use main = value) into a dictionary
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(
    name="Mr. boring",
    street="123 boring road",
    city = "boring city",
    states= "wyoming",
    zip="who cares"
    )



#combine *args and **kwargs
#combine *args and **kwargs
def shipping_label(*args, **kwargs):
    # Print the full name
    for arg in args:
        print(arg, end=" ")
    print()  # New line

    # Print the address
    if "apartment" in kwargs:
        print(f"{kwargs.get('street')}, Apartment #{kwargs.get('apartment')}")
    elif "PO_box" in kwargs:
        print(f"{kwargs.get('street')}, P.O. Box {kwargs.get('PO_box')}")
    else:
        print(kwargs.get("street"))

    # Print the city, state, and zip
    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label(
    "Dr.", "SpongeBob", "SquarePants", "III",
    street="123 Fake Street",
    apartment=100,
    city="Detroit",
    state="Michigan",
    zip="54321"
)