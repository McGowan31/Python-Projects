enter = input("Enter a strings: ")

acount = 0
ecount = 0
icount = 0
ocount = 0
ucount = 0
ycount = 0

for letter in enter:
	if letter.lower() == "a":
		acount = acount + 1
	elif letter.lower() == "e":
		ecount = ecount + 1
	elif letter.lower() == "i":
		icount = icount + 1
	elif letter.lower() == "o":
		ocount = ocount + 1
	elif letter.lower() == "u":
		ucount = ucount + 1
	elif letter.lower() == "y":
		ycount = ycount + 1
	
total_vowels = (acount + ecount + icount + ocount + ucount + ycount)

print("The number of A is ",acount)
print("The number of E is ",ecount)
print("The number of I is ",icount)
print("The number of O is ",ocount)
print("The number of U is ",ucount)
print("The number of Y is ",ycount)
print("The total number on vowels is",total_vowels)