print("При покупке более 3-х билетов вы получаете скидку 10%")
ticket = int(input("Введите количество билетов:"))
ages = []
for a in range(ticket):
    ages.append(int(input("Введите возраст того, кому покупаете билет:")))
summ = 0
for age in ages:
    if age < 18:
        price = 0
        print ("Цена билета = ", price)
    elif age <= 25 and age >= 18:
        price = 990
        summ += price
        print ("Цена билета = ", price)
    elif age > 25:
        price = 1390
        summ += price
        print ("Цена билета = ", price)
print(summ if ticket <= 3 else summ*0.9, "- сумма к оплате")


