
#inputing information
while True:
    fullname = input("Fullname: ")
    if not len(fullname) > 0:
        print("Invalid")
        continue

    birthdate = input("birthdate: ")
    if not len(birthdate) > 0:
        print("invalid")
        continue

    section = input("Section: ")
    if not len(section) > 0:
        print("invalid")
        continue

    address = input("Home address: ")
    if not len(address) > 0:
        print("Invalid")
        continue

    religion = input("Religion: ")
    if not len(religion) > 0:
        print("Invalid")
        continue

    email = input("Email: ")
    if not len(email) > 0:
        print("Invalid")
        continue

    phone = input("Phone number: ")
    if not len(phone) > 0:
        print("Invalid")
        continue

    emergency_contact = input("Emergency contact: ")
    if not len(emergency_contact) > 0:
        print("Invalid")
        continue

    #putting the inputs in a txt file
    with open("informations.txt", "a") as file_handle:
        file_handle.write(f"Fullname:{fullname}\n")
        file_handle.write(f"birthdate:{birthdate}\n")
        file_handle.write(f"section:{section}\n")
        file_handle.write(f"Religion:{religion}\n")
        file_handle.write(f"address:{address}\n")
        file_handle.write(f"email:{email}\n")
        file_handle.write(f"Phone number:{phone}\n")
        file_handle.write(f"Emergency contact:{emergency_contact}\n")
        file_handle.write(f" \n")

    #ask for new entry
    new_entry = input("Give new entry?(yes or no): ")
    if new_entry == "no":
        break
