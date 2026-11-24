# konverter.py - Khusus untuk semua konverter satuan - VERSI LENGKAP
import streamlit as st

def tampilkan_konverter():
    st.header("Konverter Satuan")
    st.write("Konversi satuan panjang, massa, suhu, dan waktu dengan cepat dan akurat.")

    menu_k = st.selectbox("Pilih Konverter", ["Satuan Panjang", "Satuan Massa / Berat", "Satuan Suhu", "Satuan Waktu"])

    # ================= 1. PANJANG =================
    if menu_k == "Satuan Panjang":
        st.subheader("Satuan Panjang")
        st.markdown("Urutan satuan metrik: **km - hm - dam - m - dm - cm - mm**")
        st.markdown("Setiap turun satu tangga dikali 10. Setiap naik satu tangga dibagi 10.")

        nilai = st.number_input("Nilai", min_value=0.0, value=1.0, key="panjang_nilai")
        dari = st.selectbox("Dari", ["Kilometer (km)", "Hektometer (hm)", "Dekameter (dam)", "Meter (m)", "Desimeter (dm)", "Centimeter (cm)", "Milimeter (mm)", "Mikrometer (µm)", "Nanometer (nm)", "Inci / Inch (in)", "Kaki / Feet (ft)", "Yard (yd)", "Mil / Mile (mi)", "Mil Laut / Nautical Mile"], key="panjang_dari")
        ke = st.selectbox("Ke", ["Kilometer (km)", "Hektometer (hm)", "Dekameter (dam)", "Meter (m)", "Desimeter (dm)", "Centimeter (cm)", "Milimeter (mm)", "Mikrometer (µm)", "Nanometer (nm)", "Inci / Inch (in)", "Kaki / Feet (ft)", "Yard (yd)", "Mil / Mile (mi)", "Mil Laut / Nautical Mile"], key="panjang_ke")

        faktor_ke_meter = {
            "Kilometer (km)": 1000,
            "Hektometer (hm)": 100,
            "Dekameter (dam)": 10,
            "Meter (m)": 1,
            "Desimeter (dm)": 0.1,
            "Centimeter (cm)": 0.01,
            "Milimeter (mm)": 0.001,
            "Mikrometer (µm)": 0.000001,
            "Nanometer (nm)": 0.000000001,
            "Inci / Inch (in)": 0.0254,
            "Kaki / Feet (ft)": 0.3048,
            "Yard (yd)": 0.9144,
            "Mil / Mile (mi)": 1609.34,
            "Mil Laut / Nautical Mile": 1852
        }
        if st.button("Konversi", key="btn_panjang"):
            hasil = nilai * faktor_ke_meter[dari] / faktor_ke_meter[ke]
            st.success(f"{nilai} {dari} = {hasil} {ke}")
            st.caption(f"Penjelasan: {nilai} {dari} diubah dulu ke meter, lalu diubah ke {ke}.")

    # ================= 2. MASSA / BERAT =================
    elif menu_k == "Satuan Massa / Berat":
        st.subheader("Satuan Massa / Berat")
        st.markdown("Urutan satuan metrik: **kg - hg - dag - g - dg - cg - mg**")
        st.markdown("Konversi tambahan: 1 Ton = 1.000 kg. 1 Kwintal = 100 kg. 1 Ons = 100 g.")

        nilai = st.number_input("Nilai", min_value=0.0, value=1.0, key="berat_nilai")
        dari = st.selectbox("Dari", ["Ton", "Kwintal", "Kilogram (kg)", "Hektogram / Ons (hg)", "Dekagram (dag)", "Gram (g)", "Desigram (dg)", "Centigram (cg)", "Miligram (mg)", "Mikrogram (µg)", "Pon / Pound (lb)", "Ounce (oz)", "Karats"], key="berat_dari")
        ke = st.selectbox("Ke", ["Ton", "Kwintal", "Kilogram (kg)", "Hektogram / Ons (hg)", "Dekagram (dag)", "Gram (g)", "Desigram (dg)", "Centigram (cg)", "Miligram (mg)", "Mikrogram (µg)", "Pon / Pound (lb)", "Ounce (oz)", "Karats"], key="berat_ke")

        faktor_ke_gram = {
            "Ton": 1000000,
            "Kwintal": 100000,
            "Kilogram (kg)": 1000,
            "Hektogram / Ons (hg)": 100,
            "Dekagram (dag)": 10,
            "Gram (g)": 1,
            "Desigram (dg)": 0.1,
            "Centigram (cg)": 0.01,
            "Miligram (mg)": 0.001,
            "Mikrogram (µg)": 0.000001,
            "Pon / Pound (lb)": 453.592,
            "Ounce (oz)": 28.3495,
            "Karats": 0.2
        }
        if st.button("Konversi Massa", key="btn_berat"):
            hasil = nilai * faktor_ke_gram[dari] / faktor_ke_gram[ke]
            st.success(f"{nilai} {dari} = {hasil} {ke}")

    # ================= 3. SUHU =================
    elif menu_k == "Satuan Suhu":
        st.subheader("Satuan Suhu")
        st.markdown("Satuan suhu yang umum digunakan: **Celcius (°C), Fahrenheit (°F), Reamur (°R), Kelvin (K)**")
        st.markdown("**Rumus patokan:** Semua suhu diubah dulu ke Celcius, lalu diubah ke tujuan.")
        st.markdown("- Celcius ke Fahrenheit: (°C x 9/5) + 32")
        st.markdown("- Celcius ke Reamur: °C x 4/5")
        st.markdown("- Celcius ke Kelvin: °C + 273,15")

        nilai = st.number_input("Nilai Suhu", value=0.0, key="suhu_nilai")
        dari = st.selectbox("Dari", ["Celcius (°C)", "Fahrenheit (°F)", "Reamur (°R)", "Kelvin (K)"], key="suhu_dari")
        ke = st.selectbox("Ke", ["Celcius (°C)", "Fahrenheit (°F)", "Reamur (°R)", "Kelvin (K)"], key="suhu_ke")

        def ke_celcius(n, satuan):
            if satuan == "Celcius (°C)":
                return n
            elif satuan == "Fahrenheit (°F)":
                return (n - 32) * 5/9
            elif satuan == "Reamur (°R)":
                return n * 5/4
            elif satuan == "Kelvin (K)":
                return n - 273.15

        def dari_celcius(n, satuan):
            if satuan == "Celcius (°C)":
                return n
            elif satuan == "Fahrenheit (°F)":
                return (n * 9/5) + 32
            elif satuan == "Reamur (°R)":
                return n * 4/5
            elif satuan == "Kelvin (K)":
                return n + 273.15

        if st.button("Konversi Suhu", key="btn_suhu"):
            celcius = ke_celcius(nilai, dari)
            hasil = dari_celcius(celcius, ke)
            st.success(f"{nilai} {dari} = {hasil:.2f} {ke}")
            if ke == "Kelvin (K)" and hasil < 0:
                st.warning("Perhatian: Suhu Kelvin tidak bisa di bawah 0 K (nol mutlak).")

    # ================= 4. WAKTU =================
    elif menu_k == "Satuan Waktu":
        st.subheader("Satuan Waktu")
        st.markdown("Urutan satuan waktu: **1 Hari = 24 Jam, 1 Jam = 60 Menit, 1 Menit = 60 Detik**")
        st.markdown("Untuk Bulan dan Tahun, digunakan patokan: 1 Bulan = 30 Hari, 1 Tahun = 365 Hari.")

        nilai = st.number_input("Nilai", min_value=0.0, value=1.0, key="waktu_nilai")
        dari = st.selectbox("Dari", ["Milidetik (ms)", "Detik (s)", "Menit (m)", "Jam (h)", "Hari", "Minggu", "Bulan", "Tahun"], key="waktu_dari")
        ke = st.selectbox("Ke", ["Milidetik (ms)", "Detik (s)", "Menit (m)", "Jam (h)", "Hari", "Minggu", "Bulan", "Tahun"], key="waktu_ke")

        faktor_ke_detik = {
            "Milidetik (ms)": 0.001,
            "Detik (s)": 1,
            "Menit (m)": 60,
            "Jam (h)": 3600,
            "Hari": 86400,
            "Minggu": 604800,
            "Bulan": 2592000,
            "Tahun": 31536000
        }
        if st.button("Konversi Waktu", key="btn_waktu"):
            hasil = nilai * faktor_ke_detik[dari] / faktor_ke_detik[ke]
            st.success(f"{nilai} {dari} = {hasil} {ke}")