from method_exercise.may15.basic_method_exercise_0_3 import BasicMethodExcercise

def userselection():
	print("1. Mcdonald - RM 10")
	print("2. Nasi Lemak  - RM 2")
	print("3. Mee Kosong  - RM 1")
	x = input("Enter your food choice here: Enter 1 2 or 3 ")
	return x

selected = userselection()

print ('Your selected food is ' + BasicMethodExcercise.userselection(selected) + ' and the total price is RM' , BasicMethodExcercise.getTotalPrice(selected))
