import os

def add_name():
    name_list = []
    
    size = int(input("HOW MANY NAMES? "))
        
    for i in range(size):
        name_list.append(input(f"{i + 1} NAME: "))
    
    os.system("cls" if os.name == "nt" else "clear")
    
    file = open("name.txt", "a")
    
    for name in name_list:
        file.write(name.upper() + "\n")
        
    file.close()
    
    file = open("name.txt", "r")
    sort_name = file.readlines()
    sort_name.sort()
    file.close()
    
    file = open("name.txt", "w")
    
    for name in sort_name:
        file.write(name)
        
    file.close()

def view_names():
    file = open("name.txt", "r")
    
    print("ALL NAMES")
    print("----------")
    
    lines = file.read()
    print(lines)
    
    file.close()
    
    print(input("PRESS ANY KEY TO CONTINUE . . ."))
    
def delete_name():
    del_name = int(input("HOW MANY NAME YOU WANT TO DELETE? "))
    to_del_name = []
    
    for i in range(del_name):
        to_del_name.append(input(f"ENTER NAME {i + 1}. ").upper())
    
    os.system("cls" if os.name == "nt" else "clear")
    
    file = open("name.txt", "r")
    all_names = []
    
    for name in file.readlines():
        all_names.append(name.strip())
    
    file.close()
    
    try:
        for name in to_del_name:
            all_names.remove(name)
            
        print(input("SUCCESSFUL DELETED! . . . "))
    except:
         print(input("No Such Name! . . ."))
            
        
    file = open("name.txt", "w")
    
    for name in all_names:
        file.write(name + "\n")
    
    file.close()
    
def main():
    stopper = True
    
    while stopper:
        
        os.system("cls" if os.name == "nt" else "clear")

        print("[1] - ADD NAMES")
        print("[2] - VIEW NAMES")
        print("[3] - DELETE NAMES")
        print("[4] - EXIT")
        choice = int(input(": "))

        os.system("cls" if os.name == "nt" else "clear")
        
        match choice:
            case 1:
                add_name()
                
            case 2:
                view_names()
                
            case 3:
                delete_name()
                
            case 4:
                stopper = False

if __name__ == "__main__":
    main()