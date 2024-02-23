# lab5.1.4_Student_Name_&_Course
# Write a program that stores a student name and a list of her courses and
# grades in a dict, the program should then print out her data 

student = {
    "name":"Mary",
    "modules": [
        {
            "courseName":"Programming",
            "grade": 45
        },
        {
            "courseName":"History",
            "grade":99
        }
    ]
}
print (f'Student: {student["name"]}')
for module in student["modules"]:
    print (f'\t{module["courseName"]} \t:{module["grade"]}')