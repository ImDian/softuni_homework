phonebook = {}

while True:
    command = input()

    if command.isdigit():
        break

    name, number = command.split("-")

    if name not in phonebook:
        phonebook[name] = number

x = int(command)

for _ in range(x):
    check_name = input()
    if check_name in phonebook.keys():
        print(f"{check_name} -> {phonebook[check_name]}")
    else:
        print(f"Contact {check_name} does not exist.")

