
def register (students):
    id_st = input("Enter id: ")
    name = input("Enter the student's name: ")
    state = input("Enter student status (active, inactive): ")
    age = int(input("Enter the student's age:" ))
    course = input("Enter the course the student is in:" )
    student= {
        "id" : id_st,
        "name" : name,
        "state" : state,
        "age " : age,
        "course": course
    }
    students.append(student)
