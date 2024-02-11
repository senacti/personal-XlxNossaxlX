n = int(input("¿Cuántos términos de la secuencia de Fibonacci deseas ver? "))

n1, n2 =  0,  1
count =  0
suma = n1  

if n <=  0:
    print("Por favor ingresa un número entero positivo.")
elif n ==  1:
    print("Secuencia de Fibonacci hasta el término", n, ":")
    print(n1)
else:
    print("Secuencia de Fibonacci:")
    while count < n:
        print(n1, end=" ")
        suma += n1  
        nth = n1 + n2  
        n1 = n2  
        n2 = nth 
        count +=  1

    print("\nLa suma de los primeros {} términos de la secuencia de Fibonacci es: {}".format(n, suma))
