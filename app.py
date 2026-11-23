# SAAS PERTAMA LU - KALKULATOR RUMUS ONLINE
# Dibikin dari rumus.py yang tadi!

import streamlit as st
import math

st.set_page_config(page_title="RumusKilat - Kalkulator Rumus", page_icon="⚡")

st.title("⚡ RumusKilat")
st.write("Kalkulator rumus matematika, biar lu gak pusing ngitung manual lagi bro!")

# --- MENU SAMPING ---
menu = st.sidebar.selectbox("Pilih Rumus Bro:", 
    ["Luas Bangun Datar", "Keliling Bangun Datar", "Sigma Bebas (Kasih Nilai Sendiri)", "Volume Bangun Ruang"])

st.sidebar.markdown("---")
st.sidebar.write("**Versi Gratis:** Semua rumus dasar bisa dipake")
st.sidebar.write("**Versi PRO ($2/bln):** Download PDF + Tanpa Iklan + Rumus Lengkap")
if st.sidebar.button("Upgrade ke PRO 🚀"):
    st.sidebar.success("Mantap! Chat gw di WhatsApp buat aktivasi PRO ya bro!")
    st.sidebar.write("Nanti lu bayar manual dulu, gw bukain fiturnya.")

# --- 1. LUAS ---
if menu == "Luas Bangun Datar":
    st.header("📐 Luas Bangun Datar")
    bangun = st.selectbox("Pilih Bangun:", ["Persegi", "Persegi Panjang", "Segitiga", "Lingkaran"])
    
    if bangun == "Persegi":
        s = st.number_input("Masukin Sisi:", min_value=0.0, value=5.0)
        if st.button("Hitung!"):
            st.success(f"Luas Persegi = {s} x {s} = **{s*s}**")
    elif bangun == "Persegi Panjang":
        p = st.number_input("Panjang:", min_value=0.0, value=10.0)
        l = st.number_input("Lebar:", min_value=0.0, value=5.0)
        if st.button("Hitung!"):
            st.success(f"Luas = {p} x {l} = **{p*l}**")
    elif bangun == "Segitiga":
        a = st.number_input("Alas:", min_value=0.0, value=10.0)
        t = st.number_input("Tinggi:", min_value=0.0, value=5.0)
        if st.button("Hitung!"):
            st.success(f"Luas = 1/2 x {a} x {t} = **{0.5*a*t}**")
    elif bangun == "Lingkaran":
        r = st.number_input("Jari-jari:", min_value=0.0, value=7.0)
        if st.button("Hitung!"):
            st.success(f"Luas = 3.14 x {r} x {r} = **{math.pi*r*r:.2f}**")

# --- 2. KELILING ---
elif menu == "Keliling Bangun Datar":
    st.header("📏 Keliling Bangun Datar")
    bangun = st.selectbox("Pilih Bangun:", ["Persegi", "Persegi Panjang", "Lingkaran"])
    if bangun == "Persegi":
        s = st.number_input("Sisi:", min_value=0.0, value=5.0)
        if st.button("Hitung!"):
            st.success(f"Keliling = 4 x {s} = **{4*s}**")
    elif bangun == "Persegi Panjang":
        p = st.number_input("Panjang:", min_value=0.0, value=10.0)
        l = st.number_input("Lebar:", min_value=0.0, value=5.0)
        if st.button("Hitung!"):
            st.success(f"Keliling = 2 x ({p} + {l}) = **{2*(p+l)}**")
    elif bangun == "Lingkaran":
        r = st.number_input("Jari-jari:", min_value=0.0, value=7.0)
        if st.button("Hitung!"):
            st.success(f"Keliling = 2 x 3.14 x {r} = **{2*math.pi*r:.2f}**")

# --- 3. SIGMA BEBAS - INI JAGOAN LU BRO! ---
elif menu == "Sigma Bebas (Kasih Nilai Sendiri)":
    st.header("∑ Sigma Bebas - Lu Yang Kasih Nilai!")
    st.write("Ini yang tadi lu tanya bro! Lu bisa kasih nilai sendiri, gak dipaksa 1 sampe 5.")
    
    teks = st.text_input("Masukin angka lu, pisahin pake koma. Contoh: 2,5,10", "2,5,10")
    mode = st.selectbox("Mau diapain?", ["Totalin Aja (Sigma)", "Sigma Kuadrat (x^2)", "Sigma Kubik (x^3)"])
    
    if st.button("Hitung Sigma!"):
        try:
            angka_list = [float(x.strip()) for x in teks.split(",")]
            if mode == "Totalin Aja (Sigma)":
                hasil = sum(angka_list)
                st.success(f"{' + '.join(map(str, angka_list))} = **{hasil}**")
            elif mode == "Sigma Kuadrat (x^2)":
                hasil = sum([x**2 for x in angka_list])
                st.success(f"Sigma Kuadrat = **{hasil}**")
                st.write(f"Dibuka: {' + '.join([str(x**2) for x in angka_list])}")
            else:
                hasil = sum([x**3 for x in angka_list])
                st.success(f"Sigma Kubik = **{hasil}**")
                st.write(f"Dibuka: {' + '.join([str(x**3) for x in angka_list])}")
        except:
            st.error("Formatnya salah bro! Pastiin pake koma ya, contoh: 2,5,10")

# --- 4. VOLUME ---
elif menu == "Volume Bangun Ruang":
    st.header("🧊 Volume Bangun Ruang")
    bangun = st.selectbox("Pilih Bangun:", ["Kubus", "Balok", "Tabung"])
    if bangun == "Kubus":
        s = st.number_input("Sisi:", min_value=0.0, value=5.0)
        if st.button("Hitung!"):
            st.success(f"Volume Kubus = **{s**3}**")
    elif bangun == "Balok":
        p = st.number_input("Panjang:", min_value=0.0, value=5.0)
        l = st.number_input("Lebar:", min_value=0.0, value=3.0)
        t = st.number_input("Tinggi:", min_value=0.0, value=2.0)
        if st.button("Hitung!"):
            st.success(f"Volume Balok = **{p*l*t}**")
    elif bangun == "Tabung":
        r = st.number_input("Jari-jari:", min_value=0.0, value=7.0)
        t = st.number_input("Tinggi:", min_value=0.0, value=10.0)
        if st.button("Hitung!"):
            st.success(f"Volume Tabung = **{math.pi*r*r*t:.2f}**")

st.markdown("---")
st.write("Dibikin sama lu bro, dari Gorontalo untuk dunia ⚡")