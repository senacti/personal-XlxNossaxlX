filas =  5
for i in range(1, filas +  1):
    for j in range(filas - i):
        print(" ", end="")
    for k in range(1, i +  1):
        print(k, end=" ")
    print()


