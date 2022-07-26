Admins = ["Hamza", "Banga", "Ahmed", "Osama", "Moazer", "Buga" ]
# print(Admins.index("hamza"))
name = input("Enter Youre Name Plaes.").strip().capitalize()
# Admins = Admins.strip().capitalize()
if name in Admins :
    print(f"Hello {name} Welcome ")
    option = input("Delete Or Update ? ").strip().capitalize()

    if option == "Delete" or option == "D" :
        Admins.remove(name)
        print(Admins)
        print("Done ")
        print("See You Soon ")
    elif  option == "Update" or option == "U" : 
        newName = input("Enter New Name ").strip().capitalize()
        Admins[Admins.index(name)] = newName
        print("Done ")
        print(Admins)
    else :
        print(f" Your Input {option} Not includ in Option Pleas Try Agine")

else : 
    print("Youre Not Admin Add You ?")
    input("Add You ? Yes OR NO ").strip().capitalize()
    Admins.append(name)
    print("Done ")
    print(Admins)
    