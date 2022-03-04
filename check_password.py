user_password = 'a123456'
i = 3

while i > 0 :
    password = input('請輸入密碼: ')
    if password == user_password :
        print('登入成功')
        break
    else:
        i -= 1
        if i == 0:
            break
        else:
            print(f'密碼錯誤! 還有{i}次機會')

