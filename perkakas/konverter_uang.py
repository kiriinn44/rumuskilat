import streamlit as st

def tampilkan_konverter_uang():
    st.title("💱 Konverter Uang")
    st.write("Buat cek kurs cepat. Mau belanja online, kirim uang, atau hitung gaji.")

    st.warning("⚠️ Kurs ini perkiraan saja ya bro. Untuk transaksi beneran, cek kurs di bank / money changer.")

    nilai = st.number_input("Masukkan Nominal:", value=100000.0, min_value=0.0, step=1000.0)

    col1, col2 = st.columns(2)
    with col1:
        dari = st.selectbox("Dari:", ["Rupiah (IDR)", "Dollar (USD)", "Ringgit (MYR)", "Riyal (SAR)", "Yen (JPY)"])
    with col2:
        ke = st.selectbox("Ke:", ["Rupiah (IDR)", "Dollar (USD)", "Ringgit (MYR)", "Riyal (SAR)", "Yen (JPY)"])

    # Kurs perkiraan, semua diubah ke IDR dulu
    ke_idr = {
        "Rupiah (IDR)": 1,
        "Dollar (USD)": 16000,
        "Ringgit (MYR)": 3400,
        "Riyal (SAR)": 4260,
        "Yen (JPY)": 105
    }

    hasil = nilai * ke_idr[dari] / ke_idr[ke]

    st.divider()
    st.success(f"### Hasil: {nilai:,.0f} {dari} = {hasil:,.2f} {ke}")

    st.info("💡 Contoh Situbondo: Gaji TKI 1000 Riyal (SAR) = sekitar Rp 4.260.000. Lumayan buat bangun rumah di Panji.")