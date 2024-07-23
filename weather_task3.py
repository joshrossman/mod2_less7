#Task 3: User Experience Implement an else block that prints 
# the converted temperature in a user-friendly format. 
# Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

def far_to_cels(far):
    try:
        cels=(far-32)*5/9
    except TypeError:
        print("Please only use number digits")
    else:
        print(f"{far} degrees Fahrenheit is {cels} degrees Celsius.")
    

    
input("What is the weather today?")