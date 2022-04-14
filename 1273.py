per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
money = float(input("Введите сумму под процент: "))
deposit=[]
for key in per_cent:deposit.append(money*per_cent[key]/100)
print("Полученный процент в каждом банке:", deposit)
print("Максимально возможный процент:", max(deposit))