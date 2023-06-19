# Método de Borda

Este é um programa em Python que implementa o método de Borda proposto por Jean Charles de Borda. O método de Borda é um método de votação e classificação usado para determinar um ranking ou ordenação de alternativas com base nas preferências dos votantes.

## Descrição do Método de Borda

O método de Borda envolve os seguintes passos:

1. Definição das alternativas: Enumerar todas as alternativas que serão consideradas na votação.

2. Atribuição de pontuações: Cada votante atribui uma pontuação para cada alternativa, com base em sua preferência. As pontuações são geralmente atribuídas em ordem decrescente de preferência, onde a alternativa preferida recebe a maior pontuação.

3. Contagem dos pontos: Somar as pontuações atribuídas a cada alternativa em todas as votações.

4. Ordenação das alternativas: As alternativas são ordenadas de acordo com o total de pontos recebidos. A alternativa com o maior total de pontos é considerada a mais preferida e é colocada em primeiro lugar no ranking. A alternativa com o segundo maior total de pontos é colocada em segundo lugar, e assim por diante.

## Descrição do Programa

O programa em Python permite que o usuário insira as alternativas e critérios, colete as classificações das alternativas em relação a cada critério e calcule a soma dos pontos para cada alternativa. Além disso, o programa adiciona uma coluna chamada "Ordenação Final", onde as alternativas são ordenadas em ordem crescente com base na coluna "Total". Dessa forma, o programa fornece um ranking das alternativas usando o método de Borda.

## Requisitos

- Python 3.x
- Biblioteca pandas

## Executando o Programa

1. Certifique-se de ter o Python instalado em seu ambiente.

2. Instale a biblioteca pandas usando o comando `pip install pandas`.

3. Execute o programa Python.

4. Siga as instruções no terminal para inserir as alternativas, critérios e classificações.

5. O programa exibirá a tabela de classificações com as alternativas, critérios, coluna "Total" e coluna "Ordenação Final".

## Exemplo de Uso

Aqui está um exemplo de como o programa pode ser usado:

```shell
Quantas alternativas você deseja inserir? 3
Digite a alternativa 1: A
Digite a alternativa 2: B
Digite a alternativa 3: C

Quantos critérios você deseja inserir? 2
Digite o critério 1: C1
Digite o critério 2: C2

Classificação para o critério C1
Digite a classificação para a alternativa A: 2
Digite a classificação para a alternativa B: 1
Digite a classificação para a alternativa C: 3

Classificação para o critério C2
Digite a classificação para a alternativa A: 3
Digite a classificação para a alternativa B: 2
Digite a classificação para a alternativa C: 1

Tabela de Classificações:

   C1  C2  Total  Ordenação Final
A  2   3      5               2
B  1   2      3               1
C  3   1      4               3
