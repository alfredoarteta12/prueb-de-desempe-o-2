def update_st (students):
    name = input("estudiante a actualizar")
  

    for s in students:
        print("enter new date")
        s["name"] = input("nuevo nonbre")
        s["age"] = input("nueva edad")
        s["course"] = input("nuevo curso")
        s["state"] = input("nuevo estado")
    
