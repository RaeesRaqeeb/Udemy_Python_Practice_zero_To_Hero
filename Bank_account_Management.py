from re import S


class BankAccount():

    def __init__(self, account_number,  Account_holder,balance):
        self.account_number=account_number;
        self.Account_holder=Account_holder;
        self.balance=balance;
        print("Information successfully saved")

    def deposit(self, amount):
        self.balance+=amount;
        print("\nAmount is successfully deposit\n")
    def with_draw(self, amount):
        self.balance-=amount;
    def get_balance(self):
        print(self.balance)
    

#main program
user_input=1
name=""
balance=0
while(1):
    print("******Simple Bank management system******\nEnter 0 to exit 1 to continue :\n")
    user_input=int(input())
    if(user_input==0):
        break
    user_input=int(input("\nEnter the account number:"))
    name=(input("Enter the name of the account holder:"))
    balance=int(input("Current Balance:"))
    Account1=BankAccount(user_input,name,balance)
    while(1):
        print("Want to do something like:\n1)Deposit amount\n2)WithDraw\n3)Current Balance\n4)exit\n")
        user_input=int(input("\nEnter you choice(1,2,3 or 4):"))
        if(user_input==1):
            user_input=int(input("\nHow much you want to deposite:"))
            Account1.deposit(user_input)
        elif(user_input==2):
            user_input=int(input("\nHow much you want to withdraw:"))
            Account1.with_draw(user_input)
        elif(user_input==3):
            print("\nYour current balacne is :",Account1.balance)
        elif(user_input==4):
            break
    


        


    

