import streamlit as st
import math

st.set_page_config(page_title="RumusKilat - Math Calculator", page_icon="⚡", layout="centered")

# --- HEADER ---
st.title("⚡ RumusKilat")
st.markdown("Professional Math Calculator for Students & Professionals. Fast, Accurate, and Easy to Use.")
st.divider()

# --- SIDEBAR ---
st.sidebar.title("RumusKilat")
st.sidebar.markdown("Select a calculator category below.")
menu = st.sidebar.selectbox("Calculator Menu", 
    ["Area Calculator", "Perimeter Calculator", "Sigma Calculator", "Volume Calculator"])

st.sidebar.divider()
st.sidebar.markdown("### RumusKilat PRO")
st.sidebar.markdown("Unlock all features:")
st.sidebar.markdown("- Download results as PDF\n- No Ads\n- Full Formula Library\n- Priority Support")
if st.sidebar.button("Upgrade to PRO"):
    st.sidebar.info("Contact us via WhatsApp to activate PRO access.")

# --- 1. AREA ---
if menu == "Area Calculator":
    st.header("Area Calculator")
    shape = st.selectbox("Select Shape:", ["Square", "Rectangle", "Triangle", "Circle"])
    
    if shape == "Square":
        s = st.number_input("Side Length:", min_value=0.0, value=5.0)
        if st.button("Calculate", key="area_square"):
            st.success(f"Area of Square = {s} × {s} = **{s*s}**")
    elif shape == "Rectangle":
        p = st.number_input("Length:", min_value=0.0, value=10.0)
        l = st.number_input("Width:", min_value=0.0, value=5.0)
        if st.button("Calculate", key="area_rect"):
            st.success(f"Area = {p} × {l} = **{p*l}**")
    elif shape == "Triangle":
        a = st.number_input("Base:", min_value=0.0, value=10.0)
        t = st.number_input("Height:", min_value=0.0, value=5.0)
        if st.button("Calculate", key="area_tri"):
            st.success(f"Area = 1/2 × {a} × {t} = **{0.5*a*t}**")
    elif shape == "Circle":
        r = st.number_input("Radius:", min_value=0.0, value=7.0)
        if st.button("Calculate", key="area_circle"):
            st.success(f"Area = π × {r}² = **{math.pi*r*r:.2f}**")

# --- 2. PERIMETER ---
elif menu == "Perimeter Calculator":
    st.header("Perimeter Calculator")
    shape = st.selectbox("Select Shape:", ["Square", "Rectangle", "Circle"])
    if shape == "Square":
        s = st.number_input("Side Length:", min_value=0.0, value=5.0)
        if st.button("Calculate", key="per_square"):
            st.success(f"Perimeter = 4 × {s} = **{4*s}**")
    elif shape == "Rectangle":
        p = st.number_input("Length:", min_value=0.0, value=10.0)
        l = st.number_input("Width:", min_value=0.0, value=5.0)
        if st.button("Calculate", key="per_rect"):
            st.success(f"Perimeter = 2 × ({p} + {l}) = **{2*(p+l)}**")
    elif shape == "Circle":
        r = st.number_input("Radius:", min_value=0.0, value=7.0)
        if st.button("Calculate", key="per_circle"):
            st.success(f"Circumference = 2 × π × {r} = **{2*math.pi*r:.2f}**")

# --- 3. SIGMA - FITUR UNGGULAN ---
elif menu == "Sigma Calculator":
    st.header("Sigma Calculator")
    st.write("Calculate the sum of any custom series. Enter your values separated by commas.")
    
    teks = st.text_input("Enter numbers (e.g. 2, 5, 10)", "2,5,10")
    mode = st.selectbox("Calculation Type:", ["Sum (Σ x)", "Sum of Squares (Σ x²)", "Sum of Cubes (Σ x³)"])
    
    if st.button("Calculate Sigma"):
        try:
            angka_list = [float(x.strip()) for x in teks.split(",")]
            if mode == "Sum (Σ x)":
                hasil = sum(angka_list)
                st.success(f"{' + '.join(map(str, angka_list))} = **{hasil}**")
            elif mode == "Sum of Squares (Σ x²)":
                hasil = sum([x**2 for x in angka_list])
                st.success(f"Σ x² = **{hasil}**")
                st.caption(f"Expansion: {' + '.join([str(x**2) for x in angka_list])}")
            else:
                hasil = sum([x**3 for x in angka_list])
                st.success(f"Σ x³ = **{hasil}**")
                st.caption(f"Expansion: {' + '.join([str(x**3) for x in angka_list])}")
        except:
            st.error("Invalid format. Please use commas to separate numbers. Example: 2,5,10")

# --- 4. VOLUME ---
elif menu == "Volume Calculator":
    st.header("Volume Calculator")
    shape = st.selectbox("Select Shape:", ["Cube", "Cuboid", "Cylinder"])
    if shape == "Cube":
        s = st.number_input("Side Length:", min_value=0.0, value=5.0)
        if st.button("Calculate", key="vol_cube"):
            st.success(f"Volume of Cube = **{s**3}**")
    elif shape == "Cuboid":
        p = st.number_input("Length:", min_value=0.0, value=5.0)
        l = st.number_input("Width:", min_value=0.0, value=3.0)
        t = st.number_input("Height:", min_value=0.0, value=2.0)
        if st.button("Calculate", key="vol_cuboid"):
            st.success(f"Volume = **{p*l*t}**")
    elif shape == "Cylinder":
        r = st.number_input("Radius:", min_value=0.0, value=7.0)
        t = st.number_input("Height:", min_value=0.0, value=10.0)
        if st.button("Calculate", key="vol_cyl"):
            st.success(f"Volume = **{math.pi*r*r*t:.2f}**")

st.divider()
st.caption("© 2026 RumusKilat. Built for students worldwide.")
