import streamlit as st

def tampilkan_hitung_nilai():
    st.header("🎓 Hitung Nilai")
    st.write("Hitung rata-rata nilai dan patungan bareng teman, tanpa ribet.")

    tab1, tab2 = st.tabs(["Hitung Rata-rata", "Kalkulator Patungan"])

    # TAB 1: RATA-RATA (TETAP)
    with tab1:
        st.subheader("Rata-rata Nilai Ulangan")
        st.write("Masukin semua nilai lu, pisahin pakai koma. Contoh: 70, 85, 90")

        input_nilai = st.text_input("Nilai-nilai lu:", "70, 85, 90, 100", key="input_rata")

        if st.button("Hitung Rata-rata", key="btn_rata"):
            try:
                daftar_nilai = [float(x.strip()) for x in input_nilai.split(",") if x.strip() != ""]
                if len(daftar_nilai) == 0:
                    st.warning("Isi dulu nilainya bro.")
                else:
                    rata = sum(daftar_nilai) / len(daftar_nilai)
                    st.success(f"Rata-rata lu: **{rata:.2f}** dari {len(daftar_nilai)} nilai")
                    st.progress(int(rata))
                    if rata >= 80:
                        st.balloons()
                        st.write("Gila, pinter banget lu bro! 🎉")
                    elif rata >= 70:
                        st.info("Sudah bagus, dikit lagi bisa 80!")
                    else:
                        st.warning("Masih bisa naik bro, semangat!")
            except:
                st.error("Formatnya salah bro, pakai koma ya. Contoh: 70, 85, 90")

    # TAB 2: PATUNGAN (YANG BARU)
    with tab2:
        st.subheader("🍕 Kalkulator Patungan / Bagi Rata")
        st.write("Makan bareng, beli kado patungan, atau patungan bensin. Biar nggak ada yang merasa dirugikan.")

        total = st.number_input("Total yang harus dibayar (Rp)", 0, 10000000, 150000, step=1000, key="patungan_total")
        jumlah_orang = st.number_input("Berapa orang yang patungan?", 1, 100, 5, key="patungan_orang")

        st.markdown("---")

        # Opsi: Ada yang sudah bayar duluan?
        ada_yang_bayar = st.checkbox("Ada yang sudah bayar duluan / nombokin?", key="cek_nombok")

        sudah_bayar = 0
        if ada_yang_bayar:
            sudah_bayar = st.number_input("Dia sudah bayar berapa? (Rp)", 0, 10000000, 50000, step=1000, key="sudah_bayar")
            st.info(f"Berarti sisanya yang belum dibayar: Rp {total - sudah_bayar:,}")

        if st.button("Hitung Patungan", key="btn_patungan"):
            if jumlah_orang <= 0:
                st.error("Jumlah orangnya harus lebih dari 0 bro.")
            elif sudah_bayar > total:
                st.error("Yang sudah dibayar kok lebih gede dari totalnya bro? Cek lagi.")
            else:
                sisa = total - sudah_bayar
                per_orang = sisa / jumlah_orang

                st.success(f"Setiap orang harus bayar: **Rp {per_orang:,.0f}**")
                st.write(f"Total: Rp {total:,} dibagi {jumlah_orang} orang")

                if ada_yang_bayar and sudah_bayar > 0:
                    # Kalau yang nombokin juga ikut patungan, dia harus dapat kembalian / bayar kurang
                    jatah_dia = per_orang
                    selisih = sudah_bayar - jatah_dia
                    if selisih > 0:
                        st.write(f"Yang sudah nombokin Rp {sudah_bayar:,} itu sebenarnya jatahnya cuma Rp {jatah_dia:,.0f}. Berarti teman-temannya harus ganti ke dia **Rp {selisih:,.0f}**.")
                    elif selisih < 0:
                        st.write(f"Yang sudah bayar Rp {sudah_bayar:,} masih kurang bayar **Rp {abs(selisih):,.0f}**.")
                    else:
                        st.write("Pas! Yang nombokin sudah bayar sesuai jatahnya.")

                # Rincian biar jelas
                with st.expander("Lihat rincian hitungnya"):
                    st.write(f"Total - Sudah Bayar = {total:,} - {sudah_bayar:,} = {sisa:,}")
                    st.write(f"Sisa / Jumlah Orang = {sisa:,} / {jumlah_orang} = **{per_orang:,.0f}**")