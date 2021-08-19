from matplotlib.pyplot import xlabel, ylabel
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import seaborn as sns

loan_df = pd.read_csv('loan_data.csv')

loan_df['annual.inc'] = np.exp(loan_df['log.annual.inc'])

fig1 = px.histogram(loan_df, x="not.fully.paid", width=1080, height=680)
fig1.update_layout(bargap=0.2)

loan_df["not.fully.paid"] = loan_df["not.fully.paid"].astype(str)
fig2 = px.scatter(loan_df, x="fico",
                  y="revol.util",
                  color="not.fully.paid",
                  trendline="ols",
                  title="Relação taxa de utilização de crédito rotativo e o score FICO",
                  width=1080, height=680)


fig3 = px.scatter(loan_df,
                  x="fico", 
                  y="int.rate",
                  color="not.fully.paid",
                  trendline='ols',
                  title="Relação entre o score FICO e a taxa de juros",
                  width=1080, height=680)

fig4 = px.histogram(loan_df, x="annual.inc", color="not.fully.paid",
                    marginal="violin", # or violin, rug
                    hover_data=loan_df.columns,
                    title='Histograma e Violin plot do Annual Income em relação a not.fully.paid',
                    width=1080, height=680)

fig5 = px.histogram(loan_df, x="installment", color="not.fully.paid",
                    marginal="violin", # or violin, rug
                    hover_data=loan_df.columns,
                    title='Histograma e Violin plot do Installment em relação a not.fully.paid',
                    width=1080, height=680)

fig6 = px.scatter_3d(loan_df, x='int.rate', y='revol.util', z='fico',
                     color='not.fully.paid', 
                     labels={'int.rate':'Interest Rate', 'revol.util': '% Usada de crédito', 'fico': 'FICO Score'},
                      
                     width=1080, height=680)

fig7 = px.bar(loan_df, x="not.fully.paid", barmode="group", facet_col="purpose",
              title='Distribuição dos Propósitos em relação a not.fully.paid',
              category_orders={"purpose": ['debt_consolidation', 'all_other', 'credit_card', 
                                           'home_improvement', 'small_business', 'major_purchase',
                                           'educational']},
              width=1080, height=680)
fig7.update_layout(bargap=0.2)

labels = ['debt_consolidation', 'all_other', 'credit_card', 
          'home_improvement', 'small_business', 'major_purchase',
          'educational']

value0 = loan_df[loan_df['not.fully.paid']==0]['purpose'].value_counts().values
value1 = loan_df[loan_df['not.fully.paid']==1]['purpose'].value_counts().values

# fig8 = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]],
#                     subplot_titles=['Paid', 'Not fully paid'])
# fig8.add_trace(go.Pie(labels=labels, values=value0, scalegroup='one',
#                      name="Purpose for paid"), 1, 1)
# fig8.add_trace(go.Pie(labels=labels, values=value1, scalegroup='one',
#                      name="Purpose for not paid"), 1, 2)

# fig8.update_layout(title_text='Propósito do empréstimo em relação a not.fully.paid')

fig8 = px.pie(loan_df, names='purpose', title='Pie Chart dos propósitos dos empréstimos')

