# cabang/aritmatika.py - Cabang 1: Aritmatika
import streamlit as st
from utils import cek_bagi_nol, format_angka

# --- FUNGSI RUMUS MURNI, TIDAK ADA STREAMLIT DI SINI ---
# Ini biar bisa dites tanpa buka web
def tambah(a, b): return a + b
def kurang(a, b): return a - b
def kali(a, b): return a * b
def bagi(a, b):
    if cek_bagi_nol(b):
        return None
    return a / b
def sisa_bagi(a, b):
    if cek_bagi_nol(b):
        return None
    return a % b
def pangkat(a, b):
    if abs(b) > 100:
        return None
    return a ** b

# DICT DALAM FILE CABANG - Kunci = nama operasi, Nilai = fungsinya
OPERASI = {
    "Tambah (+)": (tambah, "+"),
    "Kurang (-)": (kurang, "-"),
    "Kali (×)": (kali, "×"),
    "Bagi (÷)": (bagi, "÷"),
    "Sisa Bagi (%)": (sisa_bagi, "%"),
    "Pangkat (^)": (pangkat, "^"),
}

def tampilkan():
    st.header("1. Aritmatika - Hitung Dasar")
    st.write("Tambah, Kurang, Kali, Bagi. Pondasi semua matematika.")

    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Angka Pertama", value=0.0, format="%.4f", key="arit_a")
    with col2:
        b = st.number_input("Angka Kedua", value=0.0, format="%.4f", key="arit_b")

    pilihan = st.selectbox("Pilih Operasi", list(OPERASI.keys()))

    if st.button("Hitung", type="primary", key="btn_arit"):
        fungsi, simbol = OPERASI[pilihan]
        hasil = fungsi(a, b)

        # Cek aman: kalau hasil None, berarti error (bagi nol / pangkat kebesaran)
        if hasil is None:
            if pilihan in ["Bagi (÷)", "Sisa Bagi (%)"]:
                st.error("⛔ Tidak bisa dibagi 0. Dalam matematika, pembagian dengan 0 tidak terdefinisi.")
            else:
                st.error("⛔ Pangkat terlalu besar (maksimal 100) untuk keamanan.")
            st.stop()

        st.success(f"Hasil: **{format_angka(a)} {simbol} {format_angka(b)} = {format_angka(hasil)}**")
        with st.expander("Lihat Cara Hitung"):
            st.write(f"Rumus: {format_angka(a)} {simbol} {format_angka(b)}")
            st.write(f"Hasil akhir: **{format_angka(hasil)}**")

    st.divider()
    st.subheader("Contoh Situbondo")
    st.write("""
    - **Tambah:** 2 kg + 3 kg = 5 kg beras
    - **Kurang:** 100.000 - 50.000 = 50.000 sisa uang
    - **Kali:** 3 kg × 14.000 = 42.000
    - **Bagi:** 150 km ÷ 50 km/jam = 3 jam ke Surabaya
    """)