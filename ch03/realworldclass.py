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
    print("은행 시스템에 오신 것을 환영합니다!")
    name = input("계좌 소유자 이름을 입력하세요: ")
    
    while True:
        try:
            initial = float(input("초기 입금액을 입력하세요: ₩"))
            if initial < 0:
                raise ValueError("초기 입금액은 음수가 될 수 없습니다")
            break
        except ValueError:
            print("올바른 양수를 입력해주세요")
    
    account = BankAccount(name, initial)
    
    while True:
        print("\n=== 은행 메뉴 ===")
        print("1. 입금하기")
        print("2. 출금하기") 
        print("3. 잔액 확인")
        print("4. 거래내역 출력")
        print("5. 종료")
        
        choice = input("\n선택하세요 (1-5): ")
        
        if choice == '1':
            amount = input("입금액을 입력하세요: ₩")
            if account.deposit(amount):
                print("입금이 완료되었습니다!")
                
        elif choice == '2':
            amount = input("출금액을 입력하세요: ₩")
            if account.withdraw(amount):
                print("출금이 완료되었습니다!")
                
        elif choice == '3':
            print(f"\n현재 잔액: {account.get_balance()}")
            
        elif choice == '4':
            account.print_statement()
            
        elif choice == '5':
            print("\n은행 시스템을 이용해주셔서 감사합니다!")
            break
            
        else:
            print("잘못된 선택입니다! 다시 시도해주세요.")

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

