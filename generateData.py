import pandas as pd
import random

idades = ["Jovem", "Adulto", "Idoso"]
rendas = ["Baixa", "Média", "Alta"]
localizacoes = ["Urbano", "Rural"]

dados = [
    {
        "Idade": random.choice(idades),
        "Renda": random.choice(rendas),
        "Localizacao": random.choice(localizacoes)
    }
    for _ in range(40)
]

df = pd.DataFrame(dados)

output_path = "dados_para_arvore_decisao.xlsx"
df.to_excel(output_path, index=False)

print("Arquivo salvo como:", output_path)