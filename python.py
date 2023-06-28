def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Ingresa un número: "))
resultado = factorial(num)
print("El factorial de", num, "es", resultado)
