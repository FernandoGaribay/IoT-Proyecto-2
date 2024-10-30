import random
from datetime import datetime, timedelta

class QuantumBankMethods():

    BANK_NAME = "QuantumBank"
    BANK_CONTACT_INFO = "+52 55-1234-5678"
    BANK_EMAIL = "contacto@quantumbank.com"
    BANK_ADDRESS = "Avenida Paseo de la Reforma 1234, Colonia Juárez, C.P. 06600, Ciudad de México, México"

    def get_account_number(self):
        return ''.join(str(random.randint(0, 9)) for _ in range(18))

    def get_current_balance(self):
        balance = random.randint(1000, 80000)
        return f"${balance:,.2f} MXN"

    def get_current_date(self):
        return datetime.now().strftime('%Y-%m-%d')

    def get_previous_month_start(self):
        current_date = datetime.now()
        first_day_of_current_month = current_date.replace(day=1)
        last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)
        return last_day_of_previous_month.strftime('%Y-%m-%d')

    def get_credit_limit(self):
        credit = random.choice([5000, 15000, 50000, 200000, 300000])
        return f"${credit:,.2f} MXN"
    
    def get_billing_date(self, days_until_billing=30):
        billing_date = datetime.now() + timedelta(days=days_until_billing)
        return billing_date.strftime('%Y-%m-%d')

    def get_due_date(self, days_until_due=15):
        billing_date = datetime.now() + timedelta(days=30)
        due_date = billing_date + timedelta(days=days_until_due)
        return due_date.strftime('%Y-%m-%d')

    def get_account_type(self):
        return random.choice(["Savings", "Checking", "Business", "Investment", "Joint"])

    def get_account_opening_date(self):
        current_date = datetime.now()
        months_back = random.randint(5, 12)
        days_back = random.randint(1, 30)
        opening_date = current_date - timedelta(days=(months_back * 30 + days_back))
        return opening_date.strftime('%Y-%m-%d')
    
    def get_total_amount(self):
        amount = random.randint(10000, 500000)
        return f"${amount:,.2f} MXN"

    def get_invoice_description(self):
        descriptions = [
            "Payment for services rendered",
            "Monthly subscription",
            "Grocery shopping",
            "Utility bill payment",
            "Transfer to savings account",
            "Loan repayment",
            "Online purchase",
            "ATM withdrawal",
            "Investment in stocks",
            "Gift deposit"
        ]
        return f"{random.choice(descriptions)}"

        
if __name__ == "__main__":
    bank_methods = QuantumBankMethods()
    
    print("Bank Contact Info:", bank_methods.BANK_CONTACT_INFO)
    print("Bank Email:", bank_methods.BANK_EMAIL)
    print("Bank Address:", bank_methods.BANK_ADDRESS)
    print("Account Number:", bank_methods.get_account_number())
    print("Random Balance:", bank_methods.get_current_balance())
    print("Current Date:", bank_methods.get_current_date())
    print("Random Credit Limit:", bank_methods.get_credit_limit())
    print("Billing Date:", bank_methods.get_billing_date())
    print("Due Date:", bank_methods.get_due_date())
    print("Account Type:", bank_methods.get_account_type())
    print("Account Opening Date:", bank_methods.get_account_opening_date())
    print("Total Amount:", bank_methods.get_total_amount())
    print("Invoice Description:", bank_methods.get_invoice_description())
    print("Previous Month: ", bank_methods.get_previous_month_start())
