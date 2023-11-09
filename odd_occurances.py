words = input().split()

list = []

for word in words:
    if words.count(word) % 2 != 0 and word not in list:
        list.append(word)

test = "Kuche"

test.lower()

