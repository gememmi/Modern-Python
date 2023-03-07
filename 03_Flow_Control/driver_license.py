age: int = 13

age = 13

#If and Else Statements

# age = 19 

# if age < 16:
#     print("You are not allowed to drive")
# else:
#     print("You are allowed to drive")
#note how we indented the return for the conditional statments

# My VSCode will not run this properly, but the guy onthe video can, idk


# ----------------------------------------------------
# Alternative Implementation - Without `Else` block
# ----------------------------------------------------

# if age < 16:
#     print("You are NOT eligible for a license.")

# print("You can apply for a license!")

#Chaining conditional statements

age = 100


if age < 16:
    print("You are not allowed to drive")
elif age >= 100:
    print('You are too old to drive')
else:
    print("You are allowed to drive")