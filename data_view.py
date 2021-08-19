import plotly.express as px
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

