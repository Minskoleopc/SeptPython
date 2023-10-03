

# program 1
#
# class Person:
#     country = "India"
#     def __init__(self):
#         self.firstName = "amol"
#         self.lastName = "rao"
#         self.age = 24
#
#     def displayName(self):
#         print(self.firstName + self.lastName)
#
# amol = Person()
# chinmay = Person()
# sarika = Person()
# class PersonB:
#     country = "India"
#     def __init__(self,fn,ln,ag):
#         self.firstName = fn
#         self.lastName = ln
#         self.age = ag
#
#     def displayName(self):
#         print(self.firstName+ self.lastName)
#
#     @classmethod
#     def updateCountry(cls,cntry):
#         PersonB.country = cntry
#
# PersonB.updateCountry("bharat")
# amolB = PersonB("amolB","raoB","34")
# amolC = PersonB("amolC","raoC","34")
# print(PersonB.country)
# print(PersonB.country)
# amolB.country = "nepal"
# print(amolB.country)


# program2


class BanK:
    def __init__(self,accName,accNo,bal):
        self.accName = accName
        self.accNo = accNo
        self.bal = bal
        self.transactions = []

    def withDrawl(self,amount):
        if self.bal > amount:
            self.bal = self.bal - amount
            self.transactions.append(-amount)
        else:
            print("insufficient balance")
        return self.bal

    def depsosit(self,amount):
        self.bal = self.bal + amount
        self.transactions.append(amount)
        return self.bal

    def lastFiveTransactions(self):
        return self.transactions[-5:]

chinmay  =  BanK("chinmay","123",10000000)
print(chinmay.withDrawl(10000))

chinmay.depsosit(10000)
chinmay.depsosit(10000)
chinmay.depsosit(100)
chinmay.depsosit(10000)
chinmay.depsosit(10)
chinmay.depsosit(10000)
chinmay.withDrawl(99)
print(chinmay.lastFiveTransactions())
























