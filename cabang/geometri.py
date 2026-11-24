import streamlit as st
import math

def tampilkan_geometri():
    st.title("📐 Geometri")
    st.write("Hitung luas dan keliling. Biar gampang, pakai contoh Situbondo saja.")

    bangun = st.selectbox("Pilih Bangun:", [
        "Persegi",
        "Persegi Panjang",
        "Segitiga",
        "Lingkaran"
    ])

    # 1. PERSEGI
    if bangun == "Persegi":
        st.subheader("⬛ Persegi")
        sisi = st.number_input("Sisi (meter):", value=5.0)
        luas = sisi * sisi
        keliling = 4 * sisi
        st.success(f"Luas: {luas} m² | Keliling: {keliling} m")
        st.info("Contoh: Tanah di Panji ukurannya 5m x 5m, luasnya 25 m².")

    # 2. PERSEGI PANJANG
    elif bangun == "Persegi Panjang":
        st.subheader("▭ Persegi Panjang")
        p = st.number_input("Panjang (meter):", value=10.0)
        l = st.number_input("Lebar (meter):", value=5.0)
        luas = p * l
        keliling = 2 * (p + l)
        st.success(f"Luas: {luas} m² | Keliling: {keliling} m")
        st.info("Contoh: Lapangan Pasar Situbondo 10m x 5m, luasnya 50 m².")

    # 3. SEGITIGA
    elif bangun == "Segitiga":
        st.subheader("🔺 Segitiga")
        alas = st.number_input("Alas (meter):", value=6.0)
        tinggi = st.number_input("Tinggi (meter):", value=4.0)
        luas = 0.5 * alas * tinggi
        st.success(f"Luas: {luas} m²")
        st.info("Contoh: Atap warung di Pantai Pasir Putih bentuk segitiga, alas 6m tinggi 4m, luas 12 m².")

    # 4. LINGKARAN
    elif bangun == "Lingkaran":
        st.subheader("⚪ Lingkaran")
        r = st.number_input("Jari-jari (meter):", value=7.0)
        luas = math.pi * r * r
        keliling = 2 * math.pi * r
        st.success(f"Luas: {luas:.2f} m² | Keliling: {keliling:.2f} m")
        st.info("Contoh: Kolam ikan di Besuki jari-jari 7m, luasnya 153.94 m².")