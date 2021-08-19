import streamlit as st
from data_view import fig1, fig2, loan_df, fig3, fig4, fig5, fig6, fig7, markdown_1
import seaborn as sns
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('DashBoard de análise de empréstimos')
st.write('Esse prejeto consiste na analise de dados relativo à empréstimos no qual tentamos visualizar relações entre features que possuimos')

st.sidebar.title("Configurações")
check_box = st.sidebar.checkbox(label="Mostrar Database")
check_box_col = st.sidebar.checkbox(label="Descrição de colunas")

if check_box:
    st.write(loan_df)

st.markdown("---")
st.markdown("## Descrição")
if check_box_col:
    st.markdown(markdown_1)


st.markdown("---")
st.markdown("## Visualização dos Dados")

st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)
st.plotly_chart(fig4)
st.plotly_chart(fig5)
st.plotly_chart(fig6)
st.plotly_chart(fig7)

# plt.figure(figsize=(10,8))
# sns.histplot(data=loan_df,
#                     x="annual.inc", 
#                     element='step', 
#                     fill=True, 
#                     hue="not.fully.paid")
# plt.xlim([-10000, 0.4e6])
# plt.grid()
# st.pyplot()