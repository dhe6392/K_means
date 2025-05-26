# K-Means Clustering: Classificação de Faculdades

Este projeto aplica o algoritmo de clusterização **K-Means** ao conjunto de dados `College_Data.csv`, que contém informações sobre faculdades americanas. O objetivo é verificar se o modelo consegue **separar corretamente instituições públicas e privadas** sem usar os rótulos durante o treinamento.

## 📁 Arquivos

- `projeto.py`: script principal com leitura dos dados, treinamento do modelo K-Means e avaliação da clusterização.
- `College_Data.csv`: base de dados usada no projeto, extraída do repositório da Udemy (curso de Machine Learning com Python).

## ⚙️ O que o script faz

1. Lê os dados e transforma a variável "Private" em binária (1 = privada, 0 = pública).
2. Aplica K-Means com 2 clusters (`k = 2`).
3. Ajusta os rótulos do modelo para garantir que `1 = privada`, respeitando a lógica do dataset.
4. Gera a matriz de confusão e o relatório de classificação para avaliar a qualidade da clusterização.

## 📊 Tecnologias usadas

- Python
- Pandas
- Scikit-learn

## ✅ Resultado esperado

Apesar de K-Means não utilizar os rótulos verdadeiros, o modelo consegue **agrupar razoavelmente bem** faculdades públicas e privadas com base nas variáveis numéricas, alcançando uma **acurácia de ~86%** após ajuste dos rótulos.

## 🧠 Observação

Como K-Means é um algoritmo **não supervisionado**, os rótulos 0 e 1 atribuídos aos clusters são arbitrários. O script faz uma **calibração automática** para alinhar o sentido dos rótulos com o esperado.

