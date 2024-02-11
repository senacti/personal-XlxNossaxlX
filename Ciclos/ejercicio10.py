def patron_Z(filas):
    for i in range(filas):
        for j in range(filas):
            if i == 0 or i == filas - 1:
                print("*", end="")
            elif i + j == filas - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

filas = 7  
patron_Z(filas)
