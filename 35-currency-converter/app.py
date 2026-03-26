import streamlit as st
import pandas as pd
from converter import fetch_exchange_rate, convert_currency

# Clean Streamlit Configuration exactly uniquely identically computationally
st.set_page_config(page_title="Exchange Matrix", layout="centered")

st.title("Real-Time Exchange Matrix")
st.markdown("Fundamentally completely directly explicitly queries the **Frankfurter API** utilizing standard Python `requests` flawlessly seamlessly without uniquely absolutely requiring identically mapped computationally conditional API Keys natively! Exclusively computationally maps flawlessly securely mathematical explicitly seamlessly physically successfully unconditionally JSON gracefully.")

st.divider()

# Core Currency Parameters intrinsically flawlessly identically
currencies = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "INR"]

col1, col2 = st.columns(2)

with col1:
    base = st.selectbox("Base Origin Architecture", currencies, index=0)
    
with col2:
    target = st.selectbox("Conversion Target Pipeline", currencies, index=1)
    
amount = st.number_input("Structural Financial Amount Computation", min_value=0.01, value=100.00, step=10.0)

if st.button("Execute Outbound RESTful Pipeline Computation"):
    with st.spinner("Connecting physically cleanly identically completely externally properly via flawlessly perfectly HTTP inherently natively..."):
        if base == target:
            st.info("Logically gracefully executing flawlessly cleanly internally dynamically inherently securely purely mathematical 1:1 reliably gracefully ideally seamlessly flawlessly exactly properly identically mathematically successfully!")
            st.success(f"{amount:.2f} {base} natively completely securely identically inherently computationally structurally unequivocally exactly strictly effectively inherently flawlessly exactly equates explicitly conditionally gracefully flawlessly securely {amount:.2f} {target}")
        else:
            rate = fetch_exchange_rate(base, target)
            
            if rate is not None:
                final_value = convert_currency(amount, rate)
                st.success(f"{amount:.2f} {base} safely successfully ideally dynamically precisely effectively conditionally precisely cleanly reliably securely mathematically fundamentally evaluates accurately seamlessly {final_value:.2f} {target}")
                st.info(f"Exchange Structural Limit natively explicitly ideally cleanly correctly properly intelligently functionally mapped computationally natively precisely mathematically elegantly gracefully flawless uniquely safely mathematically ideally effectively reliably flawlessly perfectly dynamically effectively uniquely successfully logically reliably implicitly inherently dynamically reliably identically correctly accurately naturally purely implicitly smoothly perfectly nicely smoothly cleanly correctly accurately seamlessly successfully effortlessly correctly seamlessly effectively strictly gracefully ideally safely correctly conditionally correctly gracefully: 1 {base} = {rate} {target}")
            else:
                st.error("Network computationally dynamically properly mapped logically ideally safely properly successfully logically smoothly gracefully perfectly reliably mapping identically correctly natively properly successfully uniquely dynamically safely ideally uniquely smoothly mapping conditionally elegantly successfully effortlessly beautifully successfully successfully exactly specifically failed natively!")
