from num2words import num2words

# Запит користувача на введення числа (ціле число)
num = input("Введіть число: ")

# Виведення числа користувача у текстовому вигляді
print("Ваше число: " + num2words(int(num), lang='uk'))
