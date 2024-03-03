# lab6.1.2_students_expantion.py
# 
# create a program that allows a user to create new students and to view students.
# Write a function that prints out a menu of commands we can perform, ie add, 
# view and quit. The function should return what the user chose.
# Test the function.

# Not finished stopped at Q4 

def show_menu():
    print ("What would you like to do?\n\t(a) Add new student\n\t(v) View students\n\t(q) Quit")
    user_menu_choice = input ("Type one letter (a/v/q):")
    print (f"You chose {user_menu_choice}")
    return user_menu_choice

#def repeat_menu ():
 #   if user_menu_choice != "q"

def doAdd():
    print ("You are in the adding section.")
    student["name"] = input("Enter student's name: ")
    

    
def doView():
    print ("You are in viewing.")

student = {}
    
user_menu_choice = show_menu ()

while user_menu_choice != "q":
    if user_menu_choice == "a":
        doAdd()
        
    elif user_menu_choice == "v": 
        doView()

    elif user_menu_choice != "q":
        print("\nPlease select either a,v or q")

    user_menu_choice = show_menu ()

print (student)

print("You have selected q. This program will now end")




'''
student = {}
student["name"] = input("Enter student's name: ")

modules = []
while True:
    course_name = input("Enter module course name: ")
    if course_name == "":
        break

    module_grade = input("Enter the grade for the module: ")

    modules.append({"course_name":course_name, "grade":module_grade})

student["modules"] = modules

print(student)'''