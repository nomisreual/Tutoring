# Lists: collection of values:

lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst_2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
lst_3 = [1, True, "Hello"]

# Looping using for:
for item in lst_1:
    print(item)

# Looping using for with index:
for idx in range(len(lst_1)):
    print(lst_1[idx])

# Looping with while:
idx = 0
while True:
    if idx == len(lst_1):
        break
    print(lst_1[idx])
    idx += 1

# Dictionaries: collection of key, value pairs.
# important: keys need to be immutable!
dictionary_1 = {
    "name": "Simon",
    "age": 33,
    "favorite_language": "Python"
}

# Looping over dictionaries to access keys and/or values:

# Access the keys:
for key in dictionary_1:
    print(key)
# Access values:
for value in dictionary_1.values():
    print(value)
# Access both at the same time:
for key, value in dictionary_1.items():
    print(f"key: {key}, value: {value}")

# Nested structures:
# @Vitaly suggested a list of dictionaries in another list of dictionaries.

# Let's create a function that creates a dictionary like the
# one above:


def person(name: str, age: int, favorite_language: str) -> dict:
    return {
        "name": name,
        "age": age,
        "favorite_language": favorite_language
    }


# A list of dictionaries (i.e. customers at location one.
customers_1 = [person("Alex", 23, "Java"),
               person("John", 30, "Python"),
               person("Charles", 65, "C")]

customers_2 = [person("Alexa", 19, "Rust"),
               person("Paris", 20, "JavaScript"),
               person("Phillip", 75, "Assembler")]

# Let's create another dictionary factory:


def location(city: str, customers: dict) -> dict:
    return {
        "city": city,
        "customers": customers
    }


# Now let's create a list of two locations:
locations = [
    location("Berlin", customers_1),
    location("London", customers_2)
]

# Yeah a list of dictionaries in another list of dictionaries!
print(locations)

# How do we access, for example, all the favorite languages?

favorite_languages = []

# Nested structure, start from the outermost layer and work your
# way through.
for location in locations:
    for customer in location.get("customers"):
        favorite_languages.append(customer.
                                  get("favorite_language"))

print(favorite_languages)

# Unpacking * and **
# Let's first look at functions:

# In the context of functions *args and **kwargs simply
# mean arbitrary many positional and keyword arguments,
# respectively.


def accept_everything(*args, **kwargs):
    return None


# We won't get any errors:
accept_everything(3, 34, "sdf", True)
accept_everything(name="Simon", age=33)

# If we want to pass kwargs more conveniently, we can do that.
# Dictionaries and unpacking:

example_dictionary = {
    "name": "Simon",
    "age": 33
}

accept_everything(**example_dictionary)

# Passing in a bunch of positional arguments?
# No problem!

accept_everything(*favorite_languages)
accept_everything(*locations)

# Accepting anything seems weird, but it can be super useful.
# For example, when creating decorators (next sessions)?

# Unpacking with * can also be extremely valuable outside of
# with functions:

# Let's say we have a list and want to assign it's content to
# variables:


# Python is so kind to automatically unpack our list and assign
# the values to a, b and c!
my_list = [1, 2, 3]
a, b, c = my_list
print(f"a: {a}, b: {b}, c: {c}")

# and works with tuples as well:
my_tuple = (4, 5, 6)
a, b, c = my_tuple
print(f"a: {a}, b: {b}, c: {c}")

# Which is very handy as functions returning more than one value
# return them as a tuple. For example:


def prev_and_next(nmb: int) -> tuple:
    return nmb - 1, nmb + 1


start = 0
prev, next = prev_and_next(start)
print(f"start: {start}, prev: {prev}, next: {next}")


# Extra: swapping values. To swap the value of two variables
# you can do the following:

a = "Hello"
b = "World"
print(a, b)

# Approach with a temporary variable:
tmp = b
b = a
a = tmp
print(a, b)

# It works, but Python let's us do it in one line.

c = "Change"
d = "Directory"
print(c, d)

c, d = d, c
print(c, d)

# Extra extra:
# List comprehensions
# Create lists easily and concise, e.g.:
new_list = ["Hello" * number for number in range(4)]
print(new_list)

# Extra extra extra:
# Zipping, for example, to create new lists:
# Combine two lists:

zipped = zip(lst_1, lst_2)

zipped_list = []
for zip_item in zipped:
    zipped_list.append(
        zip_item[0] * zip_item[1])

print(zipped_list)

# Looping is fine, but again Python let's us do it in one line:
zipped_list = [item_1 * item_2 for (item_1, item_2) in zip(lst_1, lst_2)]
print(zipped_list)
