# lab6.1.2_students_expantion.py
# 
# create a program that allows a user to create new students, add their modules and grades and to view students.
# Author: Angela Davis


def show_menu():
    print ("What would you like to do?\n\t(a) Add new student\n\t(v) View students\n\t(q) Quit")
    user_menu_choice = input ("Type one letter (a/v/q):")
    print (f"You chose {user_menu_choice}")
    return user_menu_choice

def readModules():
    modules = []
    module_name = input("\tEnter the first module name (blank to quit):").strip()

    while module_name != "":
        module = {}
        module["name"] = module_name
        module["grade"] = int(input("\tEnter grade:"))
        modules.append(module)
        module_name = input("\tEnter next module name (blank to quit): ").strip()
    return modules

def doAdd(students):
    print ("You are in the adding section.")
    current_student = {}
    current_student["name"] = input("Enter student's name: ")
    current_student["modules"] = readModules () 
    students.append(current_student)

def displayModules(modules):
    print ("\tName  \tGrade")
    for module in modules:
        print(f"\t{module['name']}  \t{module['grade']}")

def doView(students):
    print ("\nYou selected view.\n")
    for currrent_student in students:
        print (currrent_student["name"])
        displayModules (currrent_student["modules"])

students = []

user_menu_choice = show_menu ()

while user_menu_choice != "q":
    if user_menu_choice == "a":
        doAdd(students)
        
    elif user_menu_choice == "v": 
        doView(students)

    elif user_menu_choice != "q":
        print("\nPlease select either a,v or q")

    user_menu_choice = show_menu ()

print("This program will now end")
