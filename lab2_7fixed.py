k = input("Введите k: ")
# Проверка входного значения
while not k.isdigit():
    k = input("Введите корректное k: ")
k = int(k)
f = open("lab2_f.txt", "r")
seq = f.read().strip()
kt = 1
temp = ''
print("Числа, содержащие хотя бы одну последовательность длиннее", k, "подряд идущих одинаковых цифр: ")
# Поиск чисел в строке
for i in range(len(seq)):
    if seq[i].isdigit():
        temp += seq[i]
    elif temp != '':
        # Поиск кол-ва идущих подряд одинаковых цифр
        for j in range(len(temp) - 1):
            if temp[j] == temp[j + 1]:
                kt += 1
        # Вывод при выполнении условия
        if kt >= k:
            print(temp, end=' ')
        kt = 1
        temp = ''
f.close()
