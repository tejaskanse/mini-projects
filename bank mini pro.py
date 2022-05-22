#parent class
class User:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def display(self):
        print("Personal Details")
        print("Name: ",user_name)
        print("Age: ",user_age)
        print("Gender: ",user_gender)
        
user_name=input('Enter your name: ')
user_age=input('Enter your age: ')
user_gender=input('Enter your Gender: ')
u1=User(user_name,user_age,user_gender)

while(True):
    print('Do you wish to carry out available functions')
    user_wish=input("Enter 'y' for yes : ")
    if user_wish.lower()!='y':
        break
    else:
        print("Available functions")
        break
        
#child class 
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance=0
        
#deposit func
    def deposit(self,user_depo):
        self.amount=user_depo
        self.balance=self.balance+self.amount
        print("Account Balance has been updated Rs ",self.balance)
        
#withdraw func
    def withdraw(self,user_wdraw):
        self.amount=user_wdraw
        if self.amount>self.balance:
            print("Insufficient Balance:Available Balance is Rs ",self.balance)
        else:
            self.balance=self.balance-self.amount
            print("Available Balance is Rs ",self.balance)

#view balance 
    def view_balance(self):
        self.display()
        print("Account Balance is Rs ",self.balance)
    
b1=Bank(user_name,user_age,user_gender)

while(True):
    user_input=input('''"w" for withdraw,"d" for deposit and "b" for balance: ,"q" for quit: ''')
    if user_input=='d':
        user_depo=int(input('Enter amount you want to deposit: '))
        b1.deposit(user_depo)
    if user_input=='w':
        user_wdraw=int(input('Enter amount you want to withdraw: '))
        b1.withdraw(user_wdraw)
    if user_input=='b':
        b1.view_balance()
    if user_input=='q':
        break
