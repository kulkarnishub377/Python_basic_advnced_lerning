# 83 - Event Sourcing and CQRS Pattern

This project demonstrates two advanced architectural patterns:
1. **Event Sourcing:** Instead of saving the *state* of an application (e.g. `balance = 50`), we save the *events* that led to it (e.g. `Deposited 100`, `Withdrew 50`). State is recreated by replaying these immutable events.
2. **CQRS (Command Query Responsibility Segregation):** The system has a strict separation between operations that change state (Commands) and operations that return data (Queries).

## Real-world Applications
- Banking and financial ledgers
- E-commerce shopping carts
- Systems where historical audit trails are mandatory.

## Running the Application

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Streamlit User Interface:
   ```bash
   streamlit run app.py
   ```
3. Deposit and withdraw funds to see the immutable event log grow!
