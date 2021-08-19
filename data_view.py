from matplotlib.pyplot import xlabel, ylabel
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import numpy as np
import seaborn as sns

loan_df = pd.read_csv('loan_data.csv')

loan_df['annual.inc'] = np.exp(loan_df['log.annual.inc'])

fig1 = px.histogram(loan_df, x="not.fully.paid")
fig1.update_layout(bargap=0.2)

loan_df["not.fully.paid"] = loan_df["not.fully.paid"].astype(str)
fig2 = px.scatter(loan_df, x="fico",
                  y="revol.util",
                  color="not.fully.paid",
                  trendline="ols",
                  title="Taxa de alguma coisa em relação a outra")

fig3 = px.scatter(loan_df,
                  x="fico", 
                  y="int.rate",
                  color="not.fully.paid",
                  trendline='ols',
                  title="Taxa de alguma coisa em relação a outra")

fig4 = px.histogram(loan_df, x="annual.inc", color="not.fully.paid",
                    marginal="violin", # or violin, rug
                    hover_data=loan_df.columns,
                    title='Histograma e Violin plot do Annual Income em relação a not.fully.paid')

fig5 = px.histogram(loan_df, x="installment", color="not.fully.paid",
                    marginal="violin", # or violin, rug
                    hover_data=loan_df.columns,
                    title='Histograma e Violin plot do Installment em relação a not.fully.paid')

fig6 = px.scatter_3d(loan_df, x='int.rate', y='revol.util', z='fico',
                     color='not.fully.paid', 
                     labels={'int.rate':'Interest Rate', 'revol.util': '% Usada de crédito', 'days.with.cr.line': 'FICO Score'})


markdown_1 = '''
---
## Columns Info
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

