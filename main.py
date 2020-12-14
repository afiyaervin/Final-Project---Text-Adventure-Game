print("Cinderella's Adventure")
print("Welcome to  Cinderella's Adventure!")
print("Type out 'help' if you ever need to access the help menu") 
user = input("There is a ball tonight. Do you want to go?")
if user == "yes":
  print("You need to get glass slippers, a beautiful dress, and a carriage in time for the Ball tonight! In your inventory you have bread and a wand.")
else:
  print("GAME OVER")
print("The animals have the slippers. You need to find the leader to get the glass slippers.")
print(" You go to the forest to find the  leader, and he tells you that they are hungry.")
food_for_animals = input("Would you like to give them any food? (HINT: Check your inventory!)")
if food_for_animals == "yes":
  print("You gave the Animal Leader bread, so he would like to give you the glass slippers!") 
  print("~slippers added to inventory!~")
else: 
  print("You did not get shoes in time for the ball.")

print("Now you have to find the dress")
dress = input("Should you ask your stepmother? Your stepmother may be able to give you one for free!")
if dress == "yes":
  print("You asked your stepmother for help, but she does not want you to go to the ball.")
  print("You have to go to the market")
else: 
  print("You have to go to the Market to find a dress for the Ball tonight!")
print("Now you are on the way to the Market.")
pumpkin = input("There is a pumpkin on the path. Would you like to pick it up?")

if pumpkin == "yes":
  print("~Pumpkin is added to inventory~")
else: 
  print("You were unable to get to the ball in time. Game Over. ")
print("You arrived at the Market. There are three different outfits for you to pick from.")
print("Outfit One is a short casual dress.")
print("Outfit Two is jeans and a t shirt")
print("Ouftit three is a ballgown")
outfit_choice = input("Which outfit would you like to go to the ball in? Type one, two, or three: ")

if outfit_choice == "one":
  print("You do not have clothes for the ball. You must pick another outfit")
  print("Hint: It's not outfit one!")
  print("Outfit One is a short casual dress.")
  print("Outfit Two is jeans and a t shirt")
  print("Ouftit three is a ballgown")
  outfit_choice2 = input("Which outfit would you like to go to the ball in? Type one, two, or three: ")
  if outfit_choice2 == "two":
    print("You do not have clothes for the ball. You must pick another outfit")
    print("Hint: It's not outfit one or two!")
    print("Outfit One is a short casual dress.")
    print("Outfit Two is jeans and a t shirt")
    print("Ouftit three is a ballgown")
    outfit_choice3 = input("Which outfit would you like to go to the ball in? Type one, two, or three: ")
    if outfit_choice3 == "three":
      print("Congratulations! You have a beautiful dress for the ball tonight!")
elif outfit_choice == "two":
  print("You do not have clothes for the ball. You must pick another outfit")
  print("Hint: It's not outfit two!")
  print("Outfit One is a short casual dress.")
  print("Outfit Two is jeans and a t shirt")
  print("Ouftit three is a ballgown")
  outfit_choice4 = input("Which outfit would you like to go to the ball in? Type one, two, or three: ")
  if outfit_choice4 == "one":
    print("You do not have clothes for the ball. You must pick another outfit")
    print("Hint: It's not outfit one or two!")
    print("Outfit One is a short casual dress.")
    print("Outfit Two is jeans and a t shirt")
    print("Ouftit three is a ballgown")
    outfit_choice5 = input("Which outfit would you like to go to the ball in? Type one, two, or three: ")
    if outfit_choice5 == "three":
      print("Congratulations! You have a beautiful dress for the ball tonight!")
else: 
  print("Congratulations! You have a beautiful dress for the ball tonight!")
print("Alert! Time is running out! You need to get to the Ball NOW!") 
wand = input("would you like to select the wand?") 
if wand == "yes":
  magic_choice = input("What would you like to use the wand on? The pumpkin, the dress, or the shoes?")
  if magic_choice == pumpkin:
    print("You turned the pumpkin into a carraige. Have fun at the ball!")
  elif magic_choice == dress:
    print("You turned the dress into a more beautiful gown. What would you like to use the wand on next?")
    after_dress = input("What would you like to use the wand on next? Shoes or the pumpkin?")
    if after_dress == shoes:
      print("You made the shoes prettier. What would you like to use the wand on next?")
    if magic_choice == Shoes:
      print("You made the shoes prettier. What would you like to use the wand on next?")
else:
  print("You did not make it to the Ball in time. Game over.") 

print("Have fun at the ball!")
print("Help Menu: Press 'I' for inventory check, press 'b' for go back")
#Afiya -if statement, print statements
#Dara - If statement, print statements
#Damani - help menu, if statement
# def help():
  #print("[1] Option 1")
  #print("[2] Option 2")
  #print("[0] Exit the program.")
  

#help()
#option =


# Questions
#What's in the help menu? Any thing that cinderella is going to need. 
#How many options do we need for the help menu? As many as need, until we figure out what our help menu is.
#How to define function with loops? similar as a for loop function, but def "variable"()
#What are nested if statements? If under an if 
#Any shortcuts? For now no, untill we have gotten more work done.

