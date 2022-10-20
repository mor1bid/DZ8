print('Здравствуйте!', end=' ')
with open('homework.txt', 'r') as hw:
    hwtxt = hw.readlines()
with open('lessons.txt', 'r') as lsn:
    lsntxt = lsn.readlines()
while True:
    if i == 1:
        print('\nГотово!', end=' ')
    menu = input('Выберите желаемый пункт меню:\n(a) Студент\n(b) Преподаватель\n(c) Администратор\n(e) Выход\n\n')
    if menu == 'a':
        i = 0
        login = input('\nПожалуйста, введите свои имя пользователя и пароль!\n\nИмя пользователя: ')
        studword = input('Пароль: ')
        while i == 0:
            print(login, end=' - ')
            answ = input('пожалуйста, выберите желаемое действие:\n\n(1) Посмотреть расписание\n(2) Посмотреть домашнее задание\n\n')
            if answ == '1':
                print(*lsntxt)
                i += 1
            elif answ == '2':
                print(*hwtxt)
                i += 1
            else:
                print('Ошибка!')
    elif menu == 'b':
        i = 0
        login = input('\nПожалуйста, введите свои имя пользователя и пароль!\n\nИмя пользователя: ')
        teachword = input('Пароль: ')
        while i == 0:
            print(login, end=' - ')
            answ = input('пожалуйста, выберите желаемое действие:\n\n(1) Посмотреть расписание\n(2) Посмотреть домашнее задание\n(3) Добавить домашнее задание\n\n')
            if answ == '1':
                print(*lsntxt)
                i += 1
            elif answ == '2':
                print(*hwtxt)
                i += 1
            elif answ == '3':
                put = 1
                print('\nНапишите дату сдачи, предмет и домашнее задание:')
                with open('homework.txt', 'a') as work:
                    while put > 0:
                        if put > 1:
                            work.writelines(' \n')
                        text = input()
                        work.writelines(text)
                        putch = input('Добавить ещё? y/n: ')
                        if putch == 'n':
                            put = 0
                        elif putch == 'y':
                            put += 1
                        else:
                            print('Ошибка!')
                i += 1
            else:
                print('Ошибка!')
    elif menu == 'e':
        print('\nДо свидания!')
        break
    else:
        print('\nОшибка!')