import streamlit as st

st.write("ayooo")

with st.form("my_form"):
   st.write("Eosinophil calculator")
   wbc = st.number_input("WBC count (x1000)", min_value=0.0,max_value=40.0,step=0.01,value=7.8)
   eos = st.number_input("Eosinophil %", min_value=0,max_value=75,step=1,value=10)

   # Every form must have a submit button.
   submitted = st.form_submit_button("Calculate")
   if submitted:
     wbcm = wbc*1000
     eosm = eos/100
     st.header(f"Eosinophil count: {wbcm*eosm}")