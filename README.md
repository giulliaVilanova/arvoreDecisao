# Projeto de Análise de Dados com Árvores de Decisão e Random Forest

Este projeto consiste em um estudo de classificação utilizando uma árvore de decisão e explorando o conceito de entropia e Random Forest.

## Estrutura do Projeto

1. **Geração do Dataset**: Criamos um banco de dados fictício com 40 objetos, cada um possuindo três atributos:
   - **Idade**: Faixas etárias como "Jovem", "Adulto", "Idoso".
   - **Renda**: Níveis de renda como "Baixa", "Média", "Alta".
   - **Localização**: Ambiente onde o indivíduo vive, "Urbano" ou "Rural".

2. **Cálculo da Entropia**: 
   - Utilizamos a entropia para medir a incerteza da variável alvo `Localização`. A entropia ajuda a entender o nível de desordem inicial e fundamenta as divisões da árvore de decisão.

3. **Árvore de Decisão**: 
   - Implementamos uma árvore de decisão usando `scikit-learn`. O modelo é treinado para prever a `Localização` com base nos atributos `Idade` e `Renda`.
   - Dividimos os dados em conjunto de treino (70%) e teste (30%) e medimos a acurácia das previsões para avaliar o modelo.

4. **Random Forest**:
   - Incluímos uma pesquisa sobre Random Forest, explicando como o modelo combina várias árvores de decisão para melhorar a performance e reduzir o risco de overfitting.
   - Foi demonstrado um exemplo de aplicação do Random Forest no conjunto de dados para ilustrar a abordagem.

## Pré-requisitos

- **Python 3.x**
- **Bibliotecas**:
  - `pandas` para manipulação de dados
  - `scikit-learn` para modelagem da árvore de decisão e Random Forest
  - `scipy` para cálculo de entropia

## Como Executar

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/giulliaVilanova/arvoreDecisao.git
   cd arvoreDecisao
2. **Instale as dependências:**
    ```bash
   pip install pandas scikit-learn scipy

3. **Gere o Arquivo de Dados:**
- Execute o script para criar o dataset em .xlsx:
    ```bash
   python gera_dados.py
4. **Execute a Análise:**
    ```bash
   python analise_arvore_decisao.py
   
## Resultados

- Entropia Inicial: 0.971
- Acurácia da Árvore de Decisão: 50%
- Os resultados mostram a incerteza inicial dos dados e a performance do modelo ao usar Idade e Renda como variáveis preditoras para Localização.

## Referências

- Documentação do scikit-learn para Árvores de Decisão e Random Forest: https://scikit-learn.org/stable/
- Documentação do scipy para cálculo de entropia: https://docs.scipy.org/

