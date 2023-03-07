"""
Louis wants to drive a car 🚙 and he hears that in planet
Zortan 🪐 there is no age limit for getting a license.

`AND` Table
------------
True and True => True
False and False => False
True and False => False
False and True => False

`OR` Table
----------
True or True => True
False or False => False
True or False => True
False or True => True
"""

age: int = 13
planet: str = "Zortan"

#And/ Or Statements

if age < 16 and planet == "Earth":
    #Evalution - True and True => True
    print("You are not allowed to drive")
    #Python stops here because it sees that both are true and it exits the if/else block
elif age > 16 and planet == "Earth":
    print("You can drive")
elif age < 16 or planet == "Zortan":
    print ("you can drive on this planet")