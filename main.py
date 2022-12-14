import streamlit as st

st.header("Simple Eosinophil Calculator")

with st.form("my_form"):
    wbc = st.number_input("WBC count (x1000)",
                          min_value=0.0,
                          max_value=40.0,
                          step=0.01,
                          value=7.8)
    eos = st.number_input("Eosinophil %",
                          min_value=0.0,
                          max_value=75.0,
                          step=0.01,
                          value=12.5)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Calculate")
    if submitted:
        wbcm = wbc * 1000
        eosm = eos / 100
        count = round(wbcm*eosm,2)
        st.subheader(f"Eosinophil count: {count}")
