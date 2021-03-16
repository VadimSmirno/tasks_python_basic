password = input('Придумайте пароль: ')

while True:
    if password.isalnum() == True and password.islower() == False and password.isupper() == False and len(password) > 8:
        print ('Это надежный пароль!')
        break
    else:
        print ('Пароль ненадёжный. Попробуйте ещё раз.')
        password = input('Придумайте пароль: ')