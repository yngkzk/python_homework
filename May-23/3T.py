# 3. Сокращения. Запросите у пользователя слово и напечатайте сокращение для этого слова, состоящее из двух первых букв, тире и двух последних букв. 
# Например, для слова "обсерватория" должно получиться "об-ия".
# Подсказка: используйте срезы для решения задачи.
user_in = input("Enter there your word: ")
cut1 = user_in[:2]
cut2 = user_in[-2:]
result = cut1 + "-" + cut2
print("This is your cut word: ", result)