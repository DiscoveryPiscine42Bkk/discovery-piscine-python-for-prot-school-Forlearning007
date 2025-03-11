mult = 0
while mult <= 10:
    print(f"Table de {mult}: ",end="")
    i = 0
    while i <= 10:
        print(i * mult, end=" ")
        i += 1
    print()
    mult += 1
