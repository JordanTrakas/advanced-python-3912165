# Example file for Advanced Python by Joe Marini
# Itertools: count, cycle, accumulate


import itertools
from datetime import datetime, timedelta

# names = ["Joe", "Jane", "Jim"]

# cycle iterator can be used to cycle over a collection infinitely
# cycler = itertools.cycle(names)
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))

# use count to create a simple counter
# counter = itertools.count(100, 10)
# print(next(counter))
# print(next(counter))
# print(next(counter))

# accumulate creates an iterator that accumulates values
vals = [10,20,30,40,50,40,30]
acc = itertools.accumulate(vals, max)
print(list(acc))

# print(next(acc))
# print(next(acc))
# print(next(acc))

# amortize a loan over a set number of payments for a 2000 loan at 18.5%
# payments = [480 for i in range(10)]
# update = lambda balance, payment: round(balance * 1.04) - payment
# balances = itertools.accumulate(payments, update, initial=12_000)
# print(list(balances))

principal_amt = 8779.73
apr_percent = 18.52
payment_amt = 478.79
months_paid = 22
current_time = datetime.now()
maturation_time = (current_time + timedelta(weeks=4*months_paid)).strftime("%m-%Y")

rate = [1 + (apr_percent*0.01/12) for _ in range(months_paid)]
current = lambda current_item, running_total: current_item * running_total - payment_amt
balances = itertools.accumulate(rate, current, initial=principal_amt)
balances_list = list(balances)

print(f"Account maturation month: {maturation_time}")
if balances_list[len(balances_list)-1] <= 0:
    print("Account has matured! Congratulations! You now own your car.")
elif balances_list[len(balances_list)-1] > 0:
    print(f"Account has not been matured yet.")
