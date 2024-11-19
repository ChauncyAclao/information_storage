
#inputing information
infos = []

while True:
    name = input("Name: ")
    if not len(name) > 0:
        print("Invalid")
        continue

    birthdate = input("birthdate: ")
    if not len(birthdate) > 0:
        print("invalid")
        continue

    section = input("section: ")
    if not len(section) > 0:
        print("invalid")
        continue

    address = input("Home address: ")
    if not len(address) > 0:
        print("Invalid")
        continue

    email = input("Email: ")
    if not len(email) > 0:
        print("Invalid")
        continue

    infos.append({
        "name" : name,
        "birthdate" : birthdate,
        "section" : section,
        "adress" : address,
        "email" : email
    })

    with open("./output.txt", "a") as file_handle:
        file_handle.write(name)

    new_entry = input("Give new entry?(yes or no): ")
    if new_entry == "no":
        break

print(infos)



