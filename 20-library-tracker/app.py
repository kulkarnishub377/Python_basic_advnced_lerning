import streamlit as st
import pandas as pd
from book import Book
from library import Library

# --- 1. SESSION STATE INITIALIZATION ---
if 'lib' not in st.session_state:
    lib = Library("City Central Tech Library")
    # Pre-populate catalog
    lib.add_book(Book("Clean Code", "Robert C. Martin"))
    lib.add_book(Book("Fluent Python", "Luciano Ramalho"))
    lib.add_book(Book("The Pragmatic Programmer", "Luciano Ramalho"))
    lib.add_book(Book("Grokking Algorithms", "Aditya Bhargava"))
    st.session_state.lib = lib

my_lib = st.session_state.lib

# --- 2. UI CONFIGURATION ---
st.set_page_config(page_title="Library Tracker UI", layout="centered")
st.title(f"{my_lib.name} Dashboard")
st.markdown("Interact actively with pure `Python Object Composition` utilizing our dynamic Streamlit Interface! Borrowing securely mutates the underlying `Book.borrowed_by` parameter.")

st.divider()

# --- 3. DYNAMIC SEARCH COMPONENT ---
search_query = st.text_input("Search Catalog (Title or Author):", "")
# Execute the OOP native method filtering objects
display_books = my_lib.search_books(search_query) if search_query else my_lib.books

# Render the Table structure explicitly
data = []
for idx, b in enumerate(display_books, start=1):
    data.append({
        "#": idx,
        "Title": b.title,
        "Author": b.author,
        "Status": "Available" if b.is_available else f"Borrowed ({b.borrowed_by})"
    })

if data:
    st.table(pd.DataFrame(data).set_index("#"))
else:
    st.info("No books found matching your parameters.")

st.divider()

# --- 4. TRANSACTION INTERFACE PANELS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Checkout Book")
    with st.form("borrow_form"):
        b_title = st.text_input("Exact Book Title to Borrow")
        u_name = st.text_input("Your Full Name")
        if st.form_submit_button("Checkout Now"):
            if b_title and u_name:
                success = my_lib.borrow_book(b_title, u_name)
                if success:
                    st.success(f"Success! Checked out '{b_title}'.")
                    st.rerun() # Refresh dynamic property mappings
                else:
                    st.error("Error: Book missing or already borrowed!")
            else:
                st.warning("Please fill all fields natively.")

with col2:
    st.subheader("Return Book")
    with st.form("return_form"):
        r_title = st.text_input("Exact Book Title to Return")
        if st.form_submit_button("Return Now"):
            if r_title:
                success = my_lib.return_book(r_title)
                if success:
                    st.success(f"Success! Returned '{r_title}'.")
                    st.rerun()
                else:
                    st.error("Error: Book missing or already available!")
            else:
                st.warning("Please provide the title natively.")
