from account import Account

#zadanie na grudzien: account history - zamienić na dict, żeby pokazywał nam jakie operacje robiliśmy,
# dodać do history tworzenie long term deposit
# try, błędy ogarnąć

#Spłata kredytu, wypisuje dni, okreslam datę spłaty, rozkłada na raty
#kwota, czas, ilośc rat, on rozkłada to na raty, równa rata
# wpłaca kasę na konto, ale z drugiej strony mamy debet

class AccountPremium(Account):
    def __init__(self):
        super(AccountPremium, self).__init__()
        self.isPremium = True


    def withdraw(self, amount):
        return super().withdraw(amount + (0.005 * amount))

    def deposit(self, amount):
        return super().deposit(amount + (0.02 * amount))

    def initiateLongTermDeposit(self, amount):
        return self.balance