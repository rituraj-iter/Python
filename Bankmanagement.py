import pickle
import os
import pathlib


class Account:
    account_number = 0
    name = ""
    balance_amount = 0
    account_type = ""

    def account_creation(self):
        self.account_number = int(input("Enter the account number\t"))
        self.name = input("Enter the account holder name\t")
        self.account_type = input("Enter the type of account\t")
        self.balance_amount = int(input("Enter the opening balance amount\t"))
        print("Account Created")

    def account_modification(self):
        print("Account Number\t", self.account_number)
        self.name = input("Modify Account Holder Name\t")
        self.account_type = input("Modify type of Account\t")

    def view_account(self):
        print("Account Number\t", self.account_number)
        print("Account Holder Name\t", self.name)
        print("Type of Account\t", self.account_type)
        print("Balance\t", self.balance_amount)

    def amount_deposition(self, amount):
        self.balance_amount = self.balance_amount + amount

    def amount_withdrawn(self, amount):
        self.balance_amount = self.balance_amount - amount

    def show(self):
        print(self.account_number, " ", self.name, " ", self.account_type, " ", self.balance_amount)

    def return_account_number(self):
        return self.account_number

    def return_account_holder_name(self):
        return self.name

    def return_account_type(self):
        return self.account_type

    def return_balance(self):
        return self.balance_amount


def intro():
    print("\t\t\t\tBANK MANAGEMENT SYSTEM\t\t\t\t")


def create_account():
    account = Account()
    account.account_creation()
    accounts_file(account)


def display_account_holders():
    file = pathlib.Path("accounts.data")
    if file.exists():
        prefile = open('accounts.data', 'rb')
        list = pickle.load(prefile)
        for item in list:
            print(item.account_number, " ", item.name, " ", item.account_type, " ", item.balance_amount)
        prefile.close()
    else:
        print("No accounts are currently availabe")


def balance_enquiry(number):
    file = pathlib.Path("accounts.data")
    if file.exists():
        prefile = open('accounts.data', 'rb')
        list = pickle.load(prefile)
        prefile.close()
        found = False
        for item in list:
            if item.account_number == number:
                print("Your account Balance is\t", item.balance_amount)
                found = True
    else:
        print("No data found")
    if not found:
        print("No data exists")


def deposit_and_withdraw(number1, number2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        prefile = open('accounts.data', 'rb')
        list = pickle.load(prefile)
        prefile.close()
        os.remove('accounts.data')
        for item in list:
            if item.account_number == number1:
                if number2 == 1:
                    amount = int(input("Enter the amount to be deposited\t"))
                    item.balance_amount = item.balance_amount + amount
                    print("New Balance\t",item.balance_amount)
                elif number2 == 2:
                    amount = int(input("Enter the amount to be withdrawn\t"))
                    if amount <= item.balance_amount:
                        item.balance_amount = item.balance_amount - amount
                        print("New Balance\t",item.balance_amount)
                    else:
                        print("Insufficient balance")

    else:
        print("No data found")
    newfile = open('newaccounts.data', 'wb')
    pickle.dump(list, newfile)
    newfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def delete_account(number):
    file = pathlib.Path("accounts.data")
    if file.exists():
        prefile = open('accounts.data', 'rb')
        previous_list = pickle.load(prefile)
        prefile.close()
        new_list = []
        for item in previous_list:
            if item.account_number != number:
                new_list.append(item)
        os.remove('accounts.data')
        newfile = open('newaccounts.data', 'wb')
        pickle.dump(new_list, newfile)
        newfile.close()
        os.rename('newaccounts.data', 'accounts.data')
        print("\tClosed Successfully")

def modify_account(number):
    file = pathlib.Path("accounts.data")
    if file.exists():
        prefile = open('accounts.data', 'rb')
        previous_list = pickle.load(prefile)
        prefile.close()
        os.remove('accounts.data')
        for item in previous_list:
            if item.account_number == number:
                item.name = input("Enter the account holder new name\t")
                item. account_type = input("Enter the account type which you want to be\t")

        newfile = open('newaccounts.data', 'wb')
        pickle.dump(previous_list, newfile)
        newfile.close()
        os.rename('newaccounts.data', 'accounts.data')
        print("\tModified Successfully")

def accounts_file(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        prefile = open('accounts.data', 'rb')
        previous_list = pickle.load(prefile)
        previous_list.append(account)
        prefile.close()
        os.remove('accounts.data')
    else:
        previous_list = [account]
    newfile = open('newaccounts.data', 'wb')
    pickle.dump(previous_list, newfile)
    newfile.close()
    os.rename('newaccounts.data', 'accounts.data')


ch = ''
intro()

while ch != 8:
    print("\tMAIN MENU\t")
    print("\t1. NEW ACCOUNT\t")
    print("\t2. DEPOSIT AMOUNT\t")
    print("\t3. WITHDRAW AMOUNT\t")
    print("\t4. BALANCE ENQUIRY\t")
    print("\t5. ALL ACCOUNT HOLDER LIST\t")
    print("\t6. CLOSE AN ACCOUNT\t")
    print("\t7. MODIFY AN ACCOUNT\t")
    print("\t8. EXIT\t")
    ch = input()

    if ch == '1':
        create_account()
    elif ch == '2':
        number = int(input("\tEnter The account number\t"))
        deposit_and_withdraw(number, 1)
    elif ch == '3':
        number = int(input("\tEnter The account number\t"))
        deposit_and_withdraw(number, 2)
    elif ch == '4':
        number = int(input("\tEnter The account number\t"))
        balance_enquiry(number)
    elif ch == '5':
        display_account_holders();
    elif ch == '6':
        number = int(input("\tEnter The account number\t"))
        delete_account(number)
    elif ch == '7':
        number = int(input("\tEnter The account number\t"))
        modify_account(number)
    elif ch == '8':
        print("\tThanks a lot hope you like the service\t")
        break
    else:
        print("Wrong input")
