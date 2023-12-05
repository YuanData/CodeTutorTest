from random import randint

from faker import Faker

# 初始化 Faker 對象，設置地區
fake = Faker('zh_TW')


def generate_test_data() -> dict:
    name = fake.name()
    email = fake.email()
    test_data = {'name': name, 'email': email}

    if randint(0, 1):
        test_data['phone'] = f"'09{''.join(str(randint(0, 9)) for _ in range(8))}"

    need_note = False
    if need_note:
        test_data['notes'] = fake.sentence(nb_words=10)

    return test_data
