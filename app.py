# app.py - File Utama, hanya untuk menu
import streamlit as st
from kalkulator_rumus import tampilkan_kalkulator
from konverter import tampilkan_konverter

st.set_page_config(page_title="RumusKilat - Kalkulator Matematika & Konverter Satuan", page_icon="⚡", layout="centered")

st.title("RumusKilat")
st.markdown("Kalkulator matematika dan konverter satuan. Dilengkapi penjelasan rumus dan langkah perhitungan.")
st.divider()

kategori = st.radio("Kategori", ["Kalkulator Rumus", "Konverter Satuan"], horizontal=True)
st.divider()

if kategori == "Kalkulator Rumus":
    tampilkan_kalkulator()
elif kategori == "Konverter Satuan":
    tampilkan_konverter()

st.divider()
st.caption("© 2026 RumusKilat. Kalkulator Matematika & Konverter Satuan.")