













































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