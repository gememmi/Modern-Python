# Lists are mutable structures, we can change them
from typing import List
# create a new variable that will be a list of strings and specify that
friends: List[str] = ["Cece","Chiko","Roko", "Niko"]
print(f"Friends: {friends}")
# create a simple for-in loop to greet all his friends

# for friend in friends:
#     print(f"Zola {friend}")

# find the length of the list

print(f"Number of Friends: {len(friends)}")

# Louis wants to remove a friend from the list

unfriend = friends.pop()
# print(unfriend)
# print(friends)

# Louis wants to add a friend to the list

friends.append("Ziko")
print(friends)

# print(friends[3])

friends.remove(friends[3])
print(friends)

friends.insert(1,"Riko")
print(friends)


if "Roko" in friends:
    print("Zola Roko")
else: 
    print("Oh thats right he is not my friend")

friends.insert(0, "Niko")
print(friends)

# will sort into alphabetical order
friends.sort()
print(f"Friends List: {friends}")

# now that we have sorted them alphabetically, we can call .reverse to get them in reverse order
friends.reverse()
print(f"Friends List: {friends}")

# this will get rid of and return the popped off element
unfriend = friends.pop(2)
print(unfriend)
print(friends)






