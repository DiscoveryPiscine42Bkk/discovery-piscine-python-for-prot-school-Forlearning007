print("Enter a number less than 25")
Loop = int(input(" "))  

if Loop > 25:
    print("Error")
else:
    Loop1 = int(input("Enter another number less than 25: "))
    for i in range(Loop1, 26):
        print(f"Inside the loop, my variable is {i}")
