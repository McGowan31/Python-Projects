enter = input("Enter a strings: ")
a = "a"
e = "e"
i = "i"
o = "o"
u = "u"
acount = 0
ecount = 0
icount = 0
ocount = 0
ucount = 0

#vowels = ("a","A","e","E","i","I","o","O","u","U")

for letter in enter:
	#print("--- The letter is", letter.lower())
	if letter.lower() in "a":
		acount = acount + 1
	elif letter.lower() in "e":
		ecount = ecount + 1
	elif letter.lower() in "i":
		icount = icount + 1
	elif letter.lower() in "o":
		ocount = ocount + 1
	elif letter.lower() in "u":
		ucount = ucount + 1
	

print("The number of A is ",acount)
print("The number of E is ",ecount)
print("The number of I is ",icount)
print("The number of O is ",ocount)
print("The number of U is ",ucount)