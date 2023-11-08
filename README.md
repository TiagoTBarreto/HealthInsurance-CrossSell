# Projeto de Cross Sell de uma Seguradora de Saúde

<p align="center">
  <img src="https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/5be72c6e-c4f0-44ce-83c0-ecec156c8c96" width="100%" height="400">
</p>

# 1. Problema de Negócio
Nosso cliente é uma seguradora que oferece Seguro Saúde aos seus clientes, agora eles precisam da construção de um modelo para prever se os segurados (clientes) do ano passado também terão interesse no Seguro Automóvel oferecido pela empresa.

Construir um modelo para prever se um cliente estaria interessado no seguro automóvel é extremamente útil para a empresa porque ela pode então planejar a sua estratégia de comunicação para chegar a esses clientes e optimizar o seu modelo de negócio e receitas.

# 2. Ferramentas Utilizadas

**Ferramentas para Análise de Dados**
- Python 3.11.4: A linguagem de programação principal usada para desenvolver o projeto.
- Ferramentas Estatísticas para Análise dos Dados (Information Value, Histogramas, Boxplot).

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
 
# 5. Descrição da solução
Foi empregado o método de gerenciamento CRIPS-DM, que tem como objetivo o desenvolvimento de projetos de Data Science de forma cíclica. Esse método é abrangente e, ao concluir um ciclo, você obterá:
- Uma versão completa da solução.
- Maior rapidez na entrega de valor.
- Mapeamento de todos os possíveis problemas.

O CRIPS-DM é composto pelos seguintes passos: 
![image](https://github.com/TiagoTBarreto/Rossmann_Sales/assets/137197787/f4cac96f-a228-4e28-b5a2-eb16f29d5a39)

# 6. Top Insights
### H1. Clientes que tem histórico de acidentes podem ter maior interesse em adquirir o seguro de veículo. 
**VERDADEIRO** O fator histórico de acidentes contribui significamente para o interesse do cliente.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/f5f9b812-1e41-4fdf-88f8-116e93aa5a25)

### H2. A idade pode ser um fator diferencial, com clientes mais jovens tendo menos interesse.
**VERDADEIRO** Clientes com idade entre 35 e 50 são os mais interessados, jovens realmente tem pouco interesse.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/994bd526-2bd2-4938-bc98-dfce2388a672)

### H3. Clientes com carros novos podem ter maior interesse em aderir ao seguro de carro.
**FALSO** Clientes com carros mais velhos e usados tem maior interesse.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/84aea930-9456-4d4f-b32a-1cd62e53cf39)

Inicialmente, pode parecer que a condição do carro é o fator determinante para o interesse, no entanto, na realidade, a idade das pessoas é o principal influenciador por trás desse comportamento.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/46bf7be0-9e9e-4735-9c90-a19bd18ebb25)

### H4. O valor cobrado pode impactar no interesse do seguro de veículo.
**VERDADEIRO** Seguros na faixa de 10000 a 20000 tem menos clientes interessados.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/7b487e2a-a7d1-451a-96ba-1fd234b0b58c)

Da mesma forma que a hipótese anterior, à primeira vista, pode parecer que o valor do seguro tem uma influência direta no interesse. No entanto, ao analisar os segundo e terceiro gráficos, torna-se evidente que as três faixas etárias com menor interesse são aquelas que têm uma grande quantidade de pessoas com idades entre 20 e 35 anos.

### H5. Clientes que moram em regiões específicas podem ter maior interesse no seguro.
**VERDADEIRO** Pessoas que moram na região 28 tem maior interesse no seguro.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/bbcd2347-e67c-4d55-ac48-110de27ac001)

## Insights acionáveis:
Se o projeto chegasse a esse ponto e não envolvesse a parte de machine learning, seria uma recomendação válida entrar em contato com os seguintes grupos de clientes:
1. Aqueles com faixa etária entre 35 e 50 anos, pois demonstraram maior interesse no seguro.
2. Clientes que relataram já ter sofrido acidentes, uma vez que essa experiência aumenta a probabilidade de interesse no seguro.
3. Clientes que residem na região 28.
4. Observar que a longevidade dos clientes na base não parece ter um impacto significativo no interesse pelo novo seguro.

Essas recomendações podem ajudar a direcionar as estratégias de contato e vendas para maximizar as chances de sucesso.

# 7. Machine Learning
- KNN Classifier
- Random Forest Classifier
- Logistic Regression
- XGBoost Classifier

**Após uma análise das métricas com Cross-Validation de 5 splits, o XGBoost demonstrou o melhor desempenho. Portanto, optei por prosseguir com esse modelo para a próxima fase do projeto.**

| Models CV            | Precision at k  | Recall at k  | F1-Score at k  |
|----------------------|------------------|--------------|----------------|
| XGBoost              | 0.396       | 0.265      | 0.318       |
| Random Forest        | 0.360       | 0.240      | 0.288       |
| LogisticRegression   | 0.348       | 0.233      | 0.279       |
| KNN                 | 0.330       | 0.221      | 0.265       |


