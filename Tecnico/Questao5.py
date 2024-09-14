def inverter_string(s):
    # Inicializa a string invertida
    invertida = ""
    
    # Adiciona cada caractere da string original na frente da string invertida
    for char in s:
        invertida = char + invertida
    
    # Retorna a string invertida
    return invertida

# Solicita ao usuário uma string
string = input("Informe uma string: ")

# Imprime a string invertida
print(f"String invertida: {inverter_string(string)}")
