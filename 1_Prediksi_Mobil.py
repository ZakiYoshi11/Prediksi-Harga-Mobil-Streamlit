import streamlit as st
import pickle
import numpy as np


# membuka file model
model=pickle.load(open('Util/estimasi_mobil.sav', 'rb'))


# ==================setup layout==================
st.set_page_config(
    page_title="Prediksi Harga Mobil",
    page_icon="🚗"
)

# ==================header==================
st.header('Aplikasi Prediksi Harga Mobil BMW Bekas')

# ==================input==================
# tahun, mileage, tax, mpg, engineSize
tahun =st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input jarak tempuh mobil')
tax = st.number_input('Input Pajak mobil')
mpg = st.number_input('Input BBM Mobil')
engineSize = st.number_input('Input Engine Size Mobil')

# ==================prediksi==================
if st.button('Prediksi'):
    new_data = np.array([[tahun, mileage, tax, mpg, engineSize]])
    prediksi = model.predict(new_data)
    pred =prediksi[0]

    # convert UER to IDR
    idr = pred * 19000

    # ==================output==================
    if pred > 0:
        st.write(f'Harga prediksi mobil BMW bekas (Pounds) :£ {pred:,.2f}')
        st.write(f'Harga prediksi mobil BMW bekas (IDR) : {idr:,.0f},-Rp')
    else:
        st.write("Belum Ada Inputan")
