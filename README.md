<div style="width: 100%;">


# Projeto de Cross Sell de Seguro de Saúde

<p align="center">
  <img src="https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/5be72c6e-c4f0-44ce-83c0-ecec156c8c96" width="100%" height="400">
</p>

| feature              | unique | faltantes |
|----------------------|--------|-----------|
| id                   | 304887 | 0         |
| gender               | 2      | 0         |
| age                  | 66     | 0         |
| driving_license      | 2      | 0         |
| region_code          | 53     | 0         |
| previously_insured   | 2      | 0         |
| vehicle_age          | 3      | 0         |
| vehicle_damage       | 2      | 0         |
| annual_premium       | 46479  | 0         |
| policy_sales_channel | 154    | 0         |
| vintage              | 290    | 0         |
| response             | 2      | 0         |


# 1. Problema de Negócio
Nosso cliente é uma seguradora que oferece Seguro Saúde aos seus clientes, agora eles precisam da construção de um modelo para prever se os segurados (clientes) do ano passado também terão interesse no Seguro Automóvel oferecido pela empresa.

Construir um modelo para prever se um cliente estaria interessado no seguro automóvel é extremamente útil para a empresa porque ela pode então planejar a sua estratégia de comunicação para chegar a esses clientes e optimizar o seu modelo de negócio e receitas.

# 2. Ferramentas Utilizadas

**Ferramentas para Análise de Dados**
- Python 3.11.4: A linguagem de programação principal usada para desenvolver o projeto.
- Estatística.

**Biblioteca de Machine Learning e Otimização:**
- Scikit-learn: Empregado para a preparação de dados, treinamento de modelos, avaliação de desempenho e validação cruzada.
- XGBoost: Implementação de algoritmo de aprendizado de máquina Gradient Boosting.
- Scikit-Optimize com BayesSearchCV: Utilizado para a busca de hiperparâmetros de forma eficiente.
- ScikitPlot: Utilizada para gerar gráficos informativos no contexto de "Learn to Rank". 
  
**Desenvolvimento e Controle de Versão:**
- Git: Ferramenta de versionamento de código para rastrear alterações e colaboração em equipe.
- Pyenv (Ambiente Virtual): Utilizado para isolar dependências e gerenciar versões do Python.

**Implantação e Exposição do Modelo:**
- Flask: Usado para criar uma API RESTful, permitindo a hospedagem do modelo em produção.

**Habilidades e Abordagem:**
- Pensamento Crítico e Resolução de Problemas: Habilidades fundamentais aplicadas para analisar, solucionar problemas e tomar decisões ao longo do projeto.

# 3. Descrição dos Dados 
| Campo                  | Descrição                                                                           |
|------------------------|-------------------------------------------------------------------------------------|
| ID                     | Identificador único do cliente.                                                   |
| Gênero                 | Gênero do cliente.                                                                 |
| Idade                  | Idade do cliente.                                                                  |
| Carteira de Motorista  | 0: O cliente não possui CNH, 1: O cliente já possui CNH.                             |
| Código de Região       | Código único para a região do cliente.                                            |
| Já Segurado Antes      | 1: O cliente já possui Seguro de Veículo, 0: O cliente não possui Seguro de Veículo. |
| Idade do Veículo       | Idade do veículo.                                                                  |
| Danos no Veículo       | 1: O cliente teve seu veículo danificado no passado, 0: O cliente não teve seu veículo danificado no passado. |
| Prêmio Anual           | O valor que o cliente precisa pagar como prêmio durante o ano.                    |
| Canal de Vendas da Apólice | Código anonimizado para o canal de contato com o cliente, ou seja, diferentes agentes, por correio, por telefone, pessoalmente, etc. |
| Tempo de Associação    | Número de dias que o cliente está associado à empresa.                            |
| Resposta               | 1: O cliente está interessado, 0: O cliente não está interessado.                   |
 
# 4. Descrição da solução
Foi empregado o método de gerenciamento CRIPS-DM, que tem como objetivo o desenvolvimento de projetos de Data Science de forma cíclica. Esse método é abrangente e, ao concluir um ciclo, você obterá:
- Uma versão completa da solução.
- Maior rapidez na entrega de valor.
- Mapeamento de todos os possíveis problemas.

O CRIPS-DM é composto pelos seguintes passos: 
![image](https://github.com/TiagoTBarreto/Rossmann_Sales/assets/137197787/f4cac96f-a228-4e28-b5a2-eb16f29d5a39)

# 5. Top Insights
### H1. Clientes que já tiveram seu veículo danificado podem ter maior interesse em adquirir o seguro de veículo.  
**VERDADEIRO** A ocorrência de incidentes anteriores exerce uma influência significativa no aumento do interesse pelo seguro automotivo.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/f5f9b812-1e41-4fdf-88f8-116e93aa5a25)

### H2. A idade pode ser um fator diferencial, com clientes mais jovens tendo menos interesse.
**VERDADEIRO** Clientes com idade entre 35 e 50 são os mais interessados, jovens realmente tem pouco interesse.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/994bd526-2bd2-4938-bc98-dfce2388a672)

### H3. Clientes com carros novos podem ter maior interesse em aderir ao seguro de carro.
**FALSO** Clientes com carros mais velhos e usados tem maior interesse.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/84aea930-9456-4d4f-b32a-1cd62e53cf39)

Inicialmente, pode parecer que a condição do carro é o fator determinante para o interesse, no entanto, na realidade, a idade das pessoas é o principal influenciador por trás desse comportamento.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/46bf7be0-9e9e-4735-9c90-a19bd18ebb25)

