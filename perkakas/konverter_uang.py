import streamlit as st
import requests

def get_kurs(dari, ke):
    # Coba 1: Frankfurter (ECB - paling akurat)
    try:
        r = requests.get(f"https://api.frankfurter.app/latest?from={dari}&to={ke}", timeout=5)
        data = r.json()
        return data['rates'][ke], f"Live - Frankfurter / ECB - Tanggal: {data['date']}"
    except:
        pass

    # Coba 2: ExchangeRate-API (cadangan)
    try:
        r = requests.get(f"https://open.er-api.com/v6/latest/{dari}", timeout=5)
        data = r.json()
        return data['rates'][ke], f"Live - ExchangeRate-API - Update: {data['time_last_update_utc']}"
    except:
        return None, "Gagal"

def tampilkan_konverter_uang():
    st.title("💱 Konverter Uang - Kurs Live")
    st.write("Kurs resmi dari Bank Sentral, bukan angka paten.")

    nilai = st.number_input("Masukkan Nominal:", value=100000.0, min_value=0.0)

    col1, col2 = st.columns(2)
    with col1:
        dari = st.selectbox("Dari:", ["IDR", "USD", "MYR", "SAR", "JPY", "EUR", "SGD"])
    with col2:
        ke = st.selectbox("Ke:", ["IDR", "USD", "MYR", "SAR", "JPY", "EUR", "SGD"])

    if st.button("Konversi 🔄"):
        kurs, sumber = get_kurs(dari, ke)

        if kurs:
            hasil = nilai * kurs
            st.success(f"### {nilai:,.0f} {dari} = {hasil:,.2f} {ke}")
            st.caption(f"1 {dari} = {kurs} {ke}")
            st.caption(f"Sumber: {sumber}")
            st.info("💡 Kurs ini kurs tengah resmi. Kalau ke money changer di Situbondo, biasanya selisih sedikit karena ada biaya admin. Itu wajar.")
        else:
            st.error("⚠️ Gagal ambil kurs, internet / API lagi down. Coba lagi 1 menit. Jangan pakai angka paten buat transaksi!")