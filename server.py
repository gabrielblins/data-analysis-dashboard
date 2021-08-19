import streamlit as st
from data_view import fig1, fig2, loan_df, fig3, fig4, fig5, fig6, fig7, markdown_1, markdown_2, markdown_3, markdown_4, markdown_5, markdown_6
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
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

st.markdown(markdown_2)
st.plotly_chart(fig1, use_container_width=True)
st.markdown(markdown_3)
st.plotly_chart(fig2, use_container_width=True)
st.markdown(markdown_4)
st.plotly_chart(fig3, use_container_width=True)
st.markdown(markdown_5)
st.plotly_chart(fig4, use_container_width=True)
st.plotly_chart(fig5, use_container_width=True)
st.plotly_chart(fig6, use_container_width=True)
st.markdown(markdown_6)
st.plotly_chart(fig7, use_container_width=True)

# plt.figure(figsize=(10,8))
# sns.histplot(data=loan_df,
#                     x="annual.inc", 
#                     element='step', 
#                     fill=True, 
#                     hue="not.fully.paid")
# plt.xlim([-10000, 0.4e6])
# plt.grid()
# st.pyplot()