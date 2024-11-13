# TrabalhoMachineLearning
Modelo de Detecção de Intrusões - KDD Cup 1999
Este projeto foi desenvolvido como parte de um trabalho de estudante e utiliza técnicas de Machine Learning para detectar intrusões em redes de computadores. O modelo de Árvore de Decisão foi treinado utilizando o conjunto de dados KDD Cup 1999, que contém informações sobre atividades de rede e foi projetado para detectar ataques em sistemas computacionais.

O que é o KDD Cup 1999?
O KDD Cup 1999 é um conjunto de dados utilizado em uma competição de Data Mining focada na detecção de intrusões em redes de computadores. O conjunto contém uma série de registros sobre atividades de rede, com rótulos indicando se a atividade é normal ou corresponde a um tipo específico de ataque, como DoS (Denial of Service), U2R (User to Root), R2L (Remote to Local), ou Probe.

Objetivo do Projeto
O objetivo deste projeto é treinar um modelo de Árvore de Decisão para classificar os registros de rede como normais ou ataques. Utilizamos o algoritmo para prever a classe (normal ou ataque) com base em uma série de características da rede, como:

Tipo de protocolo
Número de bytes enviados
Número de falhas de login
Taxas de erro e sucesso
O modelo foi treinado com 80% dos dados, e a avaliação foi feita com os 20% restantes.

Metodologia
Pré-processamento de Dados:

O conjunto de dados foi carregado e as colunas relevantes foram definidas.
O rótulo de "target" foi transformado em uma variável binária (0 = normal, 1 = ataque).
Variáveis categóricas (como protocol_type, service, flag) foram convertidas para códigos numéricos.
Divisão dos Dados:

Os dados foram divididos em conjunto de treinamento (80%) e teste (20%) usando train_test_split.
Treinamento do Modelo:

Um modelo de Árvore de Decisão foi treinado com os dados de treinamento. O modelo foi ajustado para considerar o balanceamento de classes, o que é importante, pois os ataques são menos frequentes do que as atividades normais.
Avaliação do Modelo:

A Matriz de Confusão e o Relatório de Classificação foram gerados para avaliar o desempenho do modelo em termos de precisão, recall e f1-score.
Foi realizado um filtro específico para avaliar apenas os dados relacionados a ataques, para obter uma análise detalhada dessa classe.
Resultados
Após o treinamento do modelo, as principais métricas de avaliação foram apresentadas:

Matriz de Confusão: Mostra os resultados da classificação, incluindo o número de verdadeiros positivos, falsos positivos, verdadeiros negativos e falsos negativos.
Relatório de Classificação: Apresenta as métricas de avaliação para cada classe (normal e ataque), incluindo precisão, recall e f1-score.
Além disso, foi gerado um relatório específico para os ataques, separando as métricas para essa classe.

Requisitos
Python 3.x
Bibliotecas:
pandas
scikit-learn
matplotlib
Como Rodar o Projeto
Baixar o Conjunto de Dados: Baixe o conjunto de dados KDD Cup 1999 (10% corrigido) aqui e salve no mesmo diretório do script com o nome kddcup.data_10_percent_corrected.
Instalar as Dependências:
bash
Copiar código
pip install pandas scikit-learn matplotlib
Executar o Código: Basta rodar o script Python:
bash
Copiar código
python nome_do_arquivo.py
Observações
Este modelo foi desenvolvido como um experimento inicial para a detecção de intrusões em redes. Algumas melhorias podem ser feitas, como a experimentação com outros algoritmos de aprendizado de máquina (por exemplo, Random Forest, SVM) e ajustes adicionais no pré-processamento de dados.

