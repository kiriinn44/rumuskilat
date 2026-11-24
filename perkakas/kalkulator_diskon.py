import streamlit as st

def tampilkan_kalkulator_diskon():
    st.title("🏷️ Kalkulator Diskon")
    st.write("Jangan sampai ketipu diskon palsu. Hitung dulu sebelum bayar!")

    harga_awal = st.number_input("Harga Awal (Rp):", value=150000.0, min_value=0.0, step=1000.0)
    diskon = st.slider("Diskon (%):", 0, 90, 30)

    potongan = harga_awal * diskon / 100
    harga_akhir = harga_awal - potongan

    col1, col2 = st.columns(2)
    col1.metric("Kamu Hemat", f"Rp {potongan:,.0f}")
    col2.metric("Yang Harus Dibayar", f"Rp {harga_akhir:,.0f}")

    st.divider()
    st.success(f"Jadi, barang Rp {harga_awal:,.0f} diskon {diskon}% -> Bayar **Rp {harga_akhir:,.0f}** saja!")

    if diskon >= 50:
        st.balloons()
        st.write("🔥 Wah, diskon gede ini! Gas beli bro!")
    else:
        st.info("💡 Contoh Situbondo: Baju di Toko Panji harga 150rb diskon 30%, bayarnya tinggal 105rb.")