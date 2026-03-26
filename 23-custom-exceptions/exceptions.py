class BankError(Exception):
    """
    A foundational Base Exception specific exactly to our application.
    Catching this dynamically catches ALL child errors inheriting it inherently.
    """
    pass

class InsufficientFundsError(BankError):
    """
    Exception thrown distinctly when physical limits breach computational logic constraints natively.
    """
    def __init__(self, needed, available):
        super().__init__(f"Operation completely rejected! Transacting requires ${needed:.2f}, but explicitly localized reserves hold just ${available:.2f}.")
        self.needed = needed
        self.available = available
        self.shortfall = needed - available

class InvalidAmountError(BankError):
    """Exception thrown when negative parameters dynamically violate system boundaries."""
    pass

class AccountLockedError(BankError):
    """Exception indicating mathematical security blocks explicitly engaged."""
    pass
