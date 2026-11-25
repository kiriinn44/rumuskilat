import streamlit as st

def tampilkan_hitung_nilai():
    st.header("🎓 Hitung Nilai")
    st.write("Hitung rata-rata ulangan dan nilai akhir lu dengan cepat, tanpa ribet.")

    tab1, tab2 = st.tabs(["Hitung Rata-rata", "Hitung Nilai Akhir"])

    # TAB 1: RATA-RATA
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

    # TAB 2: NILAI AKHIR - BOBOT BISA DIATUR
    with tab2:
        st.subheader("Nilai Akhir (Bobot Fleksibel)")
        st.write("Setiap sekolah beda kebijakan bro. Atur bobotnya sesuai sekolah lu, totalnya harus 100% ya.")

        # 1. Atur Bobot Dulu
        st.markdown("**1. Atur Bobotnya Dulu:**")
        col_b1, col_b2, col_b3 = st.columns(3)
        with col_b1:
            bobot_tugas = st.slider("Bobot Tugas (%)", 0, 100, 30, key="bobot_tugas")
        with col_b2:
            bobot_uts = st.slider("Bobot UTS (%)", 0, 100, 30, key="bobot_uts")
        with col_b3:
            bobot_uas = st.slider("Bobot UAS (%)", 0, 100, 40, key="bobot_uas")

        total_bobot = bobot_tugas + bobot_uts + bobot_uas
        st.write(f"Total Bobot: **{total_bobot}%**")

        if total_bobot != 100:
            st.error(f"Total bobot lu masih {total_bobot}%, harus 100% bro! Geser-geser dulu slider di atas sampai jadi 100%.")
        else:
            st.success("Total bobot sudah 100%, mantap! Lanjut isi nilainya di bawah.")

        # 2. Isi Nilainya
        st.markdown("**2. Isi Nilainya:**")
        col1, col2, col3 = st.columns(3)
        with col1:
            tugas = st.number_input(f"Nilai Tugas ({bobot_tugas}%)", 0, 100, 85, key="tugas")
        with col2:
            uts = st.number_input(f"Nilai UTS ({bobot_uts}%)", 0, 100, 80, key="uts")
        with col3:
            uas = st.number_input(f"Nilai UAS ({bobot_uas}%)", 0, 100, 90, key="uas")

        if st.button("Hitung Nilai Akhir", key="btn_akhir"):
            if total_bobot != 100:
                st.error("Belum bisa dihitung bro, total bobotnya harus 100% dulu.")
            else:
                nilai_akhir = (tugas * bobot_tugas/100) + (uts * bobot_uts/100) + (uas * bobot_uas/100)
                st.metric("Nilai Akhir Lu", f"{nilai_akhir:.2f}")

                if nilai_akhir >= 85:
                    st.success("Nilai Akhir A! Lu aman, bisa santai dikit.")
                elif nilai_akhir >= 70:
                    st.warning("Nilai Akhir B / C. UAS-nya naikin dikit lagi bro.")
                else:
                    st.error("Nilai Akhir di bawah 70. Harus remedial bro, semangat!")

                with st.expander("Lihat cara ngitungnya"):
                    st.write(f"= ({tugas} x {bobot_tugas}%) + ({uts} x {bobot_uts}%) + ({uas} x {bobot_uas}%)")
                    st.write(f"= {tugas*bobot_tugas/100:.1f} + {uts*bobot_uts/100:.1f} + {uas*bobot_uas/100:.1f} = **{nilai_akhir:.2f}**")