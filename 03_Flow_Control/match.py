#MATCH FLOW CONDITIONAL OPERATOR

fav_color = input("Enter your favorite color:  ")
print(fav_color)

match fav_color:
    case "black":
        print("Louis has a BLACK t-shirt")
    case "red":
        print("Louis has a RED car")
    