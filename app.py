import streamlit as st
from cabang.aritmatika import tampilkan_aritmatika
from cabang.geometri import tampilkan_geometri
from perkakas.konverter import tampilkan_konverter
from perkakas.konverter_uang import tampilkan_konverter_uang
from perkakas.kalkulator_diskon import tampilkan_kalkulator_diskon
from perkakas.hitung_nilai import tampilkan_hitung_nilai

# ===== MENU 1: RUMUSKILAT - CABANG MATEMATIKA =====
st.sidebar.title("RumusKilat ⚡")
st.sidebar.write("Belajar Matematika")

menu_rumus = st.sidebar.selectbox("Pilih Cabang Matematika:", [
    "-- Pilih --",
    "1. Aritmatika",
    "2. Geometri"
])

st.sidebar.markdown("---") # Garis pemisah

# ===== MENU 2: PERKAKAS - DI BAWAHNYA, JUDUL BARU =====
st.sidebar.title("Perkakas 🧰")
st.sidebar.write("Alat Bantu Harian")

menu_perkakas = st.sidebar.selectbox("Pilih Perkakas:", [
    "-- Pilih --",
    "1. Konverter Satuan",
    "2. Konverter Uang",
    "3. Kalkulator Diskon",
    "4. Hitung Nilai"
])

# ===== LOGIKA: Mana yang dipilih, itu yang tampil =====
# Kalau Perkakas dipilih, tampilkan Perkakas. Kalau tidak, tampilkan Rumus.

if menu_perkakas == "1. Konverter Satuan":
    tampilkan_konverter()
elif menu_perkakas == "2. Konverter Uang":
    tampilkan_konverter_uang()
elif menu_perkakas == "3. Kalkulator Diskon":
    tampilkan_kalkulator_diskon()
elif menu_perkakas == "4. Hitung Nilai":
    tampilkan_hitung_nilai()

elif menu_rumus == "1. Aritmatika":
    tampilkan_aritmatika()
elif menu_rumus == "2. Geometri":
    tampilkan_geometri()

else:
    # Kalau dua-duanya masih "-- Pilih --", tampilkan halaman depan
    st.title("Selamat Datang di RumusKilat ⚡")
    st.write("Pilih di kiri bro:")
    st.write("**Atas** -> Mau belajar Matematika")
    st.write("**Bawah** -> Mau pakai Perkakas harian")
    st.info("Contoh: Mau hitung diskon baju di Pasar Situbondo? Pilih Perkakas di bawah.")