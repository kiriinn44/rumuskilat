# konverter.py - Khusus untuk semua konverter satuan
import streamlit as st

def tampilkan_konverter():
    st.header("Konverter Satuan")
    st.write("Konversi satuan panjang dan massa dengan cepat dan akurat.")

    menu_k = st.selectbox("Pilih Konverter", ["Satuan Panjang", "Satuan Massa / Berat"])

    if menu_k == "Satuan Panjang":
        st.subheader("Satuan Panjang")
        st.markdown("Urutan satuan metrik: **km - hm - dam - m - dm - cm - mm**")
        st.markdown("Setiap turun satu tangga dikali 10. Setiap naik satu tangga dibagi 10.")

        nilai = st.number_input("Nilai", min_value=0.0, value=1.0, key="panjang_nilai")
        dari = st.selectbox("Dari", ["Kilometer (km)", "Hektometer (hm)", "Dekameter (dam)", "Meter (m)", "Desimeter (dm)", "Centimeter (cm)", "Milimeter (mm)", "Inci / Inch (in)", "Kaki / Feet (ft)", "Yard (yd)", "Mil / Mile (mi)"], key="panjang_dari")
        ke = st.selectbox("Ke", ["Kilometer (km)", "Hektometer (hm)", "Dekameter (dam)", "Meter (m)", "Desimeter (dm)", "Centimeter (cm)", "Milimeter (mm)", "Inci / Inch (in)", "Kaki / Feet (ft)", "Yard (yd)", "Mil / Mile (mi)"], key="panjang_ke")

        faktor_ke_meter = {
            "Kilometer (km)": 1000,
            "Hektometer (hm)": 100,
            "Dekameter (dam)": 10,
            "Meter (m)": 1,
            "Desimeter (dm)": 0.1,
            "Centimeter (cm)": 0.01,
            "Milimeter (mm)": 0.001,
            "Inci / Inch (in)": 0.0254,
            "Kaki / Feet (ft)": 0.3048,
            "Yard (yd)": 0.9144,
            "Mil / Mile (mi)": 1609.34
        }
        if st.button("Konversi", key="btn_panjang"):
            hasil = nilai * faktor_ke_meter[dari] / faktor_ke_meter[ke]
            st.success(f"{nilai} {dari} = {hasil} {ke}")

    elif menu_k == "Satuan Massa / Berat":
        st.subheader("Satuan Massa / Berat")
        st.markdown("Urutan satuan metrik: **kg - hg - dag - g - dg - cg - mg**")
        st.markdown("Konversi tambahan: 1 Ton = 1.000 kg. 1 Kwintal = 100 kg. 1 Ons = 100 g.")

        nilai = st.number_input("Nilai", min_value=0.0, value=1.0, key="berat_nilai")
        dari = st.selectbox("Dari", ["Ton", "Kwintal", "Kilogram (kg)", "Hektogram / Ons (hg)", "Dekagram (dag)", "Gram (g)", "Desigram (dg)", "Centigram (cg)", "Miligram (mg)", "Pon / Pound (lb)", "Ounce (oz)"], key="berat_dari")
        ke = st.selectbox("Ke", ["Ton", "Kwintal", "Kilogram (kg)", "Hektogram / Ons (hg)", "Dekagram (dag)", "Gram (g)", "Desigram (dg)", "Centigram (cg)", "Miligram (mg)", "Pon / Pound (lb)", "Ounce (oz)"], key="berat_ke")

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
            "Pon / Pound (lb)": 453.592,
            "Ounce (oz)": 28.3495
        }
        if st.button("Konversi Massa", key="btn_berat"):
            hasil = nilai * faktor_ke_gram[dari] / faktor_ke_gram[ke]
            st.success(f"{nilai} {dari} = {hasil} {ke}")