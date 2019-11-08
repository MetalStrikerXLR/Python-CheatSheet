# if name is less than 3 charactes lon name must be atleast 3 characters otherwise if it is more than 50  characters long name can be max of 50
#characters otherwise look good

name = "js"
if len(name) < 3:
    print("Name must be at least 3 character")
elif len(name) > 50:
    print("name must be a max 50 charac")
else:
    print("name looks good")
