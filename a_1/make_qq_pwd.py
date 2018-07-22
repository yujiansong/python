#! pyton 3
# 随机生成qq和对应的密码,以字典的格式返回
# author: 于建松
import random,pprint
accounts = '1234567890'
passwords = 'abcdefghijklmnopqrstuvwxyz1234567890@#$%&*().'
account = {}
myPasswords = {}
for i in range(5):
    '''随机选取10个字符，
       并拼接成字符串
       random.sapple()#随机选取n个字符
    '''
    account_one = ''.join(random.sample(accounts, 10))
    password_one = ''.join(random.sample(passwords, 6))
    account.setdefault(account_one, password_one)

myPasswords.setdefault('qq', account)
myPasswords.setdefault('多看', account)
pprint.pprint(myPasswords)
