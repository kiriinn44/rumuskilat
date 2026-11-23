import streamlit as st
import math

st.set_page_config(page_title="RumusKilat - Kalkulator Matematika & Konverter Satuan", page_icon="⚡", layout="centered")

# --- HEADER ---
st.title("RumusKilat")
st.markdown("Kalkulator matematika dan konverter satuan. Dilengkapi penjelasan rumus dan langkah perhitungan.")
st.divider()

kategori = st.radio("Kategori", ["Kalkulator Rumus", "Konverter Satuan"], horizontal=True)
st.divider()

# ================= KALKULATOR RUMUS =================
if kategori == "Kalkulator Rumus":
    menu = st.selectbox("Pilih Materi", ["Luas Bangun Datar", "Keliling Bangun Datar", "Volume Bangun Ruang"])

    if menu == "Luas Bangun Datar":
        st.header("Luas Bangun Datar")
        st.write("Luas adalah besar area di dalam sebuah bangun datar. Satuan luas menggunakan pangkat dua, contoh: cm², m².")

        shape = st.selectbox("Pilih Bangun", ["Persegi", "Persegi Panjang", "Segitiga", "Lingkaran"])

        if shape == "Persegi":
            st.subheader("Persegi")
            st.markdown("**Rumus:** Luas = Sisi x Sisi")
            st.markdown("**Penjelasan:** Persegi memiliki 4 sisi yang sama panjang. Luas dihitung dengan mengalikan sisi dengan sisi.")
            s = st.slider("Sisi (cm)", 1, 20, 5)
            st.success(f"Luas = {s} x {s} = {s*s} cm²")
            st.caption("Contoh: Sisi 5 cm, maka luasnya 25 cm².")

        elif shape == "Persegi Panjang":
            st.subheader("Persegi Panjang")
            st.markdown("**Rumus:** Luas = Panjang x Lebar")
            p = st.slider("Panjang (cm)", 1, 20, 10)
            l = st.slider("Lebar (cm)", 1, 20, 5)
            st.success(f"Luas = {p} x {l} = {p*l} cm²")

        elif shape == "Segitiga":
            st.subheader("Segitiga")
            st.markdown("**Rumus:** Luas = 1/2 x Alas x Tinggi")
            st.markdown("**Penjelasan:** Segitiga adalah setengah dari persegi panjang, sehingga hasil perkalian alas dan tinggi dibagi dua.")
            a = st.slider("Alas (cm)", 1, 20, 10)
            t = st.slider("Tinggi (cm)", 1, 20, 5)
            st.success(f"Luas = 1/2 x {a} x {t} = {0.5*a*t} cm²")

        elif shape == "Lingkaran":
            st.subheader("Lingkaran")
            st.markdown("**Rumus:** Luas = π x r x r, dengan π = 3,14")
            st.markdown("**Catatan:** r adalah jari-jari, yaitu jarak dari titik pusat ke tepi lingkaran. Jika diketahui diameter, bagi dua terlebih dahulu untuk mendapatkan r.")
            r = st.slider("Jari-jari / r (cm)", 1, 20, 7)
            st.success(f"Luas = 3,14 x {r} x {r} = {math.pi*r*r:.2f} cm²")

    elif menu == "Keliling Bangun Datar":
        st.header("Keliling Bangun Datar")
        st.write("Keliling adalah total panjang sisi yang mengelilingi sebuah bangun datar. Satuan keliling adalah cm, m, tanpa pangkat.")

        shape = st.selectbox("Pilih Bangun", ["Persegi", "Persegi Panjang", "Lingkaran"])

        if shape == "Persegi":
            st.subheader("Persegi")
            st.markdown("**Rumus:** Keliling = 4 x Sisi")
            s = st.slider("Sisi (cm)", 1, 20, 5)
            st.success(f"Keliling = 4 x {s} = {4*s} cm")

        elif shape == "Persegi Panjang":
            st.subheader("Persegi Panjang")
            st.markdown("**Rumus:** Keliling = 2 x (Panjang + Lebar)")
            p = st.slider("Panjang (cm)", 1, 20, 10)
            l = st.slider("Lebar (cm)", 1, 20, 5)
            st.success(f"Keliling = 2 x ({p} + {l}) = {2*(p+l)} cm")

        elif shape == "Lingkaran":
            st.subheader("Lingkaran")
            st.markdown("**Rumus:** Keliling = 2 x π x r")
            r = st.slider("Jari-jari / r (cm)", 1, 20, 7)
            st.success(f"Keliling = 2 x 3,14 x {r} = {2*math.pi*r:.2f} cm")

    elif menu == "Volume Bangun Ruang":
        st.header("Volume Bangun Ruang")
        st.write("Volume adalah kapasitas yang dapat ditampung oleh sebuah bangun ruang. Satuan volume menggunakan pangkat tiga, contoh: cm³, m³.")

        shape = st.selectbox("Pilih Bangun", ["Kubus", "Balok", "Tabung"])

        if shape == "Kubus":
            st.subheader("Kubus")
            st.markdown("**Rumus:** Volume = Sisi x Sisi x Sisi")
            s = st.slider("Sisi (cm)", 1, 20, 5)
            st.success(f"Volume = {s} x {s} x {s} = {s**3} cm³")

        elif shape == "Balok":
            st.subheader("Balok")
            st.markdown("**Rumus:** Volume = Panjang x Lebar x Tinggi")
            p = st.slider("Panjang (cm)", 1, 20, 5)
            l = st.slider("Lebar (cm)", 1, 20, 3)
            t = st.slider("Tinggi (cm)", 1, 20, 2)
            st.success(f"Volume = {p} x {l} x {t} = {p*l*t} cm³")

        elif shape == "Tabung":
            st.subheader("Tabung")
            st.markdown("**Rumus:** Volume = π x r² x Tinggi")
            st.markdown("**Penjelasan:** Volume tabung dihitung dari luas alas lingkaran dikalikan tinggi.")
            r = st.slider("Jari-jari / r (cm)", 1, 20, 7)
            t = st.slider("Tinggi (cm)", 1, 20, 10)
            st.success(f"Volume = 3,14 x {r}² x {t} = {math.pi*r*r*t:.2f} cm³")

