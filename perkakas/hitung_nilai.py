import streamlit as st

def tampilkan_hitung_nilai():
    st.header("🎓 Hitung Nilai")
    st.write("Cek rata-rata lu sekarang, terus kejar target lu sampai tercapai!")

    tab1, tab2 = st.tabs(["Hitung Rata-rata", "Kejar Target Nilai"])

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

    # TAB 2: KEJAR TARGET (YANG BARU, GANTIIN PATUNGAN)
    with tab2:
        st.subheader("🎯 Kejar Target Nilai")
        st.write("Rata-rata lu masih kurang? Hitung di sini, ulangan besok lu harus dapat berapa biar target lu tercapai.")

        nilai_lama = st.text_input("Nilai-nilai lu yang sudah ada:", "70, 75, 80", key="input_target")
        target = st.number_input("Target rata-rata yang lu mau:", 0, 100, 85, key="target_rata")
        sisa_ulangan = st.number_input("Sisa ulangan yang masih ada:", 1, 10, 1, key="sisa_ulangan")

        if st.button("Hitung Nilai Yang Harus Gw Kejar", key="btn_target"):
            try:
                daftar = [float(x.strip()) for x in nilai_lama.split(",") if x.strip() != ""]
                if len(daftar) == 0:
                    st.warning("Isi dulu nilai lama lu bro.")
                else:
                    jumlah_lama = len(daftar)
                    total_lama = sum(daftar)
                    rata_sekarang = total_lama / jumlah_lama

                    st.write(f"Rata-rata lu sekarang: **{rata_sekarang:.2f}** dari {jumlah_lama} ulangan")
                    st.write(f"Target lu: **{target}**")

                    # RUMUSNYA DI SINI
                    # Total yang dibutuhkan = Target x (Jumlah Lama + Sisa)
                    # Nilai yang harus dikejar = Total Dibutuhkan - Total Lama
                    total_dibutuhkan = target * (jumlah_lama + sisa_ulangan)
                    total_yang_harus_dikejar = total_dibutuhkan - total_lama
                    perlu_per_ulangan = total_yang_harus_dikejar / sisa_ulangan

                    st.markdown("---")

                    if perlu_per_ulangan > 100:
                        st.error(f"Waduh bro, lu harus dapat rata-rata **{perlu_per_ulangan:.2f}** di {sisa_ulangan} ulangan sisa. Itu sudah di atas 100, mustahil!")
                        st.write("Solusinya: Turunin dikit target lu, atau minta ulangan tambahan ke guru lu. Jangan nyerah!")
                    elif perlu_per_ulangan <= 0:
                        st.balloons()
                        st.success(f"Selamat bro! Lu sudah lolos target {target}! Bahkan kalau ulangan besok lu dapat 0 pun, rata-rata lu tetap di atas target.")
                    elif perlu_per_ulangan > rata_sekarang:
                        st.success(f"Lu harus dapat rata-rata **{perlu_per_ulangan:.2f}** di {sisa_ulangan} ulangan yang tersisa!")
                        st.write(f"Berarti lu harus naik **{perlu_per_ulangan - rata_sekarang:.2f} poin** dari rata-rata lu sekarang. Berat, tapi masih bisa bro!")
                        st.progress(int(perlu_per_ulangan))
                        if perlu_per_ulangan >= 90:
                            st.warning("Ini berat banget bro, tapi bukan mustahil. Fokus belajar 1 bab yang paling sering keluar di ulangan!")
                        else:
                            st.info("Masih masuk akal! Lu cuma perlu lebih teliti dikit lagi pas ngerjain.")
                    else:
                        st.success(f"Gampang bro! Lu cuma perlu dapat **{perlu_per_ulangan:.2f}** saja di ulangan sisa, itu di bawah rata-rata lu sekarang. Santai, lu pasti bisa!")

                    with st.expander("Lihat cara ngitungnya"):
                        st.write(f"Total nilai lu sekarang = {total_lama:.0f}")
                        st.write(f"Total nilai yang dibutuhkan biar rata-rata {target} = {target} x ({jumlah_lama} + {sisa_ulangan}) = {total_dibutuhkan:.0f}")
                        st.write(f"Yang masih harus lu kejar = {total_dibutuhkan:.0f} - {total_lama:.0f} = {total_yang_harus_dikejar:.0f}")
                        st.write(f"Dibagi {sisa_ulangan} ulangan sisa = **{perlu_per_ulangan:.2f}** per ulangan")
            except:
                st.error("Formatnya salah bro, pakai koma ya. Contoh: 70, 75, 80")