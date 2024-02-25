from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    variant = int(input(f'В каком варианте записать данные?\n\n'
                 f"1 Вариант: \n"
                 f"{name}\n{surname}\n{phone}\n{address}\n\n"
                 f"2 Вариант: \n"
                 f"{name};{surname};{phone};{address}\n"
                 f'Выберите вариант: '))
    while variant != 1 and variant != 2:
        print('Неправильный ввод!')
        variant = int(input('Выберите вариант: '))
    if variant == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")       
    elif variant == 2:
        with open('data_second_variant.csv','a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

def print_data():
    variant = int(input(f'В каком варианте вывести данные? 1 или 2? Выберите вариант:'))
    while variant != 1 and variant != 2:
        print('Неправильный ввод!')
        variant = int(input('Выберите вариант: '))
    if variant == 1:
        print('Вывожу данные из 1-го файла: \n')
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            data_first_list = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_list.append(''.join(data_first[j: i + 1]))
                    j = i
            print(''.join(data_first_list))
    else:
        print('Вывожу данные из 2-го файла: \n')
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            print(*data_second)

def modify_data():
    variant = int(input('В каком файле изменить данные? 1 или 2? Выберите вариант: '))
    while variant not in [1, 2]:
        print('Неправильный ввод!')
        variant = int(input('Выберите вариант: '))
    file_name = 'data_first_variant.csv' if variant == 1 else 'data_second_variant.csv'
    print("Выберите номер записи для изменения:")
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        if variant == 1:
            for idx in range(0, len(data), 5):
                print(f"{idx // 5 + 1}: {data[idx].strip()}")
        else:
            for idx, line in enumerate(data):
                print(f"{idx + 1}: {line.strip()}")
    record_number = int(input("Введите номер записи: ")) - 1
    while record_number < 0 or (variant == 1 and record_number >= len(data) / 5) or (variant == 2 and record_number >= len(data)):
        print("Неправильный номер записи!")
        record_number = int(input("Введите номер записи: ")) - 1
    if variant == 1:
        start_index = record_number * 5
        print("Выбранная запись для изменения:")
        for i in range(start_index, start_index + 4):
            print(data[i].strip())
        field_choice = int(input("Введите номер поля для изменения (1 - имя, 2 - фамилия, 3 - номер телефона, 4 - адрес): "))
    else:
        start_index = record_number
        print("Выбранная запись для изменения:")
        print(data[start_index].strip())
        field_choice = int(input("Введите номер поля для изменения (1 - имя, 2 - фамилия, 3 - номер телефона, 4 - адрес): "))
    while field_choice not in [1, 2, 3, 4]:
        print("Неправильный номер поля!")
        field_choice = int(input("Введите номер поля для изменения (1 - имя, 2 - фамилия, 3 - номер телефона, 4 - адрес): "))
    new_value = input("Введите новое значение: ")
    if variant == 1:
        data[start_index + field_choice - 1] = new_value + '\n'
    else:
        entry = data[start_index].strip().split(';')
        entry[field_choice - 1] = new_value
        data[start_index] = ';'.join(entry) + '\n'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(data)