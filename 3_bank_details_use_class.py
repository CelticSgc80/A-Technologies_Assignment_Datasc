#Create a class Bank:
class Bank:

    def __init__(self, Customername, ac_no, credit,debit, total_balance):
        self.customername = Customername
        self.ac_no = ac_no
        self.credit=credit
        self.debit=debit
        self.total_balance= total_balance

    def printdetails(self):
        print('Name:',self.customername,'. Account No:',self.ac_no,
              '. Credit Amount:',self.credit,'. Debit Amount:',self.debit,
              '. Total Balance:',self.total_balance)


rohit= Bank("Rohit Chatterjee", 10002568945,5000,1000,50000)
rohon= Bank("Rohon Pal", 10002565897,4000,2500,78000)
soumodip= Bank("Soumodip Banerjee", 10002575297,10000,4890,102560)
abhijit= Bank("Abhjit Chowdhury", 10002558936,7000,6550,95500)

ac=int(input('Enter The account No: '))
if(ac==10002568945):
    rohit.printdetails()
elif(ac==10002565897):
    rohon.printdetails()
elif(ac==10002575297):
    soumodip.printdetails()
elif(ac==10002558936):
    abhijit.printdetails()
else:
    print('Account Details Invalid')



