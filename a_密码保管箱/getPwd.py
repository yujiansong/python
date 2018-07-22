#! python3
# 密码保管箱设计_a
# 于建松
# 20180722

'''
用字典组织账号和密码的数据结构
'''
PASSWORDS = {'qq': {'1943756208': 'h9q@md',
                    '2378410569': '$ik2h6',
                    '2450796183': 'zb(pim',
                    '2680574319': '10mz@i',
                    '7514368920': 'k@lz1e'},
             '多看': {'1943756208': 'h9q@md',
                      '2378410569': '$ik2h6',
                      '2450796183': 'zb(pim',
                      '2680574319': '10mz@i',
                      '7514368920': 'k@lz1e'}
            }

'''
处理命令行参数sys.argv列表
sys.argv第一项包含程序的文件名 getPwd.py
sys.argv第二项是第一个命令行参数，这个参数就是账户的名称，通过它来获取密码
如果用户忘记添加参数，就提示用法信息
'''
import sys
if len(sys.argv) < 2:
    print('Usage: python getPwd.py [account] - copy account password')
    sys.exit()
    
account = sys.argv[1] #first command line arg is the account name
if account in PASSWORDS:
    #如果用户输入的命令行中大于3个参数,提示错误信息
    if len(sys.argv) > 3:
        print('you input too much args, the args not exceeding 2 parameters')
        sys.exit()
    elif len(sys.argv) == 3:
        print('good luck!, the password for ' + sys.argv[2] + ' of ' + account + ' is founded, it is: ' + PASSWORDS[account][sys.argv[2]])
    else:
        count = len(PASSWORDS[account])
        print('ok, you have ' + str(count) + ' account(s)')
        i = 1
        for k, v in PASSWORDS[account].items():
            print('good luck!, the password for ' + account + str(i) + ' founded, \n' + ' account: ' + k + '\n' + ' password: ' + v)
            i += 1
else:
    print('sorry, the account of your input is not exist.')

'''
λ python .\getPwd.py 多看
ok, you have 5 account(s)
good luck!, the password for 多看1 founded,
 account: 1943756208
 password: h9q@md
good luck!, the password for 多看2 founded,
 account: 2378410569
 password: $ik2h6
good luck!, the password for 多看3 founded,
 account: 2450796183
 password: zb(pim
good luck!, the password for 多看4 founded,
 account: 2680574319
 password: 10mz@i
good luck!, the password for 多看5 founded,
 account: 7514368920
 password: k@lz1e
'''

'''
在windows上，你可以创建一个批处理文件，利用cmd窗口来运行这个程序，
或者 WIN + R 运行
在文件编辑器中输入以下代码

@py.exe G:\python\a_密码保管箱\getPwd.py %*
@pause

放在 C:\Windows 下
有了这个批处理文件 就可以通过
WIN+R getPwd <accountname> 查询密码
'''
