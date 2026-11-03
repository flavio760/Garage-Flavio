import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Garage di Flavio", page_icon="🏎️")

st.title("🏎️ Il tuo Garage - Ferrari vs Lambo")
st.write("Clicca i bottoni e guarda cosa succede!")

dati = pd.DataFrame({
    "Anno": [2021, 2022, 2023, 2024],
    "Ferrari": [11155, 13221, 13398, 13752],
    "Lamborghini": [8405, 9233, 10112, 10687]
})

scelta = st.radio("Cosa vuoi vedere?", ["Ferrari", "Lamborghini", "Confronto"], horizontal=True)

if scelta == "Ferrari":
    st.metric("Auto Ferrari nel 2024", "13.752", "+2.6%")
    st.line_chart(dati, x="Anno", y="Ferrari")
elif scelta == "Lamborghini":
    st.metric("Auto Lamborghini nel 2024", "10.687", "+5.7%")
    st.line_chart(dati, x="Anno", y="Lamborghini")
else:
    st.line_chart(dati, x="Anno", y=["Ferrari", "Lamborghini"])
    st.balloons()

st.divider()
st.subheader("📊 Scarica i dati per la tesina")

buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
    dati.to_excel(writer, index=False, sheet_name='Ferrari vs Lambo')
    
st.download_button(
    label="⬇️ SCARICA FILE EXCEL",
    data=buffer.getvalue(),
    file_name="tesina_flavio_ferrari_vs_lambo.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
