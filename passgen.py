from random import *


letters_low = list('abcdefghijklmnopqrstuvwxyz')
letters_up = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
digits = list('0123456789')
punctuations = list('!#$%&*+#=?@^_')
fake_letters = list('1ilo0OI')
chars = ''
try_again = 'y'


def password_generator(length, count, punct, fake):

    passwords = []
    buffer = []
    if fake == 'n':
        for i in range(int(count)):
            for j in range(int(length)):
                if punct == 'y':
                    lst = letters_up + letters_low + digits + punctuations
                    c = choice(lst)
                    buffer.append(c)
                else:
                    lst = letters_up + letters_low + digits
                    c = choice(lst)
                    buffer.append(c)
            shuffle(buffer)
            passwords.append(buffer)
            buffer = []
    else:
        lst = digits + letters_low + letters_up
        for i in lst:
            if i in fake_letters:
                lst.remove(i)
        for i in range(int(count)):
            for j in range(int(length)):
                if punct == 'y':
                    lst = letters_up + letters_low + digits + punctuations
                    c = choice(lst)
                    buffer.append(c)
                else:
                    lst = letters_up + letters_low + digits
                    c = choice(lst)
                    buffer.append(c)
            shuffle(buffer)
            passwords.append(buffer)
            buffer = []
    return passwords


def valid_input(number):

    while True:
        print('Нипонятно... Введите целое число > 0')
        number = input('Ваш ответ: ')
        if number.isdigit() and int(number) > 0:
            return number
        else:
            continue


def valid_answer():

    while True:
        print('Нипонятно... Введите "y" или "n" без кавычек!')
        answer = input('Ваш ответ: ')
        if answer in ('y', 'n'):
            return answer
        else:
            continue


while True:

    if try_again == 'y':

        answer_len = input('Длина пароля: ')
        if answer_len.isdigit() == False or int(answer_len) < 1:
            answer_len = valid_input(answer_len)

        answer_count = input('Количество паролей: ')
        if answer_count.isdigit() == False or int(answer_count) < 1:
            answer_count = valid_input(answer_count)

        answer_punct = input('Включить спецсимволы(y/n): ')
        if answer_punct not in ('y', 'n'):
            answer_punct = valid_answer()

        answer_fake = input('Исключить символы "1ilo0oI"(y/n): ')
        if answer_fake not in ('y', 'n'):
            answer_fake = valid_answer()

        chars = password_generator(answer_len, answer_count, answer_punct, answer_fake)
        print()
        for i in chars:
            print(*i, sep='')
        print()
        try_again = input('Генерировать еще раз?(y/n): ')


    elif try_again == 'n':
        print('Goodbye!')
        break

    else:
        try_again = valid_answer()
