# kalkulator_rumus.py - Khusus untuk semua rumus matematika
import streamlit as st
import math

def tampilkan_kalkulator():
    menu = st.selectbox("Pilih Materi", ["Luas Bangun Datar", "Keliling Bangun Datar", "Volume Bangun Ruang"])

    # ---------- LUAS ----------
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

    # ---------- KELILING ----------
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

    # ---------- VOLUME ----------
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