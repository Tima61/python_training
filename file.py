# file = open('test_file.txt', mode='rt', encoding='utf-8')
# print(file.name)
# print(file.mode)
# print(file.read())
# file.close()

# with open(file='test_file.txt') as file:
#     # print(file.read())
#     # print(file.readlines())
#
#     for line in file:
#         print(line.strip())


# В качестве аргумента использовать только строки
# my_string = "Hello World"
# password_list = ['1213', '321', '321', '345', '123', 'xxxx', 'qweccccrty', 'Time is money']
#
# with open(file='spam.txt', mode='a') as file:
#
#     file.writelines(line+ '\n' for line in password_list)

import requests

responce = requests.get('https://white-rainbow.ru/upload/iblock/b26/7sf66d03tagu4tqpxywzr9e18325c05v/BSA_3747_Pano_copy.750.jpg')

with open(file='nature.jpg', mode='wb') as file:
    file.write(responce.content)