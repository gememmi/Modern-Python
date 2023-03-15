

marks = {
    "English": 80,
    "Maths": 82,
    "Python" : 98,
    "Physics" : 40,
}

print(f"List of Marks for Louis {marks}")

# here were are just printing the keys of the dictionary 
for subject in marks.keys():
    print(subject)

# you can do the same thing for printing just the values of the dictionary
for score in marks.values():
    print(score)

# if you want to print the keys and values together you can use .items on the dictionary
for subject, score in marks.items():
    print(f"{subject}: {score}/100")

# now we can combine this for in loop with a conditional to print strings conditionally with the key value pairs
for subject, score in marks.items():
    if score <= 50:
        print(f"{subject}: FAILED!!!")
    else:
        print(f"{subject}: PASSED")

marks["English"] = 70
print(marks)
print(f"Louis has scored {marks['English']} in English")

marks["Geography"] = 70

for subject, score in marks.items():
    if score <= 50:
        print(f"{subject}: FAILED!!!")
    else:
        print(f"{subject}: PASSED")
# when an element does not exist, using bracket notation will throw and err
# java_score = marks["Java"]
# print(java_score)
# using dictionary.get(key) will return none if it does not exist, and will not interupt the code running
java_score = marks.get("Java")
print(java_score)

# checking if the key/value pair exist using if/else conditional
if java_score is None:
    print("Louis did not study Java")
else:
    print(f"Louis scored {java_score} in Java")