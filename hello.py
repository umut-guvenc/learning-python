#Ask user for their name
name =input("What is your name?")

#Remove whitespace from str
name = name.strip()

#Capitalize user's name
name = name.title()

#Greet the user
print(f"hello, {name}") 