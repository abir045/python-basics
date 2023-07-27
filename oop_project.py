from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withDraw(5000)
Dave.withDraw(10)


Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)


Jim = interestRewardAcct(1000, "jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Dave)

# Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()
Blaze.deposit(100)


Blaze.transfer(10000, Sara)
Blaze.transfer(1000, Sara)
