from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from scipy.stats import entropy
import numpy as np
import pandas as pd

df = pd.read_excel("dados_para_arvore_decisao.xlsx")

df_encoded = df.copy()
df_encoded['Idade'] = df_encoded['Idade'].map({"Jovem": 0, "Adulto": 1, "Idoso": 2})
df_encoded['Renda'] = df_encoded['Renda'].map({"Baixa": 0, "Média": 1, "Alta": 2})
df_encoded['Localizacao'] = df_encoded['Localizacao'].map({"Urbano": 0, "Rural": 1})

X = df_encoded[['Idade', 'Renda']]
y = df_encoded['Localizacao']

target_counts = y.value_counts(normalize=True)
target_entropy = entropy(target_counts, base=2)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

y_pred = tree_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(target_entropy, accuracy)
