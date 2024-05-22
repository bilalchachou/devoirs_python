import random



#--------------1--------------------------

# My Python Code Forever

#--------------2--------------------------

"""
My Python Code every day
"""

#--------------3--------------------------

variable_int = 42
variable_float = 42.0
variable_str = "42"
variable_bool = True
variable_list = [42]
variable_dict = {"key": 42}
variable_set = {42}
variable_tuple = (42,)

#--------------4--------------------------

my42count = "quarante-deux"
my42count_length = len(my42count)

#--------------5--------------------------

def variable_existe(variable_name):
    try:
        return eval(variable_name)
    except NameError:
        return 42

#--------------6--------------------------

myArray42 = list("quarante-deux")

#--------------7-------------------------

myArray42Len = len(myArray42)

#--------------8-------------------------

mot = ''.join(myArray42)

resultat = mot + " La grande réponse sur la vie, l’univers et le reste !"

#--------------9-------------------------

def check_42(num):
    return {
        True: "true",
        False: ""
    }.get(num == 42, "")

rand = check_42(random.randint(1, 42))

#--------------10-------------------------

my42Type_int = type(variable_int).__name__
my42Type_float = type(variable_float).__name__
my42Type_str = type(variable_str).__name__
my42Type_bool = type(variable_bool).__name__
my42Type_list = type(variable_list).__name__
my42Type_dict = type(variable_dict).__name__
my42Type_set = type(variable_set).__name__
my42Type_tuple = type(variable_tuple).__name__

#--------------11-------------------------

compute42 = 6 * 7
compute42_str = str(compute42)
#--------------12-------------------------

my_string = "42424242"
my_string_replaced = my_string.replace("42", "quarante-deux ")

#--------------13-------------------------

a = 24
b = 42

a, b = b, a