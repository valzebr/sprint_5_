from random import randint


class MyPerson:
    my_name = 'valera'
    my_email = 'valerazacepin_qa12@ya.ru'
    my_password = '123456789'


class MyRandomData:
    user_name = 'Testname'
    rand_email = f'{user_name}{randint(100, 999)}@ya.ru'
    rand_password = f'{randint(100000, 999999)}'
