#ask a name
print("Enter a Fullname for their Information")
name = input("Enter Fullname:")
with open("./output.txt", "r") as file:
    infos = file.read().split(f" \n")
    for info in infos:
        if f"Fullname:{name}" in info:
            print(info)