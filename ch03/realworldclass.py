from datetime import datetime

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        if initial_balance > 0:
            self.transaction_history.append(f"Initial deposit: +${initial_balance}")

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("입금액은 0보다 커야 합니다.")
            self.balance += amount
            self.transaction_history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Deposit: +${amount:.2f}")
            return True
        except ValueError as e:
            print(f"오류: {e}")
            return False

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("출금액은 0보다 커야 합니다.")
            if self.balance < amount:
                raise ValueError("잔액이 부족합니다.")
            self.balance -= amount
            self.transaction_history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Withdrawal: -${amount:.2f}")
            return True
        except ValueError as e:
            print(f"오류: {e}")
            return False

    def get_balance(self):
        return f"${self.balance:.2f}"

    def print_statement(self):
        print(f"\nAccount Statement for {self.account_holder}")
        print(f"Current Balance: {self.get_balance()}")
        print("\nTransaction History:")
        for transaction in self.transaction_history:
            print(transaction)


def main():
    print("Welcome to the Banking System!")
    name = input("Please enter account holder name: ")
    
    while True:
        try:
            initial = float(input("Enter initial deposit amount: $"))
            if initial < 0:
                raise ValueError("Initial deposit cannot be negative")
            break
        except ValueError:
            print("Please enter a valid positive number")
    
    account = BankAccount(name, initial)
    
    while True:
        print("\n=== Banking Menu ===")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Print Statement")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            amount = input("Enter deposit amount: $")
            if account.deposit(amount):
                print("Deposit successful!")
                
        elif choice == '2':
            amount = input("Enter withdrawal amount: $")
            if account.withdraw(amount):
                print("Withdrawal successful!")
                
        elif choice == '3':
            print(f"\nCurrent Balance: {account.get_balance()}")
            
        elif choice == '4':
            account.print_statement()
            
        elif choice == '5':
            print("\nThank you for using our banking system!")
            break
            
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

