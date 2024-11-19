#ask a name
print("Enter a Fullname for their Information")
name = input("Enter Fullname:")
with open("./output.txt", "r") as file:
    infos = file.read().split(f" \n")
    for info in infos:
        if f"Fullname:{name}" in info:
            print(info)
            break

        if f"Fullname:{name}" not in info:
            print(f"No Info on:{name}")
            break