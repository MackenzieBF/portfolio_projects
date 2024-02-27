# Python + SQL Personal Project
# Creating a reminder system to reach out consistently to friends

# Step 1: Creates a CSV file for the User with headings
# Step 2: Reads the CSV file for the User 
# Step 3: Stores the contact information in a DataFrame
# Step 4: Stores the recurring contact information in a separate DataFrame
# Step 5: Selects those who should be contacted this week
# Step 6: 
# Step 7: 

# Import statements for the entire program
import csv
import os.path

# Step 1: Create a CSV file for the User with headings
# Only does this one time per user unless it cannot find the file later
# If cannot find the file, ask for new path or give option to create new file

try:
    #open file and store in file
except FileNotFoundError:
    print('File does not yet exist or File Path is lost\n')
    print('Press 1 to generate a new file (first time set up) or Press 2 to input new File Path\n')
    file_selection = input("Enter 1 or 2: ")
    if file_selection = 1:
        new_file = open("Information.xlsx", "x")
    else if file_selection = 2:
        #give the user the option to select a new file path from the file explorer
    else:
        #return error and go back to 1 or 2

#dataframe of all of the headings for the xlsx file
#add the headings to the xlsx file one time

#have the user fill in their information
#store in a separate dataframe that doesn't get written over unless they go into settings

#prompt the user to go fill in the file 
#close the program or can create an internal structure eventually to hold the data
#if it gets big enough, would have to get user storage and store it online