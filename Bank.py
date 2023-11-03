import random
import datetime

class User:
    def __init__(self, name, email, address ,account_type, password) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.__password = password

    def get_pass(self):
        return self.__password
    
    def set_pass(self, password):
        self.__password = password



class Customer(User):
    def __init__(self, name, email, address, account_type, password, account_number, balance, loan = 2) -> None:
        super().__init__(name, email, address, account_type, password)
        self.account_number = account_number
        self.balance = balance
        self.loan = loan

class Admin(User):
    def __init__(self, name, email, address, account_type, password, admin_no) -> None:
        super().__init__(name, email, address, account_type, password)
        self.admin_no = admin_no

class Bank:
    allow_lone = True

    def __init__(self) -> None:
        self.customers = {}
        self.admins = {}
        self.transaction = {}
        self.history = []
        self._bank_balance = 500000
        self._bank_loan_given = 0
    
    # user method 
    def show_all_user(self):
        for c in self.customers:
            print(f'user-name: {self.customers[c].name} a/c no: {c} balance: {self.customers[c].balance}')

    def add_customer(self, customer):
        account_number = customer.account_number
        self.customers[account_number] = customer
        time = datetime.datetime.now()
        self.transaction[account_number] = ( (f'a/c created at', time, f'USER name {customer.name}', f' balance :{customer.balance}') )
   
    def check_ac(self, ac):
        if ac in self.customers: return True
        else : return False

    def check_pwd(self, pwd, acn):
        customer = self.customers.get(acn)
        if customer and pwd == customer.get_pass():
            return True
        else: return False

    def check_balance(self, ac):
        customer = self.customers.get(ac)
        return customer.balance
        
    def deposit(self, ac, amount):
        customer = self.customers.get(ac)
        customer.balance += amount
        print(f'Congratulations your balance is now {customer.balance}')
        self._bank_balance += amount
        time = datetime.datetime.now()
        self.transaction[ac] = ( (f'deposited at', time, f'USER name {customer.name}', f' balance :{customer.balance}') )
        self.history.append((ac, f'deposited at', time, f'USER name {customer.name}', f' balance :{customer.balance}') )

    def withdraw(self, ac, amount):
        if self._bank_balance < amount:
            print('sorry bank is bankrupt')
        else:
            customer = self.customers.get(ac)
            if customer.balance < amount:
                print('Withdrawal amount exceeded')
            else:
                customer.balance -= amount
                print(f'Congratulations your balance is now {customer.balance}')
                self._bank_balance -= amount
                time = datetime.datetime.now()
                self.transaction[ac] = ( (f'withdrawn at', time, f'USER name {customer.name}', f' balance :{customer.balance}') )
                self.history.append(( ac, f'withdrawn at', time, f'USER name {customer.name}', f' balance :{customer.balance}') )

    def transaction_history(self, ac):
        for h in self.transaction[ac]:
            print(h)

    def show_transaction_history(self, ac):
        for t in self.history:
            if t[0] == ac:
                print(t)

    def take_loan(self,ac, amount):
        if self._bank_balance < amount:
            print('sorry bank is bankrupt')
        else:
            customer = self.customers.get(ac)
            if  customer.loan > 0:
                customer.loan -= 1
                self._bank_balance -= amount
                customer.balance += amount
                self.history.append((ac, f'took lone at', time, f'USER name {customer.name}', f' balance :{customer.balance}') )
                print(f'congratulation you got the loan your balance is {customer.balance}')
            else :
                print('you cant have the loan you already took 2x time')
    


# admin method
    def stop_loan(self, c):
        if c == 0:
            Bank.allow_lone = False
        elif c == 1:
            Bank.allow_lone = True


    def add_admin(self, admin):
        account_number = admin.admin_no
        self.admins[account_number] = admin

    def check_admin_ac(self, ac):
        if ac in self.admins: return True
        else : return False

    def check_admin_pwd(self, pwd, acn):
        admin = self.admins.get(acn)
        if admin and pwd == admin.get_pass():
            return True
        else: return False

    def delete_user(self, ac):
        if ac in self.customers:
            del self.customers[ac]
            print(f"Customer account with account number {ac} has been deleted.")
        else:
            print(f"Customer account with account number {ac} does not exist.")


    


