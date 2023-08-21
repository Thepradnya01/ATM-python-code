class ATM:                              
    def __init__(self):
        self.__pin                              #private members, so that no-one can change the pin and balance manually outside the class
        self.__balance=0
        self.menus()

    def menus(self):
        choice=int(input('''Enter your choice from following:
                        1.Create PIN
                        2.Change PIN
                        3.Check Balance
                        4.Deposit
                        5.Credit
                        6.EXIT
                '''
              ))
        if(choice==1):
            self.create_pin()
        elif(choice==2):
            self.change_pin()
        elif(choice==3):
            self.check_balance()
        elif(choice==4):
            self.deposit()
        elif(choice==5):
            self.credit()
        elif(choice==6):
            print("Thank YOU!!! Visit again")
        else:
            print("ENTER VALID CHOICE")

    def validate_pin(self,entered_pin):
        if(self.__pin==entered_pin):                        # I am using this function multiple times in a code to validate the pin
            return True
        else:
            return False
    
    def create_pin(self):                           #creates the PIN for the first time
        self.__pin=int(input("Enter your 4 digit pin: "))
        
    def change_pin(self):
        x=int(input("Enter your old PIN"))          #function to change the pin
        if(self.validate_pin(x)):
            self.__pin=int(input("Enter your new PIN: "))
            print("PIN changed successfully")
        else:
            print("Wrong PIN entered")
        
        
    def check_balance(self):                        #check balance
        x=int(input("ENter your PIN"))
        if(self.validate_pin(x)):
            print("Available Balance: ",self.__balance)
        else:
            print("Wrong PIN entered")
    def deposit(self):                              #for deposit of money
        x=int(input("ENter your PIN"))
        if(self.validate_pin(x)):
            amount=int(input('Enter the amount'))
            if(self.__balance>=amount):
                print("collect your cash")
                self.__balance=self.__balance-amount
            else:
                print("Insufficient Balance")
                       
        else:
            print("Wrong PIN entered")

    def credit(self):                               #to credit money in the account, we are not validating PIN here
        amount=int(input('Enter the amount'))
        self.__balance=self.__balance+amount
        print("credited successfully... Available Balance = ", self.__balance)
            
            
        
            

    
    
        
            
        
