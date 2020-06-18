
# CX Programming Club
# Week 03
# lariasca

income = float(input("Enter your montly income: "))
expense_c = float(input("Enter the amount of monthly purchases: "))
expense_c = int(expense_c)

sum_exp = 0
money_left = 0
dots = 0
space = 0

exp = input("Enter all concepts and value of expenses in format 'concept,value': ")

split = exp.split(",")

concepts = split[0:len(split):2]
expenses = split[1:len(split):2]

for i in range(len(expenses)):
    sum_exp += float(expenses[i])

money_left = income - sum_exp
space = 50 - (len(str(money_left)) + 10)

print(f"""
{'#'*16}Expense Calculator{'#'*16}
Monthly income: {income}
Monthly purchases: {expense_c}""")

for i in range(len(concepts)):
    print(f'Concept: {concepts[i]}')
    print(f'Amount: {expenses[i]}')

print(f"{'*'*18}Expense report{'*'*18}")

for i in range(len(concepts)):
    expenses[i] = float(expenses[i])
    dots = 50 - (len(str(concepts[i])) + len(str(expenses[i])))
    print(f"{concepts[i]}{'.'*dots}{expenses[i]}")

print(f"""
{'-'*50}
Money left{' '*space}{money_left}
""")
