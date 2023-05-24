# 8. Запросите у пользователя стоимость покупки в $ и размер скидки в %.
# Посчитайте, какую сумму он должен заплатить на кассе и выведите эту информацию в удобном для чтения виде, с двумя знаками после запятой.
cost = input("Enter the cost of the product: $")
discount = input("Enter the current discount: %")
cost = int(cost)
discount = int(discount)
final_cost = cost - (cost * discount / 100)
form = "You have to pay: $%.2f" 
result = form % final_cost
print(result)
