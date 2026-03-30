from register import*
from consult import*
from buscar import*
from update import*
from delete import*
def menu():
    students = []
    continuar = True

    while continuar:
        print("Welcome to the Riwi student system")
        print("1. register student")
        print("2. Check student ")
        print("3. Search student")
        print("4. Update")
        print("5. Delete student")
        print("6. Exit system")
        option = input("Please enter an option (1, 6)")
                    
        if option == "1":
                print("entering to register")
                register(students)
       
        if option == "2":
               print("entering to check student ")
               consulting(students)
        if option == "3":
            name = input(" Nombre del estudiante a buscar: ")
            stu = buscar_estudiantes(students, name)
            if stu:
                print(" estudiante: ", {students[0]})
            else:
                print("estudiante no encontrado.")
        if option == "4":
             print ("entering to update")  
             update_st(students)
        if option == "5":
               print ("entering to delete")
               delete_est(students)



        elif option == "6":
            print("Exiting the program, Thank you for using the system")
            continuar = False
  

    