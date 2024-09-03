def pertence_fibonacci(n):
    
    fib_1 = 0
    fib_2 = 1
    
    if n == fib_1 or n == fib_2:
        return f"O número {n} pertence à sequência de Fibonacci."

    while fib_2 < n:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    
    if fib_2 == n:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."
    
numero = int(input("Informe um número: "))
resultado = pertence_fibonacci(numero)
print(resultado)