**Após a realização do ajuste fino do modelo, ele foi testado com dados de teste, simulando o ambiente de produção, e apresentou o seguinte desempenho:**
| Model       | Precision at k  | Recall at k  | F1-Score at k  |
|-------------|------------------|--------------|----------------|
| XGBoost     | 0.424         | 0.181     | 0.254       |


# 8. Tradução do modelo de Machine Learning
O gráfico abaixo ilustra que, ao entrar em contato com os primeiros clientes da lista, a probabilidade de eles adquirirem o seguro é alta, resultando em lucros consideráveis. No entanto, à medida que a lista é explorada mais profundamente, a propensão a adquirir o seguro diminui, o que leva a uma redução na margem de lucro devido ao custo de contato.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/7ed17bc2-fddc-463e-9e5a-fe942bf043fc)

Assumindo que a empresa esteja disposta a se comunicar com possíveis interessados e que obtenha um lucro bruto de R$ 600,00 para cada cliente que adquira o seguro de veículo. Mas também há um custo de R$ 50,00 cada vez que entrar em contato com um potencial cliente.
- Lucro ligando até o cliente 33817 (44% da base): R$3.696.372,00
- Lucro ligando para toda a base. R$1.782.302,00
  
Um lucro 2.07x maior usando o modelo.

## 8.1 Lift Curve

Ao analisar o gráfico, é possível observar que ao entrar em contato com 20% da base de clientes usando o modelo, a empresa alcançará praticamente três vezes mais pessoas.

![image](https://github.com/TiagoTBarreto/HealthInsurance-CrossSell/assets/137197787/cb687c78-eb56-49bb-8b95-70ab06d9e6a5)

# 9. O produto final do projeto
WebApp online, hospedado no Streamlit Cloud e integrado com o modelo que está no Render, está disponível para acesso em qualquer dispositivo conectado à internet, possibilitando que qualquer consumidor tenha acesso ao modelo. Você pode acessar o WebApp através do seguinte link: https://rossmann-sales-forecast.streamlit.app/

![image](https://github.com/TiagoTBarreto/Rossmann_Sales/assets/137197787/c8540192-01d1-41df-9b1a-1bef31cba492)
**A imagem acima é do WebApp, como pode se observar na barra lateral tem 3 filtros:**
- ID Store: Este filtro controla o número das lojas para as quais a previsão será realizada.
- Sales: Este filtro estabelece um limite de vendas para as lojas que serão exibidas posteriormente no dataframe.
- Budget: Dado que a ideia do CFO é alocar uma parte da receita para reformas, este filtro permite a customização da porcentagem das vendas que será destinada a esse propósito.

**Após a previsão, um dataframe é gerado e pode ser baixado ao clicar no botão "DOWNLOAD CSV", permitindo assim a manipulação desse dataframe de acordo com as necessidades do CFO.**
  
# 10. Conclusão
- O projeto fornece uma solução automatizada para a previsão de vendas das lojas da Rossmann, eliminando a necessidade de previsões manuais feitas por gerentes de loja.
- O modelo de previsão de vendas desenvolvido demonstrou um desempenho consistente na maioria das lojas, com um erro médio de aproximadamente 10%. No entanto, é importante observar que o desempenho pode variar entre as lojas. Portanto, em primeiro lugar, podemos utilizar como referência para o orçamento de reformas as mais de 600 lojas com erro inferior a 10%. Dependendo do desempenho atual do método utilizado para a previsão de vendas, podemos considerar a inclusão das previsões das lojas com erro até 15% ou 20%. No entanto, aquelas que apresentarem um erro superior a esse valor deveriam ser discutidas com o CFO, e não devemos considerar as previsões das lojas 292 e 909, que possuem erros superiores a 50%.
- Uma das principais descobertas foi que as lojas que realizam promoções consecutivas tendem a vender em média menos. Isso pode ser útil para o CFO ao tomar decisões sobre a alocação de recursos para promoções.
- Outra descoberta importante foi que as lojas com competidores mais próximos tendem a vender em média mais. Isso pode ser uma informação valiosa ao considerar a localização das lojas e a concorrência.

# 11. Próximo passos
Se fosse continuar o trabalho nesse projeto, realizando um segundo ciclo do CRISP-DS, consideraria os seguintes passos para tentar criar um novo modelo para as lojas com baixo desempenho ou melhorar o desempenho geral do modelo atual, sem outliers com grandes erros:
- Conduzir uma análise aprofundada para identificar as particularidades das lojas com baixo desempenho que estão dificultando a precisão das previsões do modelo.
- Coletar mais Dados.
- Efetuar a criação de novas variáveis a partir do conjunto de dados já existente.
- Experimentar diferentes modelos de Machine Learning.
- Formulação de novas hipóteses para gerar novos insights para o negócio.
