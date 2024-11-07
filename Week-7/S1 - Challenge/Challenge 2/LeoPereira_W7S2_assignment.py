import pytest

# Write a Class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

# Implement pytest Fixtures
@pytest.fixture
def bank_account():
    account = BankAccount(100)  # Initialize with a starting balance
    yield account
    # Teardown (if any) can be done here

### 3. Write Test Cases ###
# Unit Tests
def test_deposit(bank_account):
    assert bank_account.deposit(50) == 150
    assert bank_account.deposit(25)  # This should raise a ValueError

def test_withdraw(bank_account):
    assert bank_account.withdraw(30) == 70
    with pytest.raises(ValueError):
        bank_account.withdraw(200)  # This should raise a ValueError

def test_get_balance(bank_account):
    assert bank_account.get_balance() == 100

# Parameterized Tests
@pytest.mark.parametrize("deposit_amount, expected", [
    (50, 150), (100, 200), (150, 250), (-50, 100), (0, 100)
])
def test_deposit_parameterized(bank_account, deposit_amount, expected):
    if deposit_amount <= 0:
        with pytest.raises(ValueError):
            bank_account.deposit(deposit_amount)
    else:
        assert bank_account.deposit(deposit_amount) == expected

# Advanced Exception Handling
@pytest.mark.parametrize("withdraw_amount, exception", [
    (200, ValueError), (150, ValueError), (0, None)
])
def test_withdraw_exceptions(bank_account, withdraw_amount, exception):
    if exception:
        with pytest.raises(exception):
            bank_account.withdraw(withdraw_amount)
    else:
        assert bank_account.withdraw(withdraw_amount) == (100 - withdraw_amount)

# Grouping Tests using Test Classes
class TestBankAccount:
    def test_deposit(self, bank_account):
        assert bank_account.deposit(50) == 150

    def test_withdraw(self, bank_account):
        assert bank_account.withdraw(30) == 70

    def test_get_balance(self, bank_account):
        assert bank_account.get_balance() == 100

# Generate Coverage Reports


if __name__ == "__main__":
    pytest.main()
