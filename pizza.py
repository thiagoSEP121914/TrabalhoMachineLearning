import pandas as pd
import matplotlib.pyplot as plt

# Valor da China (59% do total)
valor_china = 13.4  # bilhões de dólares
percentual_china = 59 / 100  # 59%

# Calculando o valor total das exportações
valor_total = valor_china / percentual_china

# Dados para os outros países
dados = {
    "Ranking": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Países": ["China", "Malásia", "Japão", "Países Baixos", "Omã", "Barein", "Coréia do Sul", "Turquia", "França", "Argentina"],
    "Valor (em bilhões)": [valor_china, 1.85, 1.14, 0.90743, 0.67803, 0.6018, 0.59663, 0.34917, 0.3318, 0.25997]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Ajustando os valores dos outros países proporcionalmente
df['Valor (em bilhões)'] = df['Valor (em bilhões)'].apply(lambda x: x if x == valor_china else (x / sum(df['Valor (em bilhões)'][1:])) * (valor_total - valor_china))

# Criando o gráfico de pizza
plt.figure(figsize=(10, 7))
# Ajuste das etiquetas e das porcentagens
plt.pie(df['Valor (em bilhões)'], labels=df['Países'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, 
        pctdistance=0.85,  # Ajusta a distância das porcentagens
        textprops={'size': 12})  # Tamanho da fonte das porcentagens

# Personalizando o título
plt.title('Distribuição de Valores de Exportação de Ferro', fontsize=16)
plt.axis('equal')  # Garantindo que o gráfico seja circular.

# Exibindo o gráfico
plt.show()
