import json

# Exemplo de dados de faturamento em JSON
dados_faturamento = '''
[
    {"dia": 1, "valor": 1000.0},
    {"dia": 2, "valor": 1500.0},
    {"dia": 3, "valor": 0.0},
    {"dia": 4, "valor": 2000.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 3000.0}
]
'''

# Carrega os dados de faturamento
faturamento = json.loads(dados_faturamento)

# Filtra os valores de faturamento maiores que 0
valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

# Calcula o menor e maior valor de faturamento
menor_valor = min(valores)
maior_valor = max(valores)

# Calcula a média mensal de faturamento
media_mensal = sum(valores) / len(valores)

# Conta os dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

# Imprime os resultados
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
