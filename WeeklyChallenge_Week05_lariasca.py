# CX Programming Club
# Weekly Challenge 5
# lariasca
'''
Model   = SBS , SM  , RU  , 100GE.
----------------------------------
34180YC = 20MB, 16GB, 1RU , 6
3464C   = 22MB, 16GB, 2RU , 64
3432D-S = 70MB, -   , 1RU , 128
3408-S  = 70MB, -   , 4RU , 128

'''
total_switches = []

print("Welcome to the Inventory Program")
print("="*60)

# Ask user if they would like to input new equipment or not
# If not, take list of equipment from program directly.

choice = input("Would you like to input new equipment lists? Y/N: ")

if choice == "Y":
    print("Enter the list of equipment description in the following format:")
    print("Hostname, Shared Buffer Space, System Memory, Rack Unit, Number of 100GE ports in use")

    for x in range(6):
        switch = input(f"Switch {x+1}: ")
        switch = tuple(switch.split(","))
        total_switches.append(switch)
else:
    total_switches = [
        ("nx3k154", "70MB", "-", "1RU", "32"),
        ("nx3k456", "20MB", "16GB", "1RU", "6"),
        ("nx3k234", "70MB", "-", "4RU", "64"),
        ("nx3k222", "22MB", "16GB", "2RU", "64"),
        ("nx3k787", "70MB", "-", "4RU", "33"),
        ("nx3k1", "70MB", "-", "1RU", "32")]

# Consult inventory data

Models = {
    "34180YC": ("20MB", "16GB", "1RU", "6"),
    "3464C": ("22MB", "16GB", "2RU", "6"),
    "3432D-S": ("70MB", "-", "1RU", "128"),
    "3408-S": ("70MB", "-", "4RU", "128")}

Inventory = {}
list34180 = []
list3464 = []
list3432 = []
list3408 = []
listother = []
Nex34180 = 0
Nex3464 = 0
Nex3432 = 0
Nex3408 = 0
Other = 0
i = 0

# Create Inventory dictionary with following format:
# Model: ([Hostnames], Quantity)

for switch in total_switches:
    if switch[i+1] == "70MB" and switch[i+3] == "1RU":
        Nex3432 += 1
        list3432.append(switch[i])
    elif switch[i+1] == "70MB" and switch[i+3] == "4RU":
        Nex3408 += 1
        list3408.append(switch[i])
    elif switch[i+1] == "20MB" and switch[i+3] == "1RU":
        Nex34180 += 1
        list34180.append(switch[i])
    elif switch[i+1] == "22MB" and switch[i+3] == "2RU":
        Nex3464 += 1
        list3464.append(switch[i])
    else:
        Other += 1
        listother.append(switch[i])

Inventory["Model:3432D-S"] = (list3432, "Qty: "+str(Nex3432))
Inventory["Model:3408-S"] = (list3408, "Qty: "+str(Nex3408))
Inventory["Model:34180YC"] = (list34180, "Qty: "+str(Nex34180))
Inventory["Model:3464C"] = (list3464, "Qty: "+str(Nex3464))
Inventory["Other"] = (listother, "Qty: "+str(Other))

# Print Inventory Data

print(f'''
INVENTORY OF NEXUS SWITCHES

Acronyms: SBS, SM, RU, 100GE

SBS = Shared Buffer Space
SM = System Memory
RU = Rack Unit
100GE = Number of 100 GE Ports IN USE

Model 3432D-S:
    Characteristics: (SBS, SM, RU, 100GE)
    {Models["3432D-S"]}
    Inventory: ([List of hostnames], Quantity)
    {Inventory["Model:3432D-S"]}
Model 3408-S:
    Characteristics: (SBS, SM, RU, 100GE)
    {Models["3408-S"]}
    Inventory: ([List of hostnames], Quantity)
    {Inventory["Model:3408-S"]}
Model 34180YC:
    Characteristics: (SBS, SM, RU, 100GE)
    {Models["34180YC"]}
    Inventory: ([List of hostnames], Quantity)
    {Inventory["Model:34180YC"]}
Model 3464C:
    Characteristics: (SBS, SM, RU, 100GE)
    {Models["3464C"]}
    Inventory: ([List of hostnames], Quantity)
    {Inventory["Model:3464C"]}
Model Other:
    >>Any other switch not fitting in above categories.
    Inventory: ([List of hostnames], Quantity)
    {Inventory["Other"]}
''')
