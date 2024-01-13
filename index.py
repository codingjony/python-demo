import datetime
import os


def get_current_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


acdata = {1: [1, 1000, []], 2: [2, 2000, []]}


def deposit(acc, amt):
    acdata[acc][1] += amt
    rec = f"{get_current_datetime()} Desposit           +${amt}   Rem : ${acdata[acc][1]}"
    acdata[acc][2].append(rec)
    print("Amount Added Succesfully ")

    print()


def withdraw(acc, amt):
    acdata[acc][1] -= amt
    rec = f"{get_current_datetime()} Withdraw           -${amt}   Rem : ${acdata[acc][1]}"
    acdata[acc][2].append(rec)
    print("Amount Withdrawn ")

    print()


def transfer(x, acc, amt):
    if x in acdata:
        acdata[acc][1] -= amt
        acdata[x][1] += amt

        rec1 = f"{get_current_datetime()} Transfer to {x}     -${amt}   Rem : ${acdata[acc][1]}"
        rec2 = f"{get_current_datetime()} Transfer from {acc} +${amt}   Rem : ${acdata[x][1]}"

        acdata[acc][2].append(rec1)
        acdata[x][2].append(rec2)

        print("Transfer Succesfull ")

    else:
        print("Account Not Found")

    print()


def tot_bal():
    sum = 0
    keys = acdata.keys()
    for key in keys:
        sum += acdata[key][1]

    return sum


def clr(n=0):
    if n == 1:
        press = input("Press Any key to continue --->")
    os.system('cls')


clr()
while True:
    print("1.Account Details ")
    print("2.Create Account ")
    print("3.All Accounts ")
    print("0.Exit")

    q = int(input("------>"))

    if q == 1:

        acc = int(input("Enter Account Number = "))
        if acc in acdata and int(input("Enter Pin = ")) == acdata[acc][0]:
            os.system('cls')
            while True:
                print("1.Check Balance ")
                print("2.Deposit ")
                print("3.Withdraw ")
                print("4.Transanction History ")
                print("5.Transfer ")
                print("0.Exit")
                n = int(input("----->"))

                if n == 1:
                    print(f"Your Balance = {acdata[acc][1]}")
                    print()

                    clr(1)

                if n == 2:
                    amt = int(input("Enter Amount = $"))
                    deposit(acc, amt)

                    clr(1)

                if n == 3:
                    amt = int(input("Enter Amount = $"))
                    withdraw(acc, amt)

                    clr(1)

                if n == 4:
                    for trans in acdata[acc][2]:
                        print(trans)
                    print()

                    clr(1)

                if n == 5:
                    x = int(input("Recievers Account Number = "))
                    amt = int(input("Enter Amount = $"))
                    transfer(x, acc, amt)

                    clr(1)

                if n == 0:
                    clr()
                    break

        else:
            print("Account Not Found or Pin may be wrong")
            clr(1)

    if q == 2:

        n = int(input("Enter Account Number: "))
        p = int(input("Enter PIN: "))
        acdata[n] = [p, 0, []]

        print("Account Created Succesfully ")
        print()

        clr(1)

    if q == 3:
        print(f"Total Balance = {tot_bal()}")

        keys = acdata.keys()
        print(f"\nAc/No          Balance")
        for key in keys:
            print(f"{key}              {acdata[key][1]}")

        print()

        clr(1)

    if q == 0:
        clr()
        break
