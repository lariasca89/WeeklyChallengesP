# Weekly Challenge 08
# CX Programming Club
# lariasca

import WeeklyChallenge_Week08_lariasca.expenses.expense_convert as convert
import WeeklyChallenge_Week08_lariasca.open_image as image

print('''Select the initial currency (Just 3 letters code):\n
MXN.- Mexican Pesos
BRL.- Real Brasileño
ARS.- Peso Argentino
PEN.- Sol Peruano
EUR.- Euro\n''')

currency = input(">> ")
rate = convert.expense_rate(currency)
print(f"Exchange rate: 1 {currency} equals {rate} USD\n")
print("Please introduce items\n")

concept = []
amount = []
amount_usd = []
i = 0
items = True

while items:
    var1 = input(f"Concept {i+1}: ")
    concept.append(var1)
    var2 = int(input(f"Amount {i+1} ({currency}): "))
    amount.append(var2)
    reply = input("Do you want to add another item? (Yes/No): ")
    if reply == "Yes":
        i += 1
    else:
        items = False

# Perform math operations in order to build the expense report

amount_usd = convert.amount_convert(rate, amount)
suma_amount = sum(amount)
suma_amount_usd = sum(amount_usd)

print(f"\n{'*'*50}\n{'Expenses Report'.rjust(30,' ')}\n{'*'*50}\n")
print(f"{'Concept'.ljust(15,' ')}Amount ({currency}){'Amount (USD)'.rjust(20,' ')}\n{'='*50}")

for x in range(len(concept)):
    print(f"{concept[x].ljust(20,' ')}{amount[x]}{str(amount_usd[x]).rjust(28,' ')}")

print(f"\n{'-'*50}\n{'Totals:'.ljust(20,' ')}{suma_amount} {currency}{str(suma_amount_usd).rjust(24,' ')} USD")

# Print image of compliance
if suma_amount_usd <= 100:
    compliance = True
    image.image_display(compliance)
else:
    compliance = False
    image.image_display(compliance)
