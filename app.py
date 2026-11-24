import streamlit as st
from cabang.aritmatika import tampilkan_aritmatika
from cabang.geometri import tampilkan_geometri
from perkakas.konverter import tampilkan_konverter

st.sidebar.title("RumusKilat ⚡")
menu = st.sidebar.selectbox("Pilih Menu:", [
    "1. Aritmatika",
    "2. Geometri",
    "3. Konverter"
])

if menu == "1. Aritmatika":
    tampilkan_aritmatika()
elif menu == "2. Geometri":
    tampilkan_geometri()
elif menu == "3. Konverter":
    tampilkan_konverter()