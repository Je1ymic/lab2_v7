k = input("Введите k: ")
while not k.isdigit():  # проверка входного значения
    k = input("Введите корректное k: ")
k = int(k)
kt = 1
work_buffer = ''  # рабочий буфер
buffer_len = 1  # размер буфера чтения
try:
    with open("lab2_f.txt", "r") as file:  # открываем файл
        print("Числа, содержащие хотя бы одну последовательность длиннее", k, "подряд идущих одинаковых цифр: ")
        buffer = file.read(buffer_len)  # читаем первый блок
        if not buffer:
            print("\nФайл lab2_f.txt в директории проекта пустой.\nДобавьте непустой файл в директорию или переименуйте существующий *.txt файл.")
        while buffer:  # пока файл не пустой
            if buffer.isdigit():  # если в буфере число
                work_buffer += buffer
            elif work_buffer != '':
                for i in range(len(work_buffer)-1):  # поиск кол-ва идущих подряд одинаковых цифр
                    if work_buffer[i] == work_buffer[i + 1]:
                        kt += 1
                        if kt >= k:  # вывод при выполнении условия
                            print(work_buffer, end=' ')
                            break
                    else:
                        kt = 1
                kt = 1
                work_buffer = ''
            buffer = file.read(buffer_len)  # читаем очередной блок
except FileNotFoundError:
    print("\nФайл lab2_f.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
    
