#IMPORTS
import random as r

#FUNCTIONS/PROCEDURES
def menu():
    print("1) VIEW CURRENTLY LOADED DATASET\n"
          "2) ADD NEW PRODUCT\n"
          "3) SEARCH NAME\n"
          "4) SEARCH ID\n"
          "5) SAVE CURRENTLY LOADED\n"
          "6) LOAD DATASET\n"
          "   (OVERWRITES CURRENTLY LOADED)\n"
          "7) DELETE PRODUCT\n"
          "A) CREAT DATASET\n"
          "CHOICE: ", end = "")


def addNewProduct(dataset, productID, name, depart, location, quantity, price):
    if len(str(productID)) != 7 or type(productID) != type(0):
        return False

    dataset[name] = {}
    dataset[name]["productID"] = productID
    dataset[name]["department"] = depart
    dataset[name]["location"] = location
    dataset[name]["quantity"] = quantity
    dataset[name]["price"] = price
    dataset[name]["pricevat"] = (price * 1.2)
    return True

def deleteProduct(dataset,prodid):
    for x in dataset:
        if dataset[x]["productID"] == prodID:
            dataset.pop([x])
            return True
    return False


def searchDict(dataset, lookingfor, prodid = False):
    if prodid:
        for x in dataset:
            if dataset[x]["productID"] == lookingfor:
                print([x, dataset[x]])
        print(lookingfor + " not found")
    else:
        found = False
        for x in dataset:
            if lookingfor.lower() in x.lower():
                found = True
                print(x + " found at " + dataset[x]["location"] + "(ID: " + str(dataset[x]["productID"])+ ")")
        if not found:
            print(lookingfor + " not found.")

def createDataSet(productSet,dataset, items):
    for x in range(items):
        department = r.choice(list(productSet.keys()))
        addNewProduct(dataset, r.randint(1000000,9999999), r.choice(productSet[department]), department, (chr(r.randint(65,90)) + str(r.randint(0,9))), r.randint(0,400), r.randint(1,500))

def saveTo(dataset, filename = "Products"):
    file = open(filename + ".txt", 'w')
    for x in dataset:
        file.write(x + str(dataset[x]) + "\n")
    file.close()
    file = open(filename + "RAW.txt", 'w')
    file.write(str(dataset))
    file.close()
    print("Save Success")

def loadDataset(dataset, filename):
    try:
        file = open(filename + "RAW.txt", 'r')
        dataset.update(eval(file.read()))
        file.close()
        return True
    except FileNotFoundError:
        print("File not found")
        return False
    
    



#MAIN
productExam = {
    "power tools": ["Drill", "Nail Gun", "Sanders", "Power Saw"],
    "power toolsA": ["Vacuum", "Water Pump", "Inflators", "Heat guns"],
    "hand tools": ["Pencil","Pen","Hand Saw", "Hammer", "Wrench", "Pliers", "Scissors", "Vise"],
    "tool storage": ["Wood Shelf 15m", "Wood Shelf 20m", "Metal shelf 10m", "Cuboard  10x1", "Cuboard 20x1"],
    "measuring tools": ["Measuring Tape", "Ruler", "Yard sticks", "Meter Sticks"],
    "testing equip": ["Spirit level", "Try Square", "Straight Edge"],
    "heating plumbing": ["Pipe wrench", "Basin wrench", "Faucet Key", "Pipe cutters"],
    "electrical light": ["LED Bulb", "Fluorescent Bulb","Wire Cutters"],
    "screws nails": ["Flooring Nails", "Box Nails", "Wood Screw", "Machine Screws"]
    }

current = {
    }


while True:
    menu()
    choice = input()
    if choice == "1":
        for x in current:
            print(x)
            print(current[x])
    
    elif choice == "2":
        if addNewProduct(current, int(input("Product ID: ")),input("Name: "),input("Department: "),input("Location: "),input("Quantity: "),float(input("Price: "))):
            print("New product added successfully")
        else:
            print("Product add unsuccessful")

    elif choice == "3":
        searchDict(current, input("Looking for: "))
        
    elif choice == "4":
        searchDict(current, input("Looking for: "), True)
        
    elif choice == "5":
        saveTo(current, input("Enter File you want to save to,\n(if it doesnt exsist one will be created): "))
        
    elif choice == "6":
        if loadDataset(current, input("Enter file you want to load: ")):
            print("Load successful")
        else:
            print("Load unsuccesful/File not found")

    elif choice = "7":
        if loadDataset(current, input("Enter product you want to delete: ")):
            print("Product deleted")
        else:
            print("Product not found")
    
    elif choice.upper() == "A":
        createDataSet(productExam, current, int(input("How many items? ")))
    else:
        print("invalid choice")
         
        

