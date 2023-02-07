
from faker import Faker

# 随机数生成

fake = Faker()
name = fake.name()
print(name)  # 英文名
address = fake.address()
print(address)
tel = fake.phone_number()
print(tel)

fake = Faker(locale="zh_CN")
name = fake.name()
print(name)  # 英文名
tel = fake.phone_number()
print(tel)
address = fake.address()
print(address)

print(fake.locale())

