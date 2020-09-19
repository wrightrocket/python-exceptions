'''
Example of how advanced exception handling may be done.
'''
__author__ = 'Keith Wright'

# Import the traceback module to be able show details about exceptions
import traceback
import sys

# Assign numerator by default to 1000
numerator = 1000

# Assing a variable to not exit while loop until successful
trying = True

while trying:
    # Receive user_input for a number to use as denominator as a 'str'
    user_input = input('Number to divide 1000 by: ')

    # Convert user_input to a floating point value for the denominator
    try:
        # Put statements that may cause exceptions in the try clause
        # Will cause ValueError with non-numeric values as user_input
        denominator = float(user_input)
        
        # Will cause ZeroDivisionError with zero (0) value as user_input
        result = numerator / denominator

    except Exception:
        # print the traceback
        print(traceback.format_exc())

        # Assign info from detailed system exception information
        exception, description, tracebk = sys.exc_info()
        print("What you input caused this exception: {0}".format(exception))
        print("The description of this exception: '{0}'".format(description))


    else:
        # Show the successful result 
        # Display the calculation and the result
        print ('{:d} divided by {: .3f} equals {:+4.5f}'.format(numerator, denominator, result))
        trying = False
    finally:
        # Display at message at the end of the try block depending on if still trying
        if trying:
            print("\nTry again, there was an error with your last input\n")
        else:
            print("\nThank you for providing valid input")
            print("Goodbye!")
