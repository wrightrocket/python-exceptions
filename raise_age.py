''' Example of raising an exception where it might make sense 

If you wanted to calculate 100.0 divided by a person's age, then a value larger than zero
would make sense. This program will raise a ZeroDivisionError if the age input is less than
or equal to zero.
'''

# Receive input from the user as a string for their age.

age = input("\nHow many years old are you?  ")

# Convert the age string variable into an integer.

age = int(age)

# Check for truth if the age entered is less than or equal to 0 (zero).

if age <= 0:

    # If it is true that the age is less than or equal to 0(zero), 
    # raise the ZeroDivisionError which will cause the program to exit

    raise ZeroDivisionError

# If it false that the age <= 0, then print the age divided by 100.0.

else:

    # Calculate 100 age ratio

    age_ratio = 100 / age

    # Print the age_ratio value with 3 digits or spaces on the left and two 
    # on the right of the decimal point.

    print ('\nYour "100 age ratio" is: {: 3.2f}'.format(age_ratio))

