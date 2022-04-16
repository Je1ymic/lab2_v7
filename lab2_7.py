k = input("Введите k: ")
while not k.isdigit() or k == '0':  # проверка входного значения
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
            if buffer.isdigit():  # если в буфере цифра
                work_buffer += buffer  # набираем число
            elif work_buffer != '':  # если в рабочем буфере набралось число
                if len(work_buffer) > 1:  # число с более чем одним разрядом
                    for i in range(len(work_buffer)-1):  # поиск идущих подряд одинаковых чисел
                        if work_buffer[i] == work_buffer[i + 1]:
                            kt += 1
                        else:
                            if kt >= k:
                                print(work_buffer, end=' ')  # вывод при выполнении условия задачи
                                break
                            kt = 1
                        if kt >= k:
                            print(work_buffer, end=' ')  # вывод при выполнении условия задачи
                            break
                elif k == 1:  # однозначное число
                    print(work_buffer, end=' ')
                kt = 1
                work_buffer = ''
            buffer = file.read(buffer_len)  # читаем очередной блок
        if work_buffer != '':  # обработка числа стоящего в конце файла 
            if len(work_buffer) > 1:
                for i in range(len(work_buffer) - 1):
                    if work_buffer[i] == work_buffer[i + 1]:
                        kt += 1
                    else:
                        if kt >= k:
                            print(work_buffer, end=' ')
                            break
                        kt = 1
                    if kt >= k:
                        print(work_buffer, end=' ')
                        break
            elif k == 1:
                print(work_buffer, end=' ')
            kt = 1
            work_buffer = ''
except FileNotFoundError:
    print("\nФайл lab2_f.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
