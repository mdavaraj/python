from basic_method_exercise_0_3 import getTotalPrice


#print(getTotalPrice(10))


def userselection():
	choice1="Mcdonald"
	choice2="Nasi Lemak"
	choice3="Mee Kosong"

	print("1. Mcdonald - RM 10")
	print("2. Nasi Lemak  - RM 2")
	print("3. Mee Kosong  - RM 1")
	x = input("Enter your food choice here: Enter 1 2 or 3 ")
	return x



selected = userselection()

getTotalPrice(selected)

print ('Your selected food is ' + selected +  ' and the total price is RM' , getTotalPrice(selected))

#getTotalPrice(x)
	#
	# number =
	# food_1 = "Mcdonald"
	# food_price_1 = "RM 10"
	# food_2 = "Nasi Lemak"
	# food_price_2 = "RM 2"
	# food_3 = "Mee Kosong"
	# food_price_3 = "RM 1"


# print ("Food 1. Mcdonald RM 10")
# print ("Food 2. Nasi Lemak RM 2")
# print ("Food 3. Mee Kosong RM 1")
#
# x = input("Enter your food choice here: Enter 1 2 or 3 ")
#
#
# print ('Your selected food is ' + x + ' and the total price is RM' , getTotalPrice(x))

