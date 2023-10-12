# ATM Application

Account_kaan = {
    "name": " Kaan ",
    "account_no": "1234",
    "balance" : 3000,
    "Addition_account": 2000
}

Account_Joe = {
    "name": "Joe",
    "account_no": "12141234",
    "balance" : 2000,
    "Addition_account": 1000
}

def withdraw(account, amount):
    print(f'Hello{account["name"]}')

    if account["balance"] >= amount:
        account["balance"] -= amount
        print("you can withdraw your money")
        learn_balance(account)

    else:
        total_money = account['balance'] + account['Addition_account']

        if total_money >= amount:
            print("you can withdraw but you have to use addition account")
            learn_addition_balance(account)
            accessto_additionalaccount = input("do you want to use your addition account (y/n)")
            
            if accessto_additionalaccount == "y":
                balance = account["balance"]

                amount_to_be_used_in_additional_account = amount - account["balance"]
                account["balance"] = 0
                account["Addition_account"] -= amount_to_be_used_in_additional_account
                print("you can withdraw")
                learn_addition_balance(account)


            else:
                print(f'There is{account["balance"]} dollars in your account number {account["account_no"]}')

        else:
            print("insufficient funds")
            learn_balance(account)

def learn_balance(account):
    print(f"You have {account['balance']} dollars in your account number: {account['account_no']}")

def learn_addition_balance(account):
    print(f"You have {account['Addition_account']} dollars in your addition account number: {account['account_no']}")

learn_balance(Account_kaan) # printing = " You have 3000 dollars in your account number: 1234 "
print("*****************************")
withdraw(Account_kaan,3000) # printing = " You have 0 dollars in your account number: 1234 " updating the balance
print("*****************************")
withdraw(Account_kaan,2000) # printing this first  = " do you want to use your addition account (y/n)"
# and than printing this " you can withdraw " because we have enough money to withdraw "
# and at the last print we called function named learn_addition_balance() and we can see our addition account balance