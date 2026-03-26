"""
Simple Bank Account - Project 10
--------------------------------
What it does: A terminal banking simulation. Deposit, withdraw, and check 
balance with full validation: rejects negative amounts and overdrafts. 
Displays a mini transaction history. Good first stateful program.

Pro Hints:
- `global` is used minimally to modify the balance state inside functions.
- "Guard clauses" immediately return errors at the top of the function if 
  rules are violated, keeping the main logic un-nested.
"""

# Global State Variables
balance = 0.0
history = []

def deposit(amount):
    global balance
    
    # Guard clause: Fail fast if input is negative
    if amount <= 0:
        return False, "Deposit amount must be strictly greater than zero."
        
    balance += amount
    history.append(f"Deposited: +${amount:.2f}")
    return True, f"Successfully deposited ${amount:.2f}"

def withdraw(amount):
    global balance
    
    # Guard clauses
    if amount <= 0:
        return False, "Withdrawal amount must be strictly greater than zero."
    if amount > balance:
        return False, "Insufficient funds! Overdrafts are not allowed."
        
    balance -= amount
    history.append(f"Withdrew:  -${amount:.2f}")
    return True, f"Successfully withdrew ${amount:.2f}"

def show_history():
    print("\n--- Transaction History ---")
    if not history:
        print("No transactions yet.")
    else:
        for record in history[-5:]: # Show only last 5
            print(record)
    print(f"Current Balance: ${balance:.2f}")
    print("---------------------------\n")

def run_bank():
    print("Welcome to Secure Terminal Banking!")
    
    while True:
        print("\n1. Deposit | 2. Withdraw | 3. History | 4. Quit")
        choice = input("Select an option: ").strip()
        
        if choice == '4':
            print("Session ended. Thank you for banking with us!")
            break
            
        if choice == '3':
            show_history()
            continue
            
        if choice in ['1', '2']:
            try:
                amt = float(input("Enter amount: $"))
            except ValueError:
                print("Error: Invalid numeric input.")
                continue
                
            if choice == '1':
                success, msg = deposit(amt)
            else:
                success, msg = withdraw(amt)
                
            if not success:
                print(f"Failed: {msg}")
            else:
                print(f"Success: {msg}")
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    run_bank()
