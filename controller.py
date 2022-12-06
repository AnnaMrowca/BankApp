import account
import accountPremium
import view
from fileManager import FileManager
from view import getAmount, displayMessage, getClientAction, getLoanPeriod, getNumberOfInstalments


class Controller():
    def __init__(self):
        self.account = None
        while True:
            action = getClientAction('''
                            1 - create regular account
                            2 - create premium account
                            : ''')

            if action == 1:
                self.performActionToCreateRegularAccount()
            elif action == 2:
                self.performActionToCreatePremiumAccount()
            break

        self.file_manager = FileManager()
        self.accountPremium = self.file_manager.read()

    def performMainLoop(self):
        while True:
            action = getClientAction('''
                            Insert action number:
                            1 - withdraw
                            2 - deposit
                            3 - view account history
                            4 - terminate
                            5 - long term deposite
                            6 - take loan
                            7 - pay instalment
                            : ''')
            if action == 1:
                self.performActionToWidthraw()
            elif action == 2:
                self.performActionToDeposit()
            elif action == 3:
                self.performActionToReviewAccountHistory()
            elif action == 4:
                self.performActionToTerminate()
                return
            elif action == 5:
                self.performInitiateLongTermDeposit()
            elif action == 6:
                displayMessage('To be implemented... ')
                # TODO: implement
                # self.performActionToTakeLoan()

    def performActionToCreateRegularAccount(self):
        self.account = account.Account()
        if self.account.isPremium is False:
            displayMessage('You are using regular account')
        return self.account.isPremium

    def performActionToCreatePremiumAccount(self):
        self.account = accountPremium.AccountPremium()
        if self.account.isPremium is True:
            displayMessage('You are using premium account')
        return self.account.isPremium

    # TODO: loan impl. with installments schedule
    # def performActionToTakeLoan(self, period, instalments):
    #     self.file_manager.save(self.performActionToTakeLoanPeriod(), )
    #     # TODO: self.
    #     self.performActionToGetNumberOfInstalments()

    # TODO: installments schedule impl.
    # def performActionToTakeLoanPeriod(self):
    #     loan_period = getLoanPeriod('Provide loan period in days: ')
    #     displayMessage(f'Your loan period in days is {loan_period}')
    #     return  # TODO: trzeba by coś zwracał

    def performActionToGetNumberOfInstalments(self):
        number_of_instalments = getNumberOfInstalments('Provide number of instalments: ')
        displayMessage(f'Number of instalments is:  {number_of_instalments}')
        return  # TODO: trzeba by coś zwracał

    def performActionToWidthraw(self):
        amount = getAmount('Provide amount: ')
        self.account.account_history.append(amount)
        self.account.withdraw(amount)
        self.file_manager.save(self.account)
        displayMessage(f'Current balance {self.account.readAccountBalance()}, withdraw {amount}')

    def performActionToDeposit(self):
        amount = getAmount('Provide amount: ')
        self.account.account_history.append(amount)
        self.account.deposit(amount)
        self.file_manager.save(self.account)
        displayMessage(f'Current balance {self.account.readAccountBalance()}, deposit {amount}')

    def readAccountBalance(self):
        return self.account.readAccountBalance()

    def performActionToReviewAccountHistory(self):
        # TODO: distinguish income/outcome
        displayMessage(f'History of your account: {self.account.reviewAccountHistory()}')

    def performActionToTerminate(self):
        displayMessage('You have successfully terminated all actions')

    def performFileOperation(self, message):
        if getClientAction(message):
            self.file_manager.read()

        elif getAmount(message):
            self.file_manager.save()

    def performInitiateLongTermDeposit(self):
        amount = getAmount('Provide long term deposit amount: ')
        self.account.initiateLongTermDeposit(amount)
        self.file_manager.save(self.account)
        displayMessage(
            f'Current balance {self.readAccountBalance()}, long term deposit amount {amount},deposit balance {self.account.getDepositAmount()}')
