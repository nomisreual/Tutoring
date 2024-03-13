import os
from pathlib import Path

# Set root paths:
ROOT = Path.cwd()
DATA_ROOT = ROOT.joinpath("./data")

# Creating folders:
DATA_ROOT.mkdir()

# Create a new file:
file = DATA_ROOT.joinpath("./file.txt")

with open(file, "w") as f:
    f.write("")  # empty file

# Deleting a file:
try:
    file.unlink()
except FileNotFoundError:
    print(f"There is no file, {file.name}.")


# By default, attempting to delete a file that does
# not exist raises an exception:
null = Path("./dev/null")
try:
    null.unlink()
except FileNotFoundError:
    print(f"There is no file, {null.name}.")

# Can also be supressed within the call:
null.unlink(missing_ok=True)

# Removing directories:

# If the directory does not exist:
# a FileNotFoundError is raised.
dir = Path("./tmp")
try:
    dir.rmdir()
except FileNotFoundError:
    print(f"The directory {dir.name} does not exist")

# If the directory is not empty,
# an OSError is raised:

# Recreate the file in ./data:
with open(file, "w") as f:
    f.write("")
try:
    DATA_ROOT.rmdir()
except OSError:
    print(f"The directory {DATA_ROOT.name} is not empty.")

# Get the parent directory:
print(file.parent)  # file lives in data directory

# Replacing files:

# Create new path:
file_two = DATA_ROOT.joinpath("./file.md")
file.replace(file_two)

# List files and directories within a given path:
subdir = DATA_ROOT.joinpath("./subdir")
subdir.mkdir()

# all files and directories:
for item in DATA_ROOT.glob("*"):
    print(item)

# specific files types, like markdown files:
for item in DATA_ROOT.glob("*.md"):
    print(item)

# Resolving paths:

file_three = Path("./data/file.md")
print(file_three)  # just relative path
print(file_three.is_absolute())
print(file_three.resolve())  # absolute path
print(file_three.resolve().is_absolute())

# Alternative join path notation:
print(DATA_ROOT.joinpath("home", "data"))
# and
print(DATA_ROOT / "home" / "data")

# Check existence of a path:
print(DATA_ROOT.exists())  # True
print(Path("./tmp").exists())  # False


# You can use this instead of a try/except block.
# However, it is more pythonic to ask for forgiveness
# (try/except) rather than asking for permission
# (if/else).

# There are more methods availabe such as is_dir().


# OS module:

# os.walk
for dirpath, dirnames, filenames in os.walk(DATA_ROOT):
    print("*" * 20)
    print("Directory:", dirpath)
    print("Subdirectories:", dirnames)
    print("Files:", filenames)

# Some useful os.path methods:
# os.path.getmtime(path)  # get timestamp of last modification
# os.path.getsize(path)  # file size
# os.path.joint(path1, path2, ...)  # join paths
# os.mkdir(path)  # make directory
# os.rename(path1, path2)  # rename path1 to path2
