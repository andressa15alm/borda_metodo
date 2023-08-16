import pandas as pd

num_alternativas = int(input("Quantas alternativas você deseja inserir? "))
respostas = []


num_criterios = int(input("Quantos criterios você deseja inserir? "))
criterios = []

for i in range(num_alternativas):
    resposta = input("Digite a alternativa {}: ".format(i+1))
    respostas.append(resposta)


for i in range(num_criterios):
    criterio = input("Digite o criterio {}: ".format(i+1))
    criterios.append(criterio)

# Coletar a classificação das alternativas para cada critério
classificacoes = {}
for criterio in criterios:
    classificacoes[criterio] = {}
    print("Classificação para o critério", criterio)

    for alternativa in respostas:
        classificacao = int(input("Digite a classificação para a alternativa {}: ".format(alternativa)))
        classificacoes[criterio][alternativa] = classificacao



# DataFrame com as classificações
df = pd.DataFrame(classificacoes, index=respostas)
df["Total"] = df.sum(axis=1)

df["Ordenação Final"] = df["Total"].rank()
print("\nTabela de Classificações:\n")
print(df)
