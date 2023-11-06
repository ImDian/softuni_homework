def loading_bar(a: int):
    chars = a // 10
    bar = "["


    for x in range(chars):
        bar += "%"

    for y in range(10 - chars):
        bar += "."

    bar += "]"

    return bar


n = int(input())

print(loading_bar(n))
