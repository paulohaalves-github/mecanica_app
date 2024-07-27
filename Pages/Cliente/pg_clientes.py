import streamlit as st 

st.title('Clientes')



cliente = st.selectbox('Cliente',['','Zezinho', 'Pedrinho'], label_visibility ="collapsed",  placeholder='Selecione o cliente')

# Ao selecionar o cliente, exibir o respectivo carro.

carro1 = {
    'id_carro' : 1,
    'Modelo': 'Spacefox 1.6',
    'Placa': 'ZAS-3212',
    'Cor': 'Prata',
    'Ano': 2010,
    'km':  16000
}

carro2 = {
    'id_carro' : 2,
    'Modelo': 'Gol',
    'Placa': 'SHD-2341',
    'Cor': 'Preto',
    'Ano': 2015,
    'km':  223000
}

if cliente == "Zezinho":
    carros=[]
    carros.append(carro1)
    carros.append(carro2)
    
    carList = []
    for i in carros:
        carList.append(i['Modelo'])

    car = st.selectbox('Carro', carList)
    if car :
        for i in carros:
            if i['Modelo'] != car:             
                continue
            else:
                st.table(i)       