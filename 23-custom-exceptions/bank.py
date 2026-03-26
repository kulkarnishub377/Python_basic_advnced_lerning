from exceptions import InsufficientFundsError, InvalidAmountError, AccountLockedError

class SecureBank:
    """
    A protected bank logic structure generating explicit errors dynamically 
    when structural boundaries are violated mathematically safely.
    """

    def __init__(self, balance=0.0):
        self.balance = balance
        self.is_locked = False
        self.failed_attempts = 0

    def withdraw(self, amount):
        """Executes safe math generating cleanly explicitly typed logic exceptions."""
        
        if self.is_locked:
            raise AccountLockedError(f"Account completely locked following {self.failed_attempts} consecutive logic violations!")
            
        if amount <= 0:
            self.failed_attempts += 1
            if self.failed_attempts >= 3:
                self.is_locked = True
                print("SECURITY: Locking account explicitly due to repetitive structural failures.")
            raise InvalidAmountError("Withdrawal matrices explicitly must exist above absolutely zero inherently.")
            
        if amount > self.balance:
            raise InsufficientFundsError(needed=amount, available=self.balance)
            
        # If no explicit Exceptions raise, process natively flawlessly!
        self.balance -= amount
        print(f"Success! Processed withdrawal mapped dynamically: ${amount:.2f}")
        return self.balance
