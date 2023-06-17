import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

gsheets_url = 'https://docs.google.com/spreadsheets/d/10aXM_qpAAha6ErA9kJ8yp3o33ixROsqrZf8sG7cOdsE/export?format=csv&gid=1007270255' 

data = pd.read_csv(gsheets_url, on_bad_lines='skip')

st.dataframe(data)

st.title("As 05 empresas editoras (publishers) mais populares!")
fig, ax = plt.subplots()
ax = sns.barplot(x="Publisher", y="Global_Sales", data=data.groupby(['Publisher']).sum().sort_values('Global_Sales', ascending=False).iloc[:5].reset_index())
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set(xlabel='Editoras', ylabel='Vendas Globais (em milhões)')
st.pyplot(fig)

st.title("As 10 plataformas mais populares!")
fig, ax = plt.subplots()
ax = sns.barplot(x="Platform", y="Global_Sales", data=data.groupby(['Platform']).sum().sort_values('Global_Sales', ascending=False).iloc[:10].reset_index())
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set(xlabel='Plataformas', ylabel='Vendas Globais (em milhões)')
st.pyplot(fig)


st.title("TOP 20 jogos mais populares!")
st.write("Selecione a região:")
region = st.selectbox("", ["América do Norte", "União Europeia", "Japão", "Resto do mundo", "Global"])
if region == "América do Norte":
    data.sort_values('NA_Sales',ascending=False)[:20][['Name','NA_Sales']]
elif region == "União Europeia":
    data.sort_values('EU_Sales',ascending=False)[:20][['Name','EU_Sales']]
elif region == "Japão":
    data.sort_values('JP_Sales',ascending=False)[:20][['Name','JP_Sales']]
elif region == "Resto do mundo":
    data.sort_values('Other_Sales',ascending=False)[:20][['Name','Other_Sales']]
else:
    data.sort_values('Global_Sales',ascending=False)[:20][['Name','Global_Sales']]


st.title("Total de vendas por região")
st.write("Selecione o jogo:")
game = st.selectbox("", data['Name'].unique())
data[data['Name'] == game][['Name','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']].set_index('Name').T.plot(kind='bar', figsize=(10,5))
st.pyplot()


st.title("Top 05 gêneros de cada mercado")
st.write("Selecione o mercado:")
region02 = st.selectbox("", ["América do Norte", "União Europeia", "Japão", "Resto do mundo", "Global "])
if region02 == "América do Norte":
    data.groupby(['Genre']).sum().sort_values('NA_Sales', ascending=False).iloc[:5].reset_index()[['Genre','NA_Sales', 'Name']]
elif region02 == "União Europeia":
    data.groupby(['Genre']).sum().sort_values('EU_Sales', ascending=False).iloc[:5].reset_index()[['Genre','EU_Sales', 'Name']]
elif region02 == "Japão":
    data.groupby(['Genre']).sum().sort_values('JP_Sales', ascending=False).iloc[:5].reset_index()[['Genre','JP_Sales', 'Name']]
elif region02 == "Resto do mundo":
    data.groupby(['Genre']).sum().sort_values('Other_Sales', ascending=False).iloc[:5].reset_index()[['Genre','Other_Sales', 'Name']]
else:
    data.groupby(['Genre']).sum().sort_values('Global_Sales', ascending=False).iloc[:5].reset_index()[['Genre','Global_Sales', 'Name']]

st.title("Quantidade de jogos lançados por ano")
st.write("Selecione o ano:")
year = st.selectbox("", data['Year'].unique())
st.write("Quantidade de jogos lançados nesse ano")
st.write(data[data['Year'] == year].shape[0])
st.write("Jogo Mais Vendido")
st.write(data[data['Year'] == year]["Name"].iloc[0])


st.title("Curiosidades sobre o jogo quantidade de vendas globais em relação aos jogos mais vendidos naquele ano")
st.write("Selecione o jogo:")
game02 = st.selectbox(" ", data['Name'].unique())
year = data[data['Name'] == game02]["Year"].iloc[0]
fig, ax = plt.subplots()
ax = sns.countplot(x="Name", hue="Global_Sales", data=data[data["Year"] == year].iloc[:5].reset_index())
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set(xlabel='Jogos', ylabel='Vendas Globais (em milhões)')

st.pyplot(fig)