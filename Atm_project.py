


class Atm:
    # make a constracture 
    def __init__(self):
        self.__pin = "7890"
        self.balance = 0

    
        self.manu()

    def manu(self):
        user_input= input('''
        hello, how would you like to proceed
        1. enter 1 to create pin
        2. enter 2 to deposit 
        3. enter 3 to withdrow 
        4. enter 4 show the balance 
        5. enter 5 to exit 

        ''')
        
        if user_input == "1":
            # print("create __pin ")
            self.create___pin()
        elif user_input =="2":
            # print("deposit")
            self.deposit()
        elif user_input == "3":
            # print("withdrow ")
           self.withdrow()
        elif user_input == "4":
            # print("amounts")
            self.show_balance()
        elif user_input == "5":
            # print("exits")
            self.exit()



    def create___pin(self):
        temp  = input("enter the old pin : ")
        if temp == self.__pin:
            self.__pin = input("enter the new pin : ")
            print("pin set seccusfully ")
        else:
            print("invalid old pin ")
        self.manu()


    def deposit(self):
        temp = input("enter the pin: ")
        if temp == self.__pin:
            amounts = int(input("enter the amount :"))
            self.balance = self.balance + amounts
            print("deposit succesful ")
        else:
            print("invalid pin ")
        
        
        self.manu()



    def withdrow(self):
        temp = input("enter the pin :")
        if temp == self.__pin:
            amounts = int(input("enter the amounts : "))
            if amounts < self.balance:
                self.balance = self.balance - amounts
            else:
                print("you have don't sufficient balance \n please enter the valid amount  ")
        else:
            print("invalid pin ")
        
        self.manu()
    

    def show_balance(self):
        temp = input("enter the pin : ")
        if temp == self.__pin:
            print("Total balance : ",self.balance)
        else:
            print("invalid pin ")
        
        self.manu()
        
    def exit(self):
        exit()


sbi = Atm()