### H4. Diferentes métodos de contato podem impactar o interesse na apólice.
**VERDADEIRO** Os métodos de contato 26.0 e 124.0 apresentam a maior taxa de conversão de clientes interessados na apólice de veículo.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/edb225e4-a02f-4e2a-ae2d-969f348cb07b)

### H5. Clientes que moram em regiões específicas podem ter maior interesse no seguro.
**VERDADEIRO** Pessoas que moram na região 28 tem maior interesse no seguro.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/5fe01c43-c5a1-4530-af17-224c160bcb10)


## Insights acionáveis:
**Se o projeto chegasse a esse ponto e não envolvesse a parte de Machine Learning, seria uma recomendação válida entrar em contato com os seguintes grupos de clientes:**
1. Aqueles com faixa etária entre 35 e 50 anos.
2. Clientes residentes da região 28.
3. Clientes que já tiveram dano em seus veículos.
4. Clientes que não tem seguro de carro.

**E se atentar aos seguintes pontos:**
- Clientes com carros novos e que são jovens tem pouquíssimo interesse no seguro.
- Priorizar os métodos de contato 26 e 124.
- A longevidade do cliente na empresa não é um fator importante.

Essas recomendações vão direcionar as estratégias de contato e vendas para maximizar as chances de sucesso.

# 6. Machine Learning
- KNN Classifier
- Random Forest Classifier
- Logistic Regression
- XGBoost Classifier

**Após uma análise detalhada das métricas utilizando Cross-Validation com 5 splits, o XGBoost destacou-se como o modelo com o melhor desempenho. Diante dessa constatação, optei por avançar para a próxima fase do projeto utilizando este modelo. O valor de K=10.000 utilizado na validação representa 15% do dataset total.**

| Models CV            | Precision at k  | Recall at k  | F1-Score at k  |
|----------------------|------------------|--------------|----------------|
| XGBoost              | 0.370       | 0.453      | 0.407       |
| LogisticRegression   | 0.343       | 0.420      | 0.378       |
| Random Forest        | 0.340       | 0.416      | 0.374       |
| KNN                 | 0.317       | 0.389      | 0.349       |


**Após ajustar o modelo, foi realizado um teste simulando o ambiente de produção. Os resultados foram os seguintes:**
| Model       | Precision at k  | Recall at k  | F1-Score at k  |
|-------------|------------------|--------------|----------------|
| XGBoost     | 0.374         | 0.458     | 0.412      |

**O valor de K utilizado foi de 11.430, correspondendo a 15% do dataset de teste. Observa-se que o modelo apresentou um bom poder de generalização, indicando que não ocorreu overfitting.**

# 7. Tradução do modelo de Machine Learning
O gráfico abaixo ilustra que, ao entrar em contato com os primeiros clientes da lista, a probabilidade de eles adquirirem o seguro é alta, resultando em lucros consideráveis. No entanto, à medida que a lista é explorada mais profundamente, a propensão a adquirir o seguro diminui, o que leva a uma redução na margem de lucro devido ao custo de contato.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/7ed17bc2-fddc-463e-9e5a-fe942bf043fc)

Considerando que a empresa esteja disposta a se comunicar com possíveis interessados e obtenha um lucro bruto de R$ 600,00 para cada cliente que adquira o seguro de veículo, mas também incorra um custo de R$ 50,00 a cada vez que entra em contato com um potencial cliente, observamos o seguinte:
- Lucro ao entrar em contato com os primeiros 33.817 clientes (44% da base): R$3.696.372,00
- Lucro ao entrar em contato com toda a base de clientes: R$1.782.302,00
  
Isso representa um lucro 2.07x maior ao usar o modelo, o que indica que a abordagem do modelo é mais eficaz em maximizar os lucros em comparação com entrar em contato com todos os clientes sem a orientação do modelo.

## 7.1 Lift Curve

Ao analisar o gráfico, é possível observar que ao entrar em contato com 20% da base de clientes usando o modelo, a empresa alcançará praticamente três vezes mais pessoas.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/cb687c78-eb56-49bb-8b95-70ab06d9e6a5)

# 8. O produto final do projeto
O produto final foi uma planilha do Google Sheets conectada com o modelo de Machine Learning em nuvem. Agora, essa planilha pode ser acessada de qualquer dispositivo compatível com o Google Sheets. No vídeo abaixo, apresento uma demonstração da planilha, destacando a funcionalidade de predição. Ao clicar em um botão, a planilha retorna uma lista ranqueada com os clientes mais propensos de adquirirem o seguro. Essa abordagem não apenas simplifica o processo, mas também oferece uma experiência intuitiva para usuários de diferentes dispositivos.

![Animação](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/246de1c3-a38c-4919-894b-2fbcb5361c25)

# 9. Próximo passos
Ao embarcar em um segundo ciclo do CRISP-DM para aprimorar ainda mais este projeto, consideraria as seguintes abordagens:
- Expandir a coleta de dados e informações sobre os clientes para enriquecer ainda mais o conjunto de dados, possibilitando análises mais abrangentes e precisas.
- Explorar novos modelos de Machine Learning.
- Integração com o Excel: Levar a praticidade da predição aos usuários do Excel, integrando o sistema de predição diretamente na plataforma.
- Formulação de Novas Hipóteses: Desenvolver e testar novas hipóteses para gerar insights adicionais para o negócio.


</div>
