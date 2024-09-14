def fibonacci(n):
    # Inicializa os dois primeiros números da sequência
    a, b = 0, 1
    
    # Loop até que 'a' seja maior que 'n'
    while a <= n:
        # Verifica se 'a' é igual a 'n'
        if a == n:
            return True
        # Atualiza os valores de 'a' e 'b'
        a, b = b, a + b
    
    # Retorna False se 'n' não for encontrado na sequência
    return False

# Solicita ao usuário um número
numero = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
