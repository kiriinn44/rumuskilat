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

    # TAB 2: NILAI AKHIR
    with tab2:
        st.subheader("Nilai Akhir (Tugas + UTS + UAS)")
        st.write("Rumus sekolah yang biasa dipakai: Tugas 30% + UTS 30% + UAS 40%")

        col1, col2, col3 = st.columns(3)
        with col1:
            tugas = st.number_input("Nilai Tugas (30%)", 0, 100, 85, key="tugas")
        with col2:
            uts = st.number_input("Nilai UTS (30%)", 0, 100, 80, key="uts")
        with col3:
            uas = st.number_input("Nilai UAS (40%)", 0, 100, 90, key="uas")

        if st.button("Hitung Nilai Akhir", key="btn_akhir"):
            nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)
            st.metric("Nilai Akhir Lu", f"{nilai_akhir:.2f}")

            if nilai_akhir >= 85:
                st.success("Nilai Akhir A! Lu aman, bisa santai dikit.")
            elif nilai_akhir >= 70:
                st.warning("Nilai Akhir B / C. UAS-nya naikin dikit lagi bro.")
            else:
                st.error("Nilai Akhir di bawah 70. Harus remedial bro, semangat!")

            with st.expander("Lihat cara ngitungnya"):
                st.write(f"= ({tugas} x 30%) + ({uts} x 30%) + ({uas} x 40%)")
                st.write(f"= {tugas*0.30:.1f} + {uts*0.30:.1f} + {uas*0.40:.1f} = **{nilai_akhir:.2f}**")