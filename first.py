#x=1
#while x < 10:
#	print "x is" + str(x)
#	x = x+0.000001

#lst = [1, 2, 3, 4, 5]
#for element in lst:
#	print "The element is " + str(element)

#mp = {1 : "number one", 2 : "number two"}
#for element in mp:
#	print str(element) + "-->" + str(mp.get(element))

mp ={1 : "number one", 2 : "number 2", 3 : "number three"}

def find(key):
	return mp.get(key)


while True:
	op = raw_input("Do you want to enter a number?: (Yes or No)\n")
	op = op.lower()
	if op == "no":
		print "Goodbye"
		exit()
	elif op == "yes":
		number = raw_input("Enter some number: ")
		name = find(int(number))
		if name is not None:
			print "You entered " + str(number) + " and its name " + name
		else:
			print "I don't know the name for " + str(number)
	else:
		print "ERROR!?"