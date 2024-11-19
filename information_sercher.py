#ask a name
print("Enter a Fullname for their Information")
name = input("Enter Fullname:")
#finding name in file
found = False
with open("informations.txt", "r") as file:
    infos = file.read().split(" \n")
    for info in infos:
        if f"Fullname:{name}" in info:
            print(info)
            found = True
            break

if not found:
    print(f"No Info on:{name}")