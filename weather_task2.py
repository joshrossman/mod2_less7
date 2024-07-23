#Task 2: Temperature Conversion Write a function that converts 
# the Fahrenheit temperature to Celsius. Remember that the formula 
# is (Fahrenheit - 32) * 5/9.Use a try block to catch any potential errors 
# during the conversion process. 
# What happens if they type out "thirty" instead of doing 30?


def far_to_cels(far):
    try:
        cels=(far-32)*5/9
    except TypeError:
        print("Please only use number digits")

    return cels
input("What is the weather today?")