# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Gene Choi,05/20/2026, Created Script
# ------------------------------------------------------------------------------------------ #

#import JSON module
import json
from json import JSONDecodeError


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json" 

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data 
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str = '' # Hold the choice made by the user.


# When the program starts, read the JSON file data into the students list(table)
# Extract the data from the file
# If the file does not exist, application will throw an error and perform actions given specific conditions

try: 
    file = open(FILE_NAME, "r")
    students=json.load(file)
except FileNotFoundError as e:
        print("File Not Found")
        print("---Technical Information---")
        print(e, e.__doc__, type(e), sep='\n')
        file = open(FILE_NAME, 'w')
except JSONDecodeError as e:
        print("---Technical Information---")
        print(e, e.__doc__, type(e), sep='\n')
        print("Data in file is not valid.  Resetting file with current student table data")
        file = open(FILE_NAME, 'w')
        json.dump(students, file)
except Exception as e:
        print("Unhandled exception")
        print("---Technical Information---")
        print(e, e.__doc__, type(e), sep='\n')
finally:
     if not file.closed:
          file.close()

# Check if a file object exists and is still open
if file is not None and file.closed == False:
    file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    # Script will check that Student First and Last Names are alphabetic
    # Error will be thrown if numeric characters detected in name input
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name must be alphabetic")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name must be alphabetic")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)
            print("---Technical Information---")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-"*50)
        continue

    # Save the data to a JSON file
    # Error handling implemented to ensure that JSON data is well-formed
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=2)
            file.close()
        except TypeError as e:
            print("JSON data was malformed")
            print("---Technical Information---")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("---Technical Information---")
            print(e, e.__doc__, type(e), sep='\n')
        # Check if a file object exists and is still open
        finally:
            if file is not None and file.closed == False:
                file.close()

        print("The following data was saved to file!")
        for student in students:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
