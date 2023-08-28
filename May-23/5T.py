# 5. Цензура. Запросите у пользователя слово и выведите зацензуренное слово, в котором все буквы кроме первой и последней заменены звёздочками '*'.
# Подсказка: используйте функцию len(), операцию повторения строк и доступ по индексу.
user_in_str = input("Enter there your word: ")
words_len = len(user_in_str)
symb_cut = words_len - 2 
stars = symb_cut * "*" 
words_symbs1 = user_in_str[:1]
words_symbs2 = user_in_str[-1:]
result = words_symbs1 + stars + words_symbs2
print("This is your censored word: ", result)

