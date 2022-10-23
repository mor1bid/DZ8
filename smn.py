i = 0
prog = 1
login = ''
password = ''
print('Здравствуйте!', end=' ')
while True:
    if i == 1:
        print('\nГотово!', end=' ')
    menu = input('Выберите желаемый пункт меню:\n\n(a) Студент\n(b) Преподаватель\n(c) Администратор\n(e) Завершение работы\n\n')
    if menu == 'a':
        call = 0
        i = 0
        while prog == 1:
            studlogin = input('\nПожалуйста, введите свои имя пользователя и пароль!\n\nИмя пользователя: ')
            with open('passwords.txt', 'r', encoding='UTF-8') as lpr:
                text = lpr.readlines()
                for line in text:
                    if 'Студент:' in line and call == 0:
                        call = 1
                    if 'l: ' in line and call == 1:
                        call = 2
                    if call == 2:
                        login = line
                    if ' \n' in line:
                        call = 0
            studword = input('Пароль: ')
            with open('passwords.txt', 'r', encoding='UTF-8') as lpr:
                text = lpr.readlines()
                for line in text:
                    if 'Студент:' in line and call == 0:
                        call = 1
                    if 'p:' in line and call == 1:
                        call = 2
                    if ' ' not in line and call == 2:
                        password = line
                    if ' \n' in line:   
                        call = 0
            if studword not in password or studlogin not in login:
                print('Введены неверный логин и/или пароль.')
            else:    
                prog = 0       
        while i == 0:
            print('\n')
            print(studlogin, end=', ')
            answ = input('пожалуйста, выберите желаемое действие:\n\n(1) Посмотреть расписание\n(2) Посмотреть домашнее задание\n(e) Выход\n\n')
            if answ == '1':
                with open('lessons.txt', 'r', encoding='UTF-8') as lsn:
                    lsntxt = lsn.readlines()
                    print('\n')
                    for line in lsntxt:
                        print(line)
            elif answ == '2':
                with open('homework.txt', 'r', encoding='UTF-8') as hw:
                    hwtxt = hw.readlines()
                    print('\n')
                    for line in hwtxt:
                        print(line)
            elif answ == 'e':
                i += 1
            else:
                print('Ошибка!')
    elif menu == 'b':
        i = 0
        teachlogin = input('\nПожалуйста, введите свои имя пользователя и пароль!\n\nИмя пользователя: ')
        teachword = input('Пароль: ')
        while i == 0:
            print('\n')
            print(teachlogin, end=', ')
            answ = input('пожалуйста, выберите желаемое действие:\n\n(1) Посмотреть расписание\n(2) Посмотреть домашнее задание\n(3) Добавить домашнее задание\n(4) Убрать домашнее задание\n(e) Выход\n\n')
            if answ == '1':
                with open('lessons.txt', 'r', encoding='UTF-8') as lsn:
                    lsntxt = lsn.readlines()
                    print('\n')
                    for line in lsntxt:
                        print(line)
            elif answ == '2':
                with open('homework.txt', 'r', encoding='UTF-8') as hw:
                    hwtxt = hw.readlines()
                    print('\n')
                    for line in hwtxt:
                        print(line)
            elif answ == '3':
                put = 1
                with open('homework.txt', 'a', encoding='UTF-8') as work:
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
                    with open('homework.txt', 'w', encoding='UTF-8') as hw:
                        hw.seek(0)
                        hw.truncate()
                elif choi == '2':
                    day = input('Введите дату сдачи (дд.мм.гг) и желаемый предмет:\nДата: ')
                    sub = input('\nНазвание предмета: ')
                    with open('homework.txt', 'r', encoding='UTF-8') as delread:
                        text = delread.readlines()
                        with open('homework.txt', 'w', encoding='UTF-8') as hw:
                            hw.seek(0)
                            for line in text:
                                if day not in line and sub not in line:
                                    hw.write(line)
            elif answ == 'e':
                i += 1
            else:
                print('Ошибка!')
    elif menu == 'c':
        i = 0
        admnlogin = input('\nПожалуйста, введите свои имя пользователя и пароль!\n\nИмя пользователя: ')
        admnword = input('Пароль: ')
        while i == 0:
            print('\n')
            print(admnlogin, end=', ')
            answ = input('пожалуйста, выберите желаемое действие:\n\n(1) Посмотреть расписание\n(2) Изменить расписание\n(3) Изменить входные данные\n(e) Выход\n\n')
            if answ == '1':
                with open('lessons.txt', 'r', encoding='UTF-8') as lsn:
                    lsntxt = lsn.readlines()
                    print('\n')
                    for line in lsntxt:
                        print(line)
            elif answ == '2':
                j = 0
                while j == 0:
                    choi = input('\n(1) Удалить предмет\n(2) Добавить предмет\n(e) Выход\n\n')
                    call = 0
                    if choi == '1':                       
                        day = input('Введите день недели и номер желаемого предмета:\nДень недели: ')
                        numb = input('\nНомер предмета: ')
                        with open('lessons.txt', 'r', encoding='UTF-8') as lsn:
                            text = lsn.readlines()
                        with open('lessons.txt', 'w', encoding='UTF-8') as edit:
                            edit.seek(0)
                            for line in text:
                                if day in line and call == 0:
                                    edit.writelines(line)
                                    call = 1
                                if day not in line and call == 0:
                                    edit.writelines(line)
                                if numb not in line and day not in line and call == 1:
                                    edit.writelines(line)
                                    call = 1
                                if numb in line and call == 1 and day not in line:
                                    edit.write(numb)
                                    edit.write('.\n')
                                    call = 0
                                if ' \n' in line and call == 1:
                                    edit.write(numb)
                                    edit.write('.\n')
                                    call = 0
                    elif choi == '2':
                        call = 0
                        day = input('Введите день недели, номер и название желаемого предмета:\nДень недели: ')
                        numb = input('\nНомер предмета: ')
                        sub = input('\nНазвание предмета: ')
                        with open('lessons.txt', 'r', encoding='UTF-8') as lsn:
                            text = lsn.readlines()
                        with open('lessons.txt', 'w', encoding='UTF-8') as edit:
                            edit.seek(0)
                            for line in text:
                                if day in line and call == 0:
                                    edit.writelines(line)
                                    call = 1
                                if day not in line and call == 0:
                                    edit.writelines(line)
                                if numb not in line and day not in line and call == 1:
                                    call = 1
                                    if ' \n' in line:
                                        lin = line.replace(' \n', '')
                                        edit.write(lin)
                                    else:
                                        edit.writelines(line)
                                if numb in line and call == 1 and day not in line:
                                    edit.write(numb)
                                    edit.write('. ')
                                    edit.write(sub)
                                    edit.write(' \n')
                                    call = 0
                                if ' \n' in line and call == 1:
                                    edit.write('\n')
                                    edit.write(numb)
                                    edit.write('. ')
                                    edit.write(sub)
                                    edit.write(' \n')
                                    call = 0                                            
                    elif choi == 'e':
                        j += 1
                    else:
                        print('Ошибка!')
            elif answ == '3':
                g = 0
                g2 = 0                
                pas = input('\n(1) Логин и пароль студента\n(2) Логин и пароль преподавателя\n(3) Логин и пароль администратора\n(e) Выход\n\n')
                if pas == '1':
                    call = 0
                    while g == 0:                            
                        yn = input('Сменить логин? y/n: ')
                        if yn == 'y':
                            nlogin = input('Введите новый логин: ')
                            with open('passwords.txt', 'r', encoding='UTF-8') as lpr:
                                text = lpr.readlines()
                                with open('passwords.txt', 'w', encoding='UTF-8') as lpw:
                                    for line in text:
                                        if 'Студент:' in line and call == 0:
                                            lpw.writelines(line)
                                        else:
                                            # lpw.writelines(line)
                                            call = 1
                                        if 'l: ' in line and call == 1:
                                            lpw.write(nlogin)
                                        else:
                                            lpw.write(line)                                            
                                        if ' \n' in line:
                                            call = 0
                                    g += 1
                        elif yn == 'n':
                            g += 1
                        else:
                            print('Ошибка')
                    while g2 == 0:
                        yn = input('Сменить пароль? y/n: ')
                        if yn == 'y':
                            npass = input('Введите новый пароль: ')
                            with open('passwords.txt', 'r', encoding='UTF-8') as lpr:
                                text = lpr.readlines()
                                with open('passwords.txt', 'w', encoding='UTF-8') as lpw:
                                    for line in text:
                                        if 'Студент:' in line and call == 0:
                                            lpw.writelines(line)
                                        else:
                                            # lpw.writelines(line)
                                            call = 1
                                        if 'p: ' in line and call == 1:
                                            lpw.write(line)
                                            lpw.write(npass)
                                        else:
                                            lpw.write(line)
                                        if ' \n' in line:
                                            call = 0
                                    g2 += 1
                        elif yn == 'n':
                            g2 += 1
                        else:
                            print('Ошибка')
            elif answ == 'e':
                i += 1
    elif menu == 'e':
        print('\nДо свидания!')
        break
    else:
        print('\nОшибка!')