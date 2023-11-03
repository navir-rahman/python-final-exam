import random

class User:
    def __init__(self, name, email, address ,account_type, password) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.__password = password


class Customer(User):
    def __init__(self, name, email, address, account_type, password, account_number, balance) -> None:
        super().__init__(name, email, address, account_type, password)
        self.account_number = account_number
        self.balance = balance

class Admin(User):
    def __init__(self, name, email, address, account_type, password, admin_no) -> None:
        super().__init__(name, email, address, account_type, password)
        self.admin_no = admin_no

class Bank:
    def __init__(self) -> None:
        self.customers = []
        self.admins = []
        self._bank_balance = 0
        self._bank_loan_given = 0
    
    def add_customer(self, customer):
        self.customers.append(customer)

    def add_admin(self, admin):
        self.admins.append(admin)



def make_user():
        print('please write your name :')
        name = input()
        print('enter your email')
        email = input()
        print('your address')
        address = input()
        print('your account type please enter 1 for Savings  and 2 for current')
        while True:
            at = input()
            if at == '1':
                account_type = 'Savings'
                break
            elif at == '2':
                account_type = 'current'
                break
            else:
                print('please enter 1 or 2 ')
        print('enter password')
        password = input()
        account_number = random.randint(1, 1000000)
        # print('your deposit, minimum amount 500, you cant withdraw it you can withdraw it if you close your account')
        # while True:
        #     try:
        #         balance = int(input())
        #         if balance >= 500:
        #             break
        #         else:
        #             print('Please enter at least 500.')
        #     except:
        #         print("Please enter a valid number.")
        user = Customer(name, email, address, account_type, password, account_number, 0)
        print(f"Congratulations you made an account. \nyour account number is {user.account_number} \n\n\n")


while True:
    print('please enter 1 to make a user \ntype "exit" to close')
    a = input()
    if a == 'exit':
        break
    if a == '1':
        make_user()
    elif a == '2':

