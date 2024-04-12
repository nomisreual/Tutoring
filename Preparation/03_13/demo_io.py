file_name = "hello.txt"


with open(file_name, "w") as file:
    file.write("Hello, world.\n")

with open(file_name, "a") as file:
    file.write("Hello, again.\n")
