# QUESTION 1. Nested decisions the adventure game


# TASK 1: Buggy code
#place= input("Choose a place: forest or cave?")
#action= input("climb a tree or cross a river")

#if place == "forest":
    #if action == "climb a tree":
        #print("You found a bird's nest!")
    #elif action == "cross a river":
       # print("You found a boat!")
#elif place == "cave":
    #print("You find a hidden treasure!")



    

#Task 2: Setting the Scene
place = input("Choose a place: forest or cave? ")
if place == ("forest"):
     action= input("Choose a action: climb a tree or cross a river? ")   
else:
    action = input("Choose a action: light a torch or proceed in the dark? ")
   

if place == "forest":
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    if action == "light a torch":
        print("fight all the creepy crawlers")
    elif action == "proceed in the dark":
        print("Trip and fall into an abyss")
    else:
        print("You find a hidden treasure")
else:
    pass



#==============2. Quick Decisions: The Event Planner 🎉====================

#Task 1
attendees = int(input("Enter number of attendees: "))
venue = (attendees)

if attendees > 100: 
    print("large hall") 
elif attendees >= 40-90: 
    print("bar") 
elif attendees >= 11-39: 
    print("confrence room") 
else: 
    attendees <= 10
    print("living room")



#Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

#Task 2
caterers = input("Do you want vegerterian food:" )

if caterers == "Yes":
    print("Veggie Delight Caterers")
else:
    caterers== "No"
    print("Gourmet Meals Caterers")
