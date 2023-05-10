from basic_method_exercise_0_3 import getTotalPrice


#print(getTotalPrice(10))
food_1 = "Mcdonald"
food_price_1 = "RM 10"
food_2 = "Nasi Lemak"
food_price_2 = "RM 2"
food_3 = "Mee Kosong"
food_price_3 = "RM 1"


print ("Food 1. Mcdonald RM 10")
print ("Food 2. Nasi Lemak RM 2")
print ("Food 3. Mee Kosong RM 1")

x = input("Enter your food choice here: Enter 1 2 or 3 ")

if (x == "1"):
	g= getTotalPrice(10)
	print ('Your selected food is ' + food_1 + ' and the total price is ' + str(getTotalPrice(10)))


elif (x == "2"):
	g= getTotalPrice(2)
	print ('Your selected food is ' + food_2 + ' and the total price is ' + str(g))
elif (x == "3"):
	g= getTotalPrice(1)
	print ('Your selected food is ' + food_3 + ' and the total price is ' + str(g))
else:
	print("Invalid choice selected!")