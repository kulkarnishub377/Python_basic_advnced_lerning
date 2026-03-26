import streamlit as st
import pandas as pd
from inventory import Inventory
from product import Product

# Initialize the manager structurally inside session mapping reliably!
if 'inv' not in st.session_state:
    st.session_state.inv = Inventory()

inv = st.session_state.inv

st.set_page_config(page_title="Retail Inventory", layout="wide")

st.title("ClassMethod Retail Inventory")
st.markdown("Advanced `Streamlit` dashboard dynamically bridging `Python OOP Constructors`, `JSON Serialization`, and `Dunder (__lt__) Magic` directly interacting with explicitly loaded native Objects real-time!")

st.divider()

# --- LOW STOCK ALERT MODULE ---
low_stock = inv.get_low_stock_alerts()
if low_stock:
    st.error(f"Warning: {len(low_stock)} explicitly tracked products plunged beneath native Class Constant `LOW_STOCK_THRESHOLD` limits!")
    cols = st.columns(min(len(low_stock), 4))
    for idx, p in enumerate(low_stock[:4]):
        cols[idx].error(f"{p.name} (Only {p.stock} exactly remaining)")
else:
    st.success("Operating flawlessly! Zero targeted products dipping beneath standard threshold limits.")

# --- INVENTORY MANAGER VISUALS ---
col_table, col_form = st.columns([2, 1])

with col_table:
    st.subheader("Current Stock Catalog")
    
    if not inv.products:
        st.info("The structurally loaded JSON database maps currently completely empty.")
    else:
        # Utilize the __lt__ dunder operator natively sorting physical objects cleanly by explicit stock volumes!
        sorted_products = sorted(inv.products)
        
        df_list = [{"SKU": p.sku, "Name": p.name, "Price": f"${p.price:.2f}", "Stock": p.stock} for p in sorted_products]
        df = pd.DataFrame(df_list)
        st.dataframe(df, use_container_width=True, hide_index=True)

with col_form:
    st.subheader("Execute Operational POS Sales")
    with st.form("pos_form"):
        s_sku = st.text_input("Product SKU Code")
        s_qty = st.number_input("Purchase Quantity Iteration", min_value=1, step=1)
        if st.form_submit_button("Process Sale Check"):
            if s_sku:
                success, msg = inv.process_sale(s_sku, s_qty)
                if success:
                    st.success(msg)
                    st.rerun()
                else:
                    st.error(msg)

    st.divider()
    
    st.subheader("Onboard New Initial Products")
    with st.form("onboard_form"):
        n_sku = st.text_input("New Item SKU")
        n_name = st.text_input("Item Name Component")
        n_price = st.number_input("Retail Price Float", min_value=0.01, format="%.2f")
        n_stock = st.number_input("Initial Physical Stock", min_value=0, step=1)
        if st.form_submit_button("Serialize New Object"):
            if n_sku and n_name:
                new_item = Product(n_sku, n_name, n_price, n_stock)
                if inv.add_product(new_item):
                    st.success(f"Serialized `{n_name}` securely explicitly inside JSON variables natively!")
                    st.rerun()
                else:
                    st.error("Collision: SKU structural variables already dynamically actively populated.")
