import streamlit as st 

def home():
    st.title('Mecânica')


pg = st.navigation([
    st.Page(home, title="Home", icon="🌐"),
    st.Page(".\Pages\Cliente\pg_clientes.py", title="Clientes", icon="🚹"),
    st.Page(".\Pages\pg_manutencao.py", title="Manutenções", icon="👨‍🔧"),
])

pg.run()