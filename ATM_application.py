class CheckPin:
    def verify(self,pin):
        if pin==1111 or pin==2222 or pin==3333:
            return True
        else:
            return False

class Balance:
    def __init__(self):
        self.bal=2000

    def getBalance(self):
        return self.bal

class Transaction:
    b=Balance()
    def process(self,amt):
        pass


class Withdraw(Transaction):
    def process(self,amt):
        if amt <= self.b.bal:
            print("amount withdrawn is ",amt)
            self.b.bal = self.b.bal - amt
            print("Remaining balance is ",self.b.getBalance())
            print("transaction successful....")
        else:
            print("insufficient balance")

class Deposit(Transaction):
    def process(self,amt):
        print("amount deposit is ",amt)
        self.b.bal = self.b.bal + amt
        print("Balance is ",self.b.getBalance())

class ATM:
    count=0
    while True:
        pin = int(input("enter pin number"))
        
        if pin>=1000 and pin<=9999:
            cpn = CheckPin()
            k = cpn.verify(pin)
            if k:
                print("Enter your choice")
                print("1. Withdraw\n2.Deposit")
                ch = int(input())
                if ch==1:
                    amt = int(input("Enter an amount for withdrawal"))
                    if amt>0 and amt%100==0:
                        wd = Withdraw()
                        wd.process(amt)
                        break
                elif ch==2:
                    amt = int(input("Enter an amount to deposit"))
                    if amt>0 and amt%100==0:
                        de=Deposit()
                        de.process(amt)
                        break
                    else:
                        print("invalid amount")
                        break

                else:
                    print("Invalid Choice")

            else:
                print("Invalid pin")
                count = count+1

        else:
            print("incorrect pin")
            count = count+1
            if count==3:
                print("blocked")
                break











                        
