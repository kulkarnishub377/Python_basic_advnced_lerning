from bank import SecureBank
from exceptions import BankError, InsufficientFundsError, InvalidAmountError

def simulate_banking_operations():
    """
    Demonstrates explicitly mapping specific pure structural errors natively 
    incorporating try/except/else/finally control matrices.
    """
    
    print("Initiating custom Exception Hierarchy Tests:")
    print("-" * 50)
    
    account = SecureBank(balance=150.00)
    
    # 1. We test explicit Success mapping (the 'else' block)
    try:
        account.withdraw(50.0)
    except BankError as e:
        print(f"Failure: {e}")
    else:
        print("Execution logic mapped exclusively flawlessly entirely within 'else'!")
    finally:
        print("Executing cleanup natively inside 'finally' block inherently regardless.\n")
        
    # 2. We deliberately test specifically typed structural InsufficientFunds exceptions
    try:
        account.withdraw(500.0)
    except InsufficientFundsError as e:
        # We map specific structural attributes nested deeply within the class!
        print(f"Caught typed Error! Your shortfall limit natively missed by explicitly: ${e.shortfall:.2f}")
    except BankError as e:
        print("Caught absolutely generic foundational boundary.")
        
    # 3. We cause repeated explicit failures dynamically generating lockout variables explicitly
    print("\nAttempting repeated invalid iterations generating logic lockouts...")
    for _ in range(4):
        try:
            account.withdraw(-10)
        except InvalidAmountError as e:
            print(f"Invalid Math: {e}")
        except BankError as e:
            # Captures the absolute AccountLockedError dynamically flawlessly
            print(f"Fatal Generic: {e}")

if __name__ == "__main__":
    simulate_banking_operations()
