import streamlit as st
from dataclasses import dataclass
from datetime import datetime
from typing import List

# --- Domain Events ---
@dataclass
class Event:
    timestamp: datetime

@dataclass
class AccountCreated(Event):
    account_id: str
    owner: str

@dataclass
class FundsDeposited(Event):
    account_id: str
    amount: float

@dataclass
class FundsWithdrawn(Event):
    account_id: str
    amount: float

# --- Event Store (Write Side / Command Side) ---
if "event_store" not in st.session_state:
    st.session_state.event_store = []

def save_event(event: Event):
    st.session_state.event_store.append(event)

# --- Read Model (Query Side) ---
def get_account_balance(account_id: str) -> float:
    balance = 0.0
    for event in st.session_state.event_store:
        if isinstance(event, FundsDeposited) and event.account_id == account_id:
            balance += event.amount
        elif isinstance(event, FundsWithdrawn) and event.account_id == account_id:
            balance -= event.amount
    return balance

def get_account_history(account_id: str) -> List[str]:
    history = []
    for event in st.session_state.event_store:
        if isinstance(event, AccountCreated) and event.account_id == account_id:
            history.append(f"[{event.timestamp.strftime('%H:%M:%S')}] Account created by {event.owner}")
        elif isinstance(event, FundsDeposited) and event.account_id == account_id:
            history.append(f"[{event.timestamp.strftime('%H:%M:%S')}] Deposited ${event.amount:.2f}")
        elif isinstance(event, FundsWithdrawn) and event.account_id == account_id:
            history.append(f"[{event.timestamp.strftime('%H:%M:%S')}] Withdrew ${event.amount:.2f}")
    return history


# --- UI ---
st.set_page_config(page_title="CQRS & Event Sourcing Bank", layout="wide")
st.title("🏦 CQRS & Event Sourcing Bank")

st.markdown("""
Unlike traditional CRUD where we just update a `balance` column, **Event Sourcing** stores an immutable log of events. 
The **CQRS** pattern separates adding events (Commands) from calculating the actual balance (Queries).
""")

# Initialize an account for demo
DEMO_ACCOUNT_ID = "ACC-001"
if not any(isinstance(e, AccountCreated) for e in st.session_state.event_store):
    save_event(AccountCreated(timestamp=datetime.now(), account_id=DEMO_ACCOUNT_ID, owner="Alice"))


col1, col2 = st.columns(2)

with col1:
    st.header("✍️ Command (Write Side)")
    
    amount_to_deposit = st.number_input("Deposit Amount", min_value=1.0, step=1.0, value=100.0)
    if st.button("Submit Deposit"):
        save_event(FundsDeposited(timestamp=datetime.now(), account_id=DEMO_ACCOUNT_ID, amount=amount_to_deposit))
        st.success(f"Deposited ${amount_to_deposit}!")
        
    st.divider()
    
    amount_to_withdraw = st.number_input("Withdraw Amount", min_value=1.0, step=1.0, value=50.0)
    if st.button("Submit Withdrawal"):
        current_balance = get_account_balance(DEMO_ACCOUNT_ID)
        if current_balance >= amount_to_withdraw:
            save_event(FundsWithdrawn(timestamp=datetime.now(), account_id=DEMO_ACCOUNT_ID, amount=amount_to_withdraw))
            st.success(f"Withdrew ${amount_to_withdraw}!")
        else:
            st.error("Insufficient Funds!")

with col2:
    st.header("📖 Query (Read Side)")
    
    if st.button("Refresh View"):
        pass # Streamlit reruns
        
    current_balance = get_account_balance(DEMO_ACCOUNT_ID)
    st.metric("Current Balance", f"${current_balance:.2f}")
    
    st.subheader("Event Ledger (Immutable)")
    history = get_account_history(DEMO_ACCOUNT_ID)
    for h in history:
        st.text(h)