markdown_1 = '''
### Informações das Colunas
* **credit.policy**: 1 se o usuário se encontra sobre os critérios de crédito do LendingClub.com, e 0 caso ao contrário.
* **purpose**: O propósito do empréstimo (recebe valores como "creditcard", "debtconsolidation", "educational", "majorpurchase", "smallbusiness", and "all_other").
* **int.rate**: Juros do empréstimo, como uma proporção (se a taxa de juros for 11% será registrada como 0.11).
* **installment**: As prestações mensais que o beneficiado deve se o empréstimo for financiado.
* **log.annual.inc**: O log natural da receita anual declarada pelo usuário(quem requisitou o empréstimo).
* **annual.inc**: receita anual declarada pelo usuário(quem requisitou o empréstimo).
* **dti**: A razão de débito do beneficiado (total de débito dividido pela receita anual).
* **fico**: A pontuação FICO do beneficiado.
* **days.with.cr.line**: O número de dias que o beneficiado teve sobre a linha de crédito.
* **revol.bal**: O saldo rotativo do beneficiado (o valor não pago do cartão de crédito ao final do ciclo de faturamento).
* **revol.util**: A taxa de utilização da linha rotativa do mutuário (o valor da linha de crédito usado em relação ao crédito total disponível).
* **inq.last.6mths**: O número de consultas do mutuário por credores nos últimos 6 meses.
* **delinq.2yrs**: O número de vezes que o beneficiário ficou sem pagar após 30+ dias do pagamento em 2 anos.
* **pub.rec**: O número de depreciações registradas(pedidos de falência, gravames fiscal, or processos/julgamentos). 
* **not.fully.paid**: 0 se o benficiado pagou todo seu débito, 1 se não foi totalmente pago.
'''

markdown_2 = '''
### Distribuição de beneficiados que pagaram (0) e que não pagaram (1)

Nesse gráfico buscamos visualizar com que taxa temos que os benefiados pelo empréstimos bancário vieram a deixar de pagar suas dívidas. Dessa maneira podemos concluir se o banco em questão obteve lucro sobre seu sistema de empréstimo
'''

markdown_3 = '''
### Scatter do Score FICO com o saldo rotativo devido

Com o plot em questão analisamos a relação entre o score financeiro FICO de cada indivíduo e a sua capacidade de pagar o empréstimo em dia, dessa maneira fazendo uma análise do sistema de empréstimo. Análisando o gráfico percebemos por meio das **regressões Lineares** que quanto menor for o FICO do indivíduo mais ele é propenso a deixar de pagar uma maior quantia da parcela.
'''

markdown_4 = '''
### Scatter plot com curva de tendência do Score FICO com a taxa de juros

Nesse plot buscamos traçar uma relação  entre a taxa de juros imposta pelo banco e o FICO do indivíduo, dessa maneira tentamos entender a política de empréstimo do banco. Analisando o plot concluímos que o FICO é inversamente proporcional aos juros, isso se dá pois o banco tem poucos indícios que um indivíduo com um score FICO baixo terminará de pagar seu empréstimo ou pagará seu empréstimo no tempo correto.
'''

markdown_5 = '''
### Histograma da receita anual dos beneficiados

Com esse histrograma traçamos o perfil financeiro das pessoas que requisitam e adquirem seus empréstimos. O gráfico de violina ajuda na interpretação na densidade dos beneficiados por valor de renda anual.
'''

markdown_6 = '''
### Bar plot para cada propósito

Com esse gráfico temos o propósito de analisar quais dos propósitos de requisição de empréstimo são mais propensos a não conseguirem apagar seus débitos com o banco.
'''

markdown_7 = '''
Gráfico 3D entre taxa de juros, score FICO e crédito usado

Dessa maneira temos a chance de analisar simultaniamente três variáveis da nossa tabela em um único plot.
'''
markdown_8 = '''
---

## Conclusão

<p align="justify">
Ao final do trabalho conseguimos concluir as políticas de empréstimos do banco em que está fortemente atrelado a com o score FICO e o porpósito de requisição de empréstimo do indivíduo. O banco busca priorizar os invíduos com um alto score FICO dando a eles o privilêgio de uma baixa taxa de juros sobre as parcelas do empréstimo e o contrário para aqueles com um baixo FICO.
</p>
<p>
Outro ponto fortemente analisado é o resultado a implementação dessa política de empréstimo do banco a partir da taxa de beneficiados que terminaram de pagar seus empréstimos. Logo no primeiro gráfico podemos perceber que a maioria os indivíduos selecionados para receber empréstimos pagarm integralmente suas dívidas, provando o sucesso do modelo implementado.
<p/>
'''