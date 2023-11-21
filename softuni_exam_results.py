command = input()

grades = {}
submissions = {}

while command != "exam finished":
    info = command.split("-")
    username = info[0]
    language = info[1]

    if language != "banned":
        points = int(info[2])

        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

        if username not in grades:
            grades[username] = points

        elif grades[username] < points:
            grades[username] = points

    else:
        del grades[username]

    command = input()

print("Results:")
for username, points in grades.items():
    print(f"{username} | {points}")

print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")