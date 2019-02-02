number_of_atbats = int(input("How many times have you gone up to bat this season: "))
number_of_hits = int(input("How many hits have you had this season: "))
batting_avg = number_of_hits / number_of_atbats

if number_of_hits > number_of_atbats:
	print("You cant have that many hits you have only been up to bat",number_of_atbats,"times!")
else:
	print(batting_avg)