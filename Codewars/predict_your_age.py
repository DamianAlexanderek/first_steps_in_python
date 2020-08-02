# My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!
# In honor of my grandfather's memory we will write a function using his formula!
# Take a list of ages when each of your great-grandparent died.
# Multiply each number by itself.
# Add them all together.
# Take the square root of the result.
# Divide by two.
# Example
# predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86


import math
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    list = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    list2 = []
    for i in list:
        list2.append( i *i)

    sum1 = sum(list2)
    sum2 = math.sqrt(sum1)

    wynik = sum2 / 2

    return int(wynik)