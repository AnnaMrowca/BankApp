from view import displayMessage


class Account():
    def __init__(self):
        self.isPremium = False
        self.balance = 0
        self.account_history = []
        self.account_deposit = []
        self.instalments = dict()
        self.loan_durance = dict()

    def chooseTypeOfAccount(self, message):
        return displayMessage(message)

    def readAccountBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance = float(self.balance) - float(amount)
        return self.balance

    def deposit(self, amount):
        self.balance = float(self.balance) + float(amount)
        return self.balance

    def reviewAccountHistory(self):
        return self.account_history

    def initiateLongTermDeposit(self, amount):
        self.balance = float(self.balance) - float(amount)
        self.account_deposit.append(amount)
        return self.balance

    def getDepositAmount(self):
        return sum(self.account_deposit)

    def takeloan(self, amount, number_of_instalments, loan_period, loan_days, instalment):
        self.number_of_instalments = number_of_instalments
        self.loan_period = loan_period
        self.instalment = instalment
        self.loan_days = loan_days
        self.balance = float(self.balance) + float(amount)
        for i in range(0, self.number_of_instalments):
            self.instalments.update({i : (amount // self.number_of_instalments)})

        for i in range(0, self.loan_days):
            self.loan_durance.update({i : (self.loan_period // self.loan_days)})




#lokata, polega na przeniesieniu i zablokowaniu kwoty, która jest zablokowana,
# zerwanie lokaty polega na przywróceniu kwoty do balansu
#trzeba wyczyścić data.db - w czasie developmentu
