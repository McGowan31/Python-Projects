def death(monster):
	print("You were killed by a",monster)
	print("Thanks for playing!")
	print("GAME OVER!")

print("You have come to a cross road will you go right of left")
print("1 for left")
print("2 for right")
choice = input("What is your choice =-> ")

if choice =="1":
	print(" ")
	print("You confront a bear what will you do")
	print("1 to attack the bear")
	print("2 run a way from the bear")
	choice2 = input("What is your choice =-> ")
	if choice2 == "1":
		print(" ")
		print("You were able to kill the bear")
		print("You stumble across a house")
		print("You dont see anyone inside")
		print("1 Go back")
		print("2 Go inside")
		choice3 = input("What is your choice =-> ")
		if choice3 == "1":
			print(" ")
			print("You are ambused by a pack if wolfs")
			death("pack of wolves")
		if choice3 == "2":
			print(" ")
			print("You open the door and you see a staircase")
			print("one way leads up the other up and the other leads down")
			print("1 to go down")
			print("2 to go up")
			choice4 = input("What is your choice =-> ")
			if choice4 == "1":
				print("You go down stairs you are in a dark basement.")
				print("You step on a button and the whole basements colapses")
				death("ceiling")
			if choice4 == "2":
				print(" ")
				print("You go upstairs and you see a treasure chest")
				print("You open the chest and you find a endless supply of gold.")
				print("Congratulations you found the treasure")
	
	if choice2 == "2":
		print(" ")
		print("The bear pounces on you and starts to attack you")
		print("You stand no chance")
		death("bear") 
		



if choice == "2":
	print("Lol you found the short ending you found the treasure!")