the_bank = Bank()
# user = Customer('a', 'email', 'address', 'account_type', 'psd', 1234, 0)
# the_bank.add_customer(user)
# print(the_bank.customers[1234].balance)
# print(the_bank.customers.get(1234).get_pass())
# the_bank.show_all_user()

def make_user():
        # print('please write your name :')
        # name = input()
        # print('enter your email')
        # email = input()
        # print('your address')
        # address = input()
        # print('your account type please enter 1 for Savings  and 2 for current')
        # while True:
        #     at = input()
        #     if at == '1':
        #         account_type = 'Savings'
        #         break
        #     elif at == '2':
        #         account_type = 'current'
        #         break
        #     else:
        #         print('please enter 1 or 2 ')
        print('enter password')
        password = input()
        while True:
            account_number = random.randint(1, 1000)
            if(the_bank.check_ac(account_number) == False):
                break
        # user = Customer(name, email, address, account_type, password, account_number, 0)
        user = Customer("name", "email", "address", "account_type", password, account_number, 0)
        the_bank.add_customer(user)
        print(f"Congratulations you made an account. \nyour account number is {user.account_number} \n")



def make_admin():
        # print('please write your name :')
        # name = input()
        # print('enter your email')
        # email = input()
        # print('your address')
        # address = input()
        # print('your account type please enter 1 for Savings  and 2 for current')
        # while True:
        #     at = input()
        #     if at == '1':
        #         account_type = 'Savings'
        #         break
        #     elif at == '2':
        #         account_type = 'current'
        #         break
        #     else:
        #         print('please enter 1 or 2 ')
        print('enter password')
        password = input()
        while True:
            admin_number = random.randint(1, 1000)
            if(the_bank.check_admin_ac(admin_number) == False):
                break
        # user = Customer(name, email, address, account_type, password, account_number, 0)
        admin = Admin("name", "email", "address", "account_type", password, admin_number)
        the_bank.add_admin(admin)
        print(f"Congratulations you made an account as an admin. \nyour account number is {admin.admin_no} \n")


#user function
def user_login():
    print('please enter your account number:')
    while True:
        try:
            ac = input()
            if ac == 'exit':
                break
            ac_number= int(ac)
            if the_bank.check_ac(ac_number):
                break
        except:
            print("Please enter valid a/c number.")

    print(f'welcome {the_bank.customers[ac_number].name}  please inter your password: ')
    pwd = input()
    if the_bank.check_pwd(pwd, ac_number):
        return ac_number
    else: return False
    


#admin function

def admin_login():
    print('please enter your admin account number:')
    while True:
        try:
            ac = input()
            if ac == 'exit':
                break
            ac_number= int(ac)
            if the_bank.check_admin_ac(ac_number):
                break
        except:
            print("Please enter valid a/c number.")

    print(f'welcome {the_bank.admins[ac_number].name}  please inter your password: ')
    pwd = input()
    if the_bank.check_admin_pwd(pwd, ac_number):
        return ac_number
    else: return False
    





# user = Customer('a', 'email', 'address', 'account_type','pass', 123, 0, 0)
# the_bank.add_customer(user)
# # print(the_bank.admins.get(123).get_pass())
# the_bank.take_loan(123, 30)
# print(the_bank.customers[123].name)
# the_bank.show_all_user()
# Bank.allow_lone = False
# print(Bank.allow_lone)















