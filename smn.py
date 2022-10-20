with open('homework.txt', 'r') as hw:
    hwtxt = hw.readlines()
with open('lessons.txt', 'r') as lsn:
    lsntxt = lsn.readlines()
while True:
    menu = input('\nЗдравствуйте! Выберите желаемый пункт меню:\n(a) Студент\n(b) Преподаватель\n(c) Администратор\n(e) Выход\n\n')
