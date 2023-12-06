import csv
from datetime import datetime
from random import randint

import numpy as np
import openpyxl
from faker import Faker

# 初始化 Faker，設置地區
fake = Faker('zh_TW')

DOMAIN_WEIGHTS = {
    "@gmail.com": 0.8,
    "@outlook.com": 0.3,
    "@yahoo.com": 0.2,
    "@hotmail.com": 0.15,
    "@icloud.com": 0.1,
    "@hinet.net": 0.05,
    "@pchome.com.tw": 0.03,
    "@seed.net.tw": 0.03,
    "@msn.com": 0.01,
}


def normalize_weights(weights: dict) -> dict:
    total = sum(weights.values())
    return {k: v / total for k, v in weights.items()}


NORMALIZED_WEIGHTS = normalize_weights(DOMAIN_WEIGHTS)
DOMAINS_PAIR = list(NORMALIZED_WEIGHTS.keys())
WEIGHTS_PAIR = list(NORMALIZED_WEIGHTS.values())


def rand_email() -> str:
    email = fake.email()
    return email.split('@')[0] + np.random.choice(DOMAINS_PAIR, p=WEIGHTS_PAIR)


def rand_phone() -> str:
    return f"'09{''.join(str(randint(0, 9)) for _ in range(8))}"


def generate_test_data() -> dict:
    test_data = {'name': fake.name(), 'email': rand_email()}

    if randint(1, 10) <= 4:
        test_data['phone'] = rand_phone()

    need_note = False
    if need_note:
        test_data['notes'] = fake.sentence(nb_words=10)

    return test_data


# -------------------------------------------------------------------

SAMPLE_DATA_HEADERS = ["名稱", "電子郵件", "手機", "備註", "created_at"]


def rand_dt_in_period() -> str:
    start_date = datetime(2023, 10, 15)
    end_date = datetime(2023, 12, 4)
    return fake.date_time_between(start_date, end_date) \
        .strftime("%Y-%m-%d %H:%M:%S")


def generate_sample_data(num_samples: int) -> list:
    data = []
    for _ in range(num_samples):
        name = fake.name()
        email = rand_email()
        phone = rand_phone() if randint(1, 100) <= 25 else ""
        created_at = rand_dt_in_period()
        data.append([name, email, phone, "", created_at])
    return sorted(data, key=lambda x: x[4])  # 用created_at排序


def save_to_csv(data: list, file_path: str):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(SAMPLE_DATA_HEADERS)
        writer.writerows(data)


def save_to_excel(data: list, file_path: str):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(SAMPLE_DATA_HEADERS)
    for row in data:
        ws.append(row)
    wb.save(file_path)


if __name__ == '__main__':
    sample_data = generate_sample_data(40)
    save_to_csv(sample_data, 'output/sample_data.csv')
    save_to_excel(sample_data, 'output/sample_data.xlsx')
