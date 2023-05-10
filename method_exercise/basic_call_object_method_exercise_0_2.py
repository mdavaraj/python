# Objective  
# To understand basic object class method and how different from static method
# Basic Object storages
# Object method parameter passing

# What to do
# ==========
# Follow TODO below

#from cls.method_exercise.basic_object_method_class import BasicObjectClass
from basic_object_method_class import BasicObjectClass
from basic_static_method_class import StaticMethodClass


m = BasicObjectClass(); # --> Obj variable
m.anIntTest = 1000;
print ('basic_call_object_method_exercise_0.1 sparePart-->', m.sparePart())

# TODO call the sparePartStaticWithParameter method with passing parameter
g = StaticMethodClass()

# Your output need to be as below
# basic_call_static_method_exercise_0 with parameter--> 1901
# anIntTest value must set as 1000
print ('basic_call_object_method_exercise_0.1 sparePartWithParameter-->', g.sparePartStaticWithParameter(1900))
