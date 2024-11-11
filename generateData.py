import pandas as pd
import random

# Definindo os valores para cada atributo
idades = ["Jovem", "Adulto", "Idoso"]
rendas = ["Baixa", "Média", "Alta"]
localizacoes = ["Urbano", "Rural"]

# Gerando uma lista de dicionários para os objetos (linhas da tabela)
dados = [
    {
        "Idade": random.choice(idades),
        "Renda": random.choice(rendas),
        "Localizacao": random.choice(localizacoes)
    }
    for _ in range(40)
]

# Criando o DataFrame
df = pd.DataFrame(dados)

# Salvando em um arquivo Excel na pasta atual
output_path = "dados_para_arvore_decisao.xlsx"
df.to_excel(output_path, index=False)

print("Arquivo salvo como:", output_path)