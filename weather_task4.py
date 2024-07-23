#Task 4: Finally Add a finally block that thanks the 
# user for using the weather forecast application, ensuring that this message
#  is displayed regardless of whether an exception was caught or not.

def far_to_cels(far):
    try:
        cels=(far-32)*5/9
    except TypeError:
        print("Please only use number digits")
    else:
        print(f"{far} degrees Fahrenheit is {cels} degrees Celsius.")
    finally:
        print("Thank you for using the weather program! Have a great day!")
  

    
far_to_cels(input("What is the weather today?"))