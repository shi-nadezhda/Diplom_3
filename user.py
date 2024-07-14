import random

class User:
    name = "Fedora2"
    email = "fedora2@mail.ru"
    password = "Fedora2"
    
class RandomUser:
    user_name = f'Test Name {random.randint(0, 999)}'
    email = f'testmail{random.randint(0, 999)}@yandex.com'
    password = f'pass{random.randint(1000, 9999)}'
    fields = {
        'name': user_name,
        'email': email,
        'password': password
    }
