from logger import input_data, print_data, modify_data, delete_data

def interface():
    while True:
        print('Добрый день! Вы попали на специальный бот-справочник от ГБ!: \n 1 - запись данных \n 2 - вывод данных \n 3 - изменение данных \n 4 - удаление данных \n 5 - выход')
        command = int(input('Введите число: '))

        while command not in [1, 2]:
            print('Неправильный ввод!')
            command = int(input('Введите число: '))
    
        if command == 1:
            input_data()
        elif command == 2:
            print_data()
        elif command == 3:
            modify_data()
        elif command == 4:
            delete_data()
        elif command == 5:
            print('До свидания!')
            return

        repeat = input('Хотите продолжить работу? (да/нет): ')
        if repeat.lower() != 'да':
            print('До свидания!')
            return