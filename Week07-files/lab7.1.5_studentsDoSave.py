# lab6.1.2_students_expantion.py
# 
# create a program that allows a user to create new students, add their modules and grades and to view students.
# Author: Angela Davis

import json
students=[]
FILENAME='students.json'

def writeDict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)

def readDict():
    with open(FILENAME) as f:
        return json.load(f)

def show_menu():
    print ("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(l) load students")
    print("\t(s) Save students")
    print("\t(q) Quit")    
    user_menu_choice = input ("Type one letter (a/v/l/s/q):")
    return user_menu_choice

def doAdd():
    print ("You are in the adding section.")
    current_student = {}
    current_student["name"] = input("Enter student's name: ")
    current_student["modules"] = readModules () 
    students.append(current_student)

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

def displayModules(modules):
    print ("\tName  \tGrade")
    for module in modules:
        print(f"\t{module['name']}  \t{module['grade']}")

def doView():
    print ("\nYou selected view.\n")
    for currrent_student in students:
        print (currrent_student["name"])
        displayModules (currrent_student["modules"])

def doSave():
    print("in save") 
    writeDict(students)
    print("students saved")

def doLoad():
    global students
    students = readDict()
    print ("students loaded")

#main program
user_menu_choice = show_menu ()
while user_menu_choice != "q":
    if user_menu_choice == "a":
        doAdd()
        
    elif user_menu_choice == "v": 
        doView()

    elif user_menu_choice == 'l':
        doLoad()

    elif user_menu_choice != "s":
        doSave()

    elif user_menu_choice != "q":
        print("\nPlease select either a,v or q")
    user_menu_choice = show_menu ()

print("This program will now end")