import csv

students=[]

with open("students.csv") as file:
    for line in file:
        #rstrip() and .split(",") is splitting the names
        name, house = line.rstrip().split(",")
        student={"name": name, "house":house}
        students.append(student)

""" This works as well
        ^^^
get_name is needed to make the list sorted
def get_name(student):         alphabet sort by names
    return student["name"]      ^^
                                ^^
def get_house(student):         "" sort by house
    return student["house"]
                                key=get_house
                                key=get_name
                                    ^^^     """
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
