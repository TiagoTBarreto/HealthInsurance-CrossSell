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
| Campo                       | Descrição                                                                                      |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| Id                          | Um ID que representa um par (Loja, Data) no conjunto de teste.                                  |
| Store                       | Um ID exclusivo para cada loja.                                                                |
| Sales                       | O faturamento para um determinado dia (o que você está prevendo).                                |
| Customers                   | O número de clientes em um determinado dia.                                                  |
| Open                        | Um indicador de se a loja estava aberta: 0 = fechada, 1 = aberta.                                  |
| StateHoliday                | Indica um feriado estadual. Normalmente, todas as lojas, com poucas exceções, estão fechadas em feriados estaduais. Observe que todas as escolas estão fechadas em feriados públicos e fins de semana. a = feriado público, b = feriado de Páscoa, c = Natal, 0 = Nenhum. |
| SchoolHoliday               | Indica se o (Loja, Data) foi afetado pelo fechamento das escolas públicas.                       |
| StoreType                   | Diferencia entre 4 modelos diferentes de loja: a, b, c, d.                                       |
| Assortment                  | Descreve um nível de sortimento: a = básico, b = extra, c = estendido.                              |
| CompetitionDistance         | Distância em metros para a loja concorrente mais próxima.                                       |
| CompetitionOpenSince[Month/Year] | Dá o ano e mês aproximados em que o concorrente mais próximo foi aberto.                        |
| Promo                       | Indica se uma loja está executando uma promoção naquele dia.                                     |
| Promo2                      | Promo2 é uma promoção contínua e consecutiva para algumas lojas: 0 = loja não está participando, 1 = loja está participando.                                       |
| Promo2Since[Year/Week]      | Descreve o ano e a semana do calendário em que a loja começou a participar da Promo2.             |
| PromoInterval               | Descreve os intervalos consecutivos em que a Promo2 é iniciada, nomeando os meses em que a promoção é reiniciada. Por exemplo, "Fev, Mai, Ago, Nov" significa que cada rodada começa em fevereiro, maio, agosto, novembro de qualquer ano para essa loja.             |

  
# 5. Descrição da solução
Foi empregado o método de gerenciamento CRIPS-DM, que tem como objetivo o desenvolvimento de projetos de Data Science de forma cíclica. Esse método é abrangente e, ao concluir um ciclo, você obterá:
- Uma versão completa da solução.
- Maior rapidez na entrega de valor.
- Mapeamento de todos os possíveis problemas.

O CRIPS-DM é composto pelos seguintes passos: 
![image](https://github.com/TiagoTBarreto/Rossmann_Sales/assets/137197787/f4cac96f-a228-4e28-b5a2-eb16f29d5a39)

# 6. Top 2 Insights
## 1.0 Lojas com mais promoções consecutivas vendem em média menos.
![image](https://github.com/TiagoTBarreto/Rossmann_Sales/assets/137197787/6cd3c587-2132-466c-b232-48e6c2c0c533)

## 2.0 Lojas com competidores mais próximos vendem em média mais.
![image](https://github.com/TiagoTBarreto/Rossmann_Sales/assets/137197787/af62eb8f-6d2e-43d9-ac95-004e6a97154e)

# 7. Machine Learning
- Average Model
- Linear Regression
- Linear Regression Regularized
- Random Forest Regressor
- XGBoost Regressor

![image](https://github.com/TiagoTBarreto/Rossmann_Sales/assets/137197787/b5b0fe72-2045-407c-a875-ddad43dc766d)

**Após uma análise das métricas com Cross-Validation de 5 splits a Random Forest apresentou o melhor desempenho, mas optei pelo XGBoost para a próxima fase pelos seguintes motivos:** 
- Requer significativamente menos armazenamento.
- Apresenta um processamento consideravelmente mais rápido
- Oferece economia em termos de custos computacionais.

# 8. Tradução do modelo de Machine Learning
O modelo previu vendas de R$ 282 milhões para as próximas 6 semanas. Devido ao seu erro médio de 10%, ele pode, na pior das hipóteses, subestimar o valor em 10% ou superestimar em 10%, como pode ser observado no dataframe a seguir, que apresenta o número de vendas previsto, o melhor cenário e o pior cenário.

![image](https://github.com/TiagoTBarreto/Rossmann_Sales/assets/137197787/75cb0041-fb29-4244-911e-255b4b2799ce)

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
