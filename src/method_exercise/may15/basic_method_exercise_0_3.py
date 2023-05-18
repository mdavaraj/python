from method_exercise.may15.static_variable_food import StaticVariableFood
class BasicMethodExcercise:

    @staticmethod 
    def userselection(x):
        if x == "1":
            return StaticVariableFood.MCDONALD_NAME
        elif x == "2":
            return StaticVariableFood.NASI_LEMAK_NAME
        elif x == "3":
            return StaticVariableFood.MEE_KOSONG_NAME
        else:
            return StaticVariableFood.INVALID_CHOICE

    @staticmethod 
    def getTotalPrice(x):

        if x == "1":
            return StaticVariableFood.MCDONALD_PRICE
        elif x == "2":
            return StaticVariableFood.NASI_LEMAK_PRICE
        elif x == "3":
            return StaticVariableFood.MEE_KOSONG_PRICE
        else:
            return StaticVariableFood.INVALID_CHOICE


