hwtxt = ''
lsntxt = ''
i = 0
print('Здравствуйте!', end=' ')
def add_work(hwtxt):
    with open('homework.txt', 'r') as hw:
        hwtxt = hw.readlines()
        return hwtxt
def add_lsn(lsntxt):
    with open('lessons.txt', 'r') as lsn:
        lsntxt = lsn.readlines()
        return lsntxt
while True:
    if i == 1:
        print('\nГотово!', end=' ')
    menu = input('Выберите желаемый пункт меню:\n\n(a) Студент\n(b) Преподаватель\n(c) Администратор\n(e) Завершение работы\n\n')
    if menu == 'a':
        i = 0
        login = input('\nПожалуйста, введите свои имя пользователя и пароль!\n\nИмя пользователя: ')
        studword = input('Пароль: ')
        while i == 0:
            print('\n')
            print(login, end=' - ')
            answ = input('пожалуйста, выберите желаемое действие:\n\n(1) Посмотреть расписание\n(2) Посмотреть домашнее задание\n(e) Выход\n\n')
            if answ == '1':
                # for line in lsntxt:
                print(add_lsn(lsntxt))
            elif answ == '2':
                # for line in hwtxt:
                print(add_work(hwtxt))
            elif answ == 'e':
                i += 1
            else:
                print('Ошибка!')
    elif menu == 'b':
        i = 0
        login = input('\nПожалуйста, введите свои имя пользователя и пароль!\n\nИмя пользователя: ')
        teachword = input('Пароль: ')
        while i == 0:
            print('\n')
            print(login, end=', ')
            answ = input('пожалуйста, выберите желаемое действие:\n\n(1) Посмотреть расписание\n(2) Посмотреть домашнее задание\n(3) Добавить домашнее задание\n(4) Убрать домашнее задание\n(e) Выход\n\n')
            if answ == '1':
                # for line in lsntxt:
                print(add_lsn(lsntxt))
            elif answ == '2':
                # for line in hwtxt:
                print(add_work(hwtxt))
            elif answ == '3':
                put = 1
                with open('homework.txt', 'a') as work:
                    while put != 0:
                        print('\nНапишите дату сдачи, предмет и домашнее задание:')
                        if put > 1:
                            work.writelines('\n \n')
                        text = input()
                        work.writelines(text)
                        putch = input('Добавить ещё? y/n: ')
                        if putch == 'n':
                            work.writelines('\n \n')
                            put = 0
                        elif putch == 'y':
                            put += 1
                        else:
                            print('Ошибка!')
            elif answ == '4':
                choi = input('\nУдалить данные?\nЕсли да - удалить все данные, либо выборочно? n/1/2: ')
                if choi == '1':
                    with open('homework.txt', 'w') as hw:
                        hw.seek(0)
                        hw.truncate()
                elif choi == '2':
                    cont = input('Введите фамилию желаемого контакта: \n')
                    with open('homework.txt', 'r') as delread:
                        text = delread.readlines()
                        with open('homework.txt', 'w') as hw:
                            call = 0
                            hw.seek(0)
                            for line in text:
                                if cont not in line and call == 0:
                                    hw.write(line)
                                else:
                                    call = 1
                                if line != ' \n' and call == 1:
                                    hw.write('')
                                else:
                                    call = 0
            elif answ == 'e':
                i += 1
            else:
                print('Ошибка!')
    elif menu == 'e':
        print('\nДо свидания!')
        break
    else:
        print('\nОшибка!')