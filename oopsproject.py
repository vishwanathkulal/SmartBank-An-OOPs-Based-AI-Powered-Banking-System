from datetime import datetime
from transformers import pipeline

class Bank:
    Bank_name = "Canara Bank"
    Branch = "Kundapura 576234, Kundapura(T), Udupi(D)"

    def __init__(self, FirstName, LastName, DateofBirth, Address, contact_number, Email):
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateofBirth = DateofBirth
        self.Address = Address
        self.contact_number = contact_number
        self.Email = Email
        self.__balance = 0.0
        self.transactions = []  # Stores transactions

    def customer_details(self):
        print(f"\nDear {self.FirstName} {self.LastName}, your account has been created successfully!")
        print(f"Details:\nDate of Birth: {self.DateofBirth}\nAddress: {self.Address}\nContact: {self.contact_number}\nEmail: {self.Email}\nCurrent Balance: ₹{self.__balance}")

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                print("\nEnter a valid amount greater than zero.")
                return
            
            self.__balance += amount  
            print(f"\n₹{amount} added successfully! New balance: ₹{self.__balance}")

        except ValueError:
            print("\nInvalid input! Please enter a number.")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                print("\nEnter a valid amount greater than zero.")
                return
            
            if amount > self.__balance:
                print("\nInsufficient balance! Check your account and try again.")
                return
            
            self.__balance -= amount  
            print(f"\n₹{amount} withdrawn successfully! New balance: ₹{self.__balance}")

        except ValueError:
            print("\nInvalid input! Please enter a number.")

    def show_transactions(self):
        print("\nTransaction History:")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for t in self.transactions[-5:]:  # Show last 5 transactions
                print(t)

class SavingsAccount(Bank):
    def account_type(self):
        return "Savings Account"

class CurrentAccount(Bank):
    def account_type(self):
        return "Current Account"

chatbot = pipeline("question-answering", model="deepset/roberta-base-squad2")

from transformers import pipeline


chatbot = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Banking Chatbot  
banking_info = {
    "1": "Account Types\n   - Savings: Earns 3.5% interest, withdrawal limits.\n   - Current: No interest, no withdrawal limits (for businesses).",
    "2": "Minimum Balance\n   - Savings: ₹1000\n   - Current: ₹5000",
    "3": "Deposits & Withdrawals\n   - Deposit: Bank, ATM, NEFT, UPI, IMPS.\n   - Withdraw: ATM, cheque, branch.",
    "4": "Loan Services\n   - Home, Personal, Business Loans available.\n   - EMI repayment options.",
    "5": "Banking Charges & Fees\n   - Penalty for low balance.\n   - ATM withdrawal limits, online transfer fees.",
    "6": "Interest Rates\n   - Savings: Compounded quarterly.\n   - Fixed Deposits offer higher returns.",
    "7": "Digital Banking\n   - Check balance via net banking, apps, ATM.\n   - UPI for quick payments.",
    "8": "Security & Support\n   - 24/7 support, OTP for transactions.\n   - Never share your PIN or OTP."
}

def bank_chatbot():
    print(" Welcome to the Banking Chatbot! \n")
    
    while True:
        print("\n Choose a topic to learn more:")
        for key, value in banking_info.items():
            first_line = value.split("\n")[0]  
            print(f"{key} {first_line}")  

        choice = input("\n🔹 Enter a number (1-8) or 'exit' to quit: ").strip()

        if choice.lower() == "exit":
            print("\n Thank you for using the Banking Chatbot! Have a great day. \n")
            break

        print("\n " + banking_info.get(choice, " Invalid choice! Please try again."))



print(f"Welcome 🙏 to {Bank.Bank_name}, {Bank.Branch}")

FirstName = input("Enter your First Name: ").strip()
LastName = input("Enter your Last Name: ").strip()

# To check and validate Date of Birth format
while True:
    DateofBirth = input("Enter your Date of Birth (DD/MM/YYYY): ").strip()
    try:
        datetime.strptime(DateofBirth, "%d/%m/%Y")
        break
    except ValueError:
        print("Invalid format! Please enter in DD/MM/YYYY format.")

Address = input("Enter your Address: ").strip()

# To check and validate contact number
while True:
    contact_number = input("Enter your Contact Number: ").strip()
    if contact_number.isdigit() and len(contact_number) == 10:
        break
    else:
        print("Invalid contact number! Please enter a 10-digit number.")

Email = input("Enter your Email: ").strip()
account_type = input("Enter Account Type (Savings/Current): ").strip().lower()

# Create account based on type
if account_type == "savings":
    new_customer = SavingsAccount(FirstName, LastName, DateofBirth, Address, contact_number, Email)
elif account_type == "current":
    new_customer = CurrentAccount(FirstName, LastName, DateofBirth, Address, contact_number, Email)
else:
    print("Invalid account type! Defaulting to Savings Account.")
    new_customer = SavingsAccount(FirstName, LastName, DateofBirth, Address, contact_number, Email)

new_customer.customer_details()
print(f"\nAccount Type: {new_customer.account_type()}")

# Banking Menu
while True:
    print("\nSelect an option:\n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. View Transactions\n5. Banking Chatbot\n6. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        amount = input("Enter amount to deposit: ").strip()
        new_customer.deposit(amount)

    elif choice == "2":
        amount = input("Enter amount to withdraw: ").strip()
        new_customer.withdraw(amount)

    elif choice == "3":
        print(f"\nYour current balance is: ₹{new_customer.get_balance()}")

    elif choice == "4":
        new_customer.show_transactions()

    elif choice == "5":
        bank_chatbot()  # Call AI Chatbot

    elif choice == "6":
        print("\nThank you for banking with us! Have a great day!")
        break

    else:
        print("\nInvalid choice! Please select a valid option.")
