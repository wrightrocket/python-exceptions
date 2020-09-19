''' Demonstrates how to display a warning to a user.

At times when the user may have entered data that exceeds the expected length,
then a warning could be displayed to the user
'''

# Make the warnings modules objects available to this program

import warnings

# Ask the user to enter a username of 10 characters or less and store the entry.
# Use \n in strings throughout to create a "newline" or blank line on the screen.

username = input("\nPlease provide a username of less than 10 characters: ")

# Check to see if the length of the username entry is less than 11 characters

if len(username) < 11:

    # If the username is 10 characters or less print a success message
    # Note: If you use single quotes(') then double quotes(") don't
    # have to be escaped by backslash(\) characters.

    print ('\nCongratulations, your new username is "{0}"!'.format(username))

# If the username is more than 10 characters, display a warning

else:

    # Create a formatted message string to be display
    # Note: Since double quotes(") were used for the string they
    # have to be escaped by backslash(\) characters.
    
    message = "\nUnfortunately, the username \"{0}\" is too long, try again.".format(username)

    # Use the warnings module warn function to display the message string to STDERR
    
    warnings.warn(message)

    # Print the message string variable to display the warning to STDOUT

    print(message) 

