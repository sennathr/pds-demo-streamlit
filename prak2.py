"analisa pertemuan 5 tentang 5.Feature Addition.py"

import streamlit as st
import pandas as pd

st.title("Cek Judul dan Status SKP")

#1. Membaca file excel
df=pd.read_excel("data_skp_2.xlsx")

#2. Membuat kolom status (nilai default: Lulus)
df["status"]="Lulus"

#3. Membuat kolom status_judul (cek apakah judul kosong atau ada)
df["status_judul"]=df["JUDUL"].apply(
    lambda x:"Judul Kosong" if pd.isnull(x) or x ==""else"Ada Judul"
)

#4. Tampilkan isi dataframe di Streamlit
st.subheader("Data SKP")
st.dataframe(df)
