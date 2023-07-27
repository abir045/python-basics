class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(
            f"\nAccount '{self.name}'  created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"]\nAccount '{self.name}' balance = ${self.balance: .2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry , account '{self.name} only has a balance of ${self.balance}")

    def withDraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw complte.")
            self.getBalance()

        except BalanceException as error:
            print(f'\n Withdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n********\n\n Beginning Transfer 🚀')
            self.viableTransaction(amount)
            self.withDraw(amount)
            account.deposit(amount)
            print('\n Trnasfer complete ✅ \n\n************')

        except BalanceException as error:
            print(f'\nTransfer interrupted ❌  {error}')


class interestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complete")
        self.getBalance()


class SavingsAcct(interestRewardAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withDraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\n Withdraw completed")
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdraw interrupted: {error}')
