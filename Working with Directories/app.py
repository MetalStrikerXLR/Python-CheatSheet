from pathlib import Path

# Check existence of Directory
# p = Path("ecommerce")
# print(p.exists())

# Create new Directory
# e = Path("emails")
# e.mkdir()

# Delete Directory
# e.rmdir()

# Change Path and search files there
p = Path()
for file in p.glob('*'): # *: all files and directories, *.*: all files but no directories
    print(file)


