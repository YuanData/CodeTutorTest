from datetime import datetime
from random import randint

import openpyxl
from faker import Faker

# 初始化Faker对象，设置地区
fake = Faker('zh_TW')


# 函数生成随机中文名字
def generate_chinese_name():
    return fake.name()


# 函数生成随机电子邮件
def generate_email():
    # 使用Faker生成电子邮件
    return fake.email()


# 函数生成随机手机号
def generate_phone():
    # 使用Faker生成手机号
    # return fake.phone_number()
    return f"'09{''.join(str(randint(0, 9)) for _ in range(8))}"


# 函数生成随机时间戳
def generate_timestamp():
    start_date = datetime(2023, 10, 15)
    end_date = datetime(2023, 12, 4)
    return fake.date_time_between(start_date=start_date, end_date=end_date).strftime("%Y-%m-%d %H:%M:%S")


# 生成20条样本数据
sample_data = []
for _ in range(20):
    name = generate_chinese_name()
    email = generate_email()
    phone = generate_phone() if randint(0, 1) else ""
    created_at = generate_timestamp()
    sample_data.append([name, email, phone, "", created_at])

# 添加标题行
sample_data.insert(0, ["名稱", "電子郵件", "手機", "備註", "created_at"])

# 将数据按照 'created_at' 排序
sample_data_sorted = sorted(sample_data[1:], key=lambda x: x[4])  # 忽略标题行进行排序
sample_data_sorted.insert(0, sample_data[0])  # 重新添加标题行

# # 保存数据到CSV文件
# csv_file_path = 'sample_data.csv'
# with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerows(sample_data_sorted)

# 保存数据到Excel文件
xlsx_file_path = 'sample_data.xlsx'
wb = openpyxl.Workbook()
ws = wb.active
for row in sample_data_sorted:
    ws.append(row)
wb.save(xlsx_file_path)
