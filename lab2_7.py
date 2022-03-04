print("Введите k:")
k = int(input())
f = open("lab2_f.txt", "r")
seq = f.read().strip().split(' ')
kt = 1
print("Числа, содержащие хотя бы одну последовательность длиннее k подряд идущих одинаковых цифр: ")
for i in seq:
    for j in range(len(i) - 1):
        if i[j] == i[j + 1]:
            kt += 1
    if kt >= k:
        print(i, end=" ")
    kt = 1
f.close()