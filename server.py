import streamlit as st
from data_view import fig1, fig2, loan_df, fig3, fig4
import seaborn as sns
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('DashBoard de análise de empréstimos')
st.write('Esse prejeto consiste na analise de dados relativo à empréstimos no qual tentamos visualizar relações entre features que possuimos')

st.sidebar.title("Configuração")
check_box = st.sidebar.checkbox(label="mostrar database")

if check_box:
    st.write(loan_df)

st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)
st.plotly_chart(fig4)

plt.figure(figsize=(10,8))
sns.histplot(data=loan_df,
                    x="annual.inc", 
                    element='step', 
                    fill=True, 
                    hue="not.fully.paid")
plt.xlim([-10000, 0.4e6])
plt.grid()
st.pyplot()