while True:
    print('\n\nplease enter \n1 to make a user or admin account \n2 to login \ntype "exit" to close')
    s = input()
    if s == 'exit':
        break
    if s == '1':
        print('enter \n1 for user \n2 for admin')
        muser = input()
        if(muser == '1'):
            make_user()
        else:
            make_admin()

    elif s == '2':
        print('enter \n1 for customer login \n2 for admin login')
        while True:
            a = input()
            if a == '1' or a == '2' or a == 'exit':
                break
            else:print('enter \n1 for customer login \n2 for admin login')

        if a == '1':
            #user 
            ac_number = user_login()
            if(ac_number):
                while True:
                    
                    print('enter \n1 to deposit, \n2 to withdraw, \n3 to check balance, \n4 to see transaction history, \n5 to take a loan, \n6 to transfer balance')
                    while True:
                        a = input()
                        if a == '1' or a == '2' or a == '3' or a == '4'  or a == '5' or a == '6':
                            break
                        else: print('enter valid number')
                    #deposit
                    if a == '1':
                        while True:
                            try:
                                print('enter deposit amount')
                                amount = int(input())
                                break
                            except:
                                print('please enter a valid number')
                        the_bank.deposit(ac_number, amount)
                    
                    #withdraw
                    elif a == '2':
                        while True:
                            try:
                                print('enter withdraw amount')
                                amt = int(input())
                                break
                            except:
                                print('please enter a valid number')
                        the_bank.withdraw(ac_number, amt)
                    #check available balance
                    elif a == '3':
                        bln = the_bank.check_balance(ac_number)
                        print('your balance: ',bln)
                    #transaction history
                    elif a == '4':
                        the_bank.show_transaction_history(ac_number)
                        
                    #take loan
                    elif a == '5':
                        if Bank.allow_lone == False:
                            print('sorry lone are not allowed at this moment')
                        else:
                            while True:
                                try:
                                    print('enter lone amount')
                                    amt = int(input())
                                    break
                                except:
                                    print('please enter a valid number')
                            the_bank.take_loan(ac_number, amt)
                    #transfer balance
                    elif a == '6':
                        while True:
                            try:
                                print('enter the account where you want to send money')
                                to_ac = int(input())
                                if the_bank.check_ac(to_ac) :
                                    break
                                else: print("Account does not exist")
                            except:
                                print('please enter a valid a/c number')

                        while True:
                            try:
                                print('enter amount you want to send')
                                
                                am = input()
                                if am == 'exit':
                                    break
                                amt = int(am)
                                if amt <= the_bank.check_balance(ac_number) :
                                    break
                                else: print('you dont have enough money')
                            except:
                                print('please enter a valid number')
                        the_bank.deposit(to_ac, amt)


                    print('would you like to continue: enter \n0 else enter \nexit')
                    b = input()
                    if b == 'exit':
                        break

        elif a == '2':
            #admin
            ad_number = admin_login()
            if ad_number:
                while True:

                    print('enter \n1 to make user account \n2 to see all user \n3 to check bank total balance \n4 to check total loan given \n5 to turn of giving loan \n6 to delete account \ntype exit to exit')
                    ai = input()
                    if ai == 'exit':
                        break
                    if ai == '1':
                        # make user
                        make_user()
                    elif ai == '2':
                        #see all user ac
                        the_bank.show_all_user()
                        print('')

                    elif ai == '3':
                        # check total balance
                        print(the_bank._bank_balance)
                        print('')

                    elif ai == '4':
                        #check loan
                        print(the_bank._bank_loan_given)

                    elif ai == '5':
                        #turn off loan
                        while True:
                                try:
                                    print('enter \n0 to turn off all loan \n1 to allow all loan')
                                    lone = int(input())
                                    break
                                except:
                                    print('please enter a valid number')
                        the_bank.stop_loan(lone)


                        
                    elif ai == '6':
                        #delete account
                        while True:
                            try:
                                print('enter the account you want to delete \ntype exit if you dont want to ')
                                u_input = input()
                                if u_input == 'exit':
                                    break
                                ac = int(u_input)
                                break
                            except:
                                print('please enter a valid number')
                        the_bank.delete_user(ac)
                        
