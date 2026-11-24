import streamlit as st
from cabang.aritmatika import tampilkan_aritmatika
from cabang.konverter import tampilkan_konverter

st.sidebar.title("RumusKilat ⚡")
menu = st.sidebar.selectbox("Pilih Cabang:", ["1. Aritmatika", "2. Geometri", "3. Konverter"])

if menu == "1. Aritmatika":
    tampilkan_aritmatika()
elif menu == "3. Konverter":
    tampilkan_konverter()
else:
    st.title("🚧 Masih Dibangun")
    st.write("Geometri lagi dibikin, sabar ya bro.")