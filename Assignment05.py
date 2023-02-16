# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# zdevries, 2.15.2023,
# <YOUR NAME HERE>,<DATE>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFileName = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)


objFile = open(objFileName, "r") # open the file saved in the local directory
for row in objFile:  # Use a for loop to process each line in the .txt file
    strData = row.split(",")  # Using a comma as a delimiter, split the data into columns in the list row
    dicRow = {'Task':strData[0].strip(),'Priority':strData[1].strip()}  # Move the list into a dictionary with provided Keys
    lstTable.append(dicRow)  # Add the dictionary to the 'table' stored in memory
objFile.close()  # close the file


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:  # For each row in the list table print the data identified by the keys
            print(row['Task'] + ' | ' + row['Priority'])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input('Enter a Task: ').strip()  # Collect user input
        strPriority = input('What is the priority? [high/low]').strip()  # Collect user input
        dicRow = {'Task': strTask, 'Priority': strPriority}  # Add user input into a dictionary
        lstTable.append(dicRow)  # Append dictionary to list table in memory
        print('Data added to table')
        #  print(len(lstTable))
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strRemoveTask = input('Enter a task to remove: ').strip()  # Collect user input
        blnItemWasRemoved = False  # Declare a boolean flag for use in identifying whether a subprocess ran succesfully below.

        for row in lstTable:
            Task, Priority = dict(row).values()
            if Task == strRemoveTask:
                lstTable.remove(row)
                blnItemWasRemoved = True  # Set flag to true for use below

        if blnItemWasRemoved == True:  # Let the user know if a Task was removed
            print('Item was removed')
        if blnItemWasRemoved == False:
            print('Item was not removed')  # Let the user know if a Task was not removed
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(str(objFileName), "w")  # open file
        for row in lstTable:
            objFile.write(row['Task'] + ' , ' + row['Priority'] + '\n')  # Write each row in the table to the file.
        objFile.close()

        print('The following data was saved in the file')
        for row in lstTable:  # For each row in the list table print the data identified by the keys
            print(row['Task'] + ' | ' + row['Priority'])
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