# ================= KONVERTER SATUAN =================
elif kategori == "Konverter Satuan":
    st.header("Konverter Satuan")
    st.write("Konversi satuan panjang dan massa dengan cepat dan akurat.")

    menu_k = st.selectbox("Pilih Konverter", ["Satuan Panjang", "Satuan Massa / Berat"])

    if menu_k == "Satuan Panjang":
        st.subheader("Satuan Panjang")
        st.markdown("Urutan satuan: **km - hm - dam - m - dm - cm - mm**")
        st.markdown("Setiap turun satu tangga dikali 10. Setiap naik satu tangga dibagi 10.")
        nilai = st.number_input("Nilai", min_value=0.0, value=1.0)
        dari = st.selectbox("Dari", ["Kilometer (km)", "Meter (m)", "Centimeter (cm)", "Millimeter (mm)"])
        ke = st.selectbox("Ke", ["Kilometer (km)", "Meter (m)", "Centimeter (cm)", "Millimeter (mm)"])
        faktor = {"Kilometer (km)": 1000, "Meter (m)": 1, "Centimeter (cm)": 0.01, "Millimeter (mm)": 0.001}
        if st.button("Konversi"):
            hasil = nilai * faktor[dari] / faktor[ke]
            st.success(f"{nilai} {dari} = {hasil} {ke}")

    elif menu_k == "Satuan Massa / Berat":
        st.subheader("Satuan Massa / Berat")
        st.markdown("Urutan satuan: **kg - hg - dag - g - dg - cg - mg**")
        st.markdown("Konversi tambahan: 1 Ton = 1.000 kg. 1 Kwintal = 100 kg.")
        nilai = st.number_input("Nilai", min_value=0.0, value=1.0)
        dari = st.selectbox("Dari", ["Ton", "Kwintal", "Kilogram (kg)", "Gram (g)"])
        ke = st.selectbox("Ke", ["Ton", "Kwintal", "Kilogram (kg)", "Gram (g)"])
        faktor_g = {"Ton": 1000000, "Kwintal": 100000, "Kilogram (kg)": 1000, "Gram (g)": 1}
        if st.button("Konversi Massa"):
            hasil = nilai * faktor_g[dari] / faktor_g[ke]
            st.success(f"{nilai} {dari} = {hasil} {ke}")

st.divider()
st.caption("© 2026 RumusKilat. Kalkulator Matematika & Konverter Satuan.")