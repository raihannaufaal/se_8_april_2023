#library
import streamlit as st

#write
st.title('software perkalian')
st.subheader('ini adalah aplikasi perkalian')

#input bilangan pertama
number1 = st.number_input('masukkan bil pertama')
st.write(f'bilangan pertama adalah {number1}')

#input bilangan kedua
number2 = st.number_input('masukkan bil kedua')
st.write(f'bilangan kedua adalah {number2}')

#hasil kali
hasil = number1*number2

if st.button('hitung'):
    st.write(f'hasil kali antara {number1} dan {number2} adalah {hasil}')
else:
    st.write('silahkan pencet tombol hitung')