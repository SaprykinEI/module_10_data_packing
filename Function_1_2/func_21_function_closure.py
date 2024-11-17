def password_protected(password):
    def inner():
        if password == "secret":
            print("Доступ разрешен!")
        else:
            print("В доступе отказано!")

    return inner

param = 25

login = password_protected('adf')
login()
print()
# login_1 = password_protected('no_secret')
# login_1()


