import streamlit as st

st.title('aplikasi perhitungan molaritas')

bobot = st.number_input('masukan nilai bobot')
volume = st.number_input('masukan nilai volume')
mr = st.number_input('masukan nilai mr')

tombol = st.button('hiting nilai molaritas')

if tombol:
    nilai_molaritas = bobot/(mr*volume)
    st.success(f'Nilai molaritas adalah {nilai_molaritas}')