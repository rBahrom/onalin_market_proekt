from datetime import datetime, timedelta
import random
import classes
import main_1
import admin1
import user1


def project():
    web = input(f"""
                Assalomu alaykum
                    1.  Login
                    2.  Register
                    3.  Admin
                    >>>>>> """)
    if web == "1":
        return login()
    elif web == "2":
        return register()
    elif web == "3":
        return admin_add()
    else:
        print("Error")
        return project()


def register():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    phone_number = input("Enter your phone number: ")
    password = input("Enter your password: ")
    card = input("Enter your card number: ")
    money = float(input("Enter your money: "))
    print(classes.User.insert(first_name, last_name, phone_number, password, card, money))
    return user.person(password)


# def login():
#     """Bu yerda foydalanuvchi login kirishini tekshirish """
#     print(f"""                      Assalomu alaykum hurmatli mijoz
#                     serverga o'langan nomeringizni kiriting""")
#     phone_number = input("Enter your phone number: ")
#     if main.Person.phone(phone_number):
#         array = random.randint(10000, 99999)
#         start_time = datetime.now()
#         print(start_time)
#         a = 0
#         end_time = datetime.now()
#         reversed_time = start_time - timedelta(seconds=10)
#         print(f""" Hurmatli mijoz bu codni hech kimga bermang : {array}   """)
#         cod = int(input("""Enter your cod : """))
#         # if timedelta(seconds=0) < end_time - start_time < timedelta(seconds=30):
#
#         while cod != array and a < 100:
#             if reversed_time < start_time:
#                 print("""               Error""")
#                 cod = int(input("""Enter your cod : """))
#                 a += 1
#                 if a > 90:
#                     print("""       Hurmatli mijoz siz kiritgan cod hammasi xato
#                         Iltimos qaytadan kiring""")
#                     return project()
#             else:
#                 print("Vaqt tugadi")
#                 return project()
#         return person_password()
#
#     else:
#         print("""               << Error >>
#         Hurmatli mijoz siz kiritgan nomer malumotlar bazasidan topilmadi""")
#         return login()


def login():
    """Bu yerda foydalanuvchi login kirishini tekshirish """
    print(f"""                      Assalomu alaykum hurmatli mijoz 
                    serverga o'langan nomeringizni kiriting""")
    phone_number = input("Enter your phone number: ")
    if main.Person.phone(phone_number):
        array = random.randint(10000, 99999)
        start_time = datetime.now()
        print(start_time)
        print(f""" Hurmatli mijoz bu codni hech kimga bermang : {array}   """)
        cod = int(input("""Enter your cod : """))
        a = 0
        end_time = datetime.now()
        if timedelta(seconds=0) < end_time - start_time < timedelta(seconds=10):
            while cod != array and a < 3:
                print("""               Error""")
                cod = int(input("""Enter your cod : """))
                a += 1
                if a > 2:
                    print("""   Hurmatli mijoz siz kiritgan cod hammasi xato 
                        Iltimos qaytadan kiring""")
                    return project()
            return person_password()
        else:
            print("""PAROL ESKIRDI ILTIMOS QAYTADAN YUBORING""")

    else:
        print("""               << Error >>
        Hurmatli mijoz siz kiritgan nomer malumotlar bazasidan topilmadi""")
        return login()


def person_password():
    """Bu yerda tizimga kirishda password tasdiqlash"""
    print(f"""<<<<<<<<< password >>>>>>>>>>""")
    password = input("""Enter your password :    """)
    if main.Person.password(password):
        return user.person(password)
    else:
        n = 0
        while n < 3:
            print("Error")
            password = input("""Enter your password :    """)
            if main.Person.password(password):
                return project()
            n += 1

        return user.person(password)


def admin_add():
    web = input(f"""
                Assalomu alaykum
                    1.  Login
                    0. Back
                """)
    if web == "1":
        return login_admin()
    elif web == "0":
        return project()
    else:
        print("Error input ")
        return admin_add()


def login_admin():
    """Bu yerda foydalanuvchi login kirishini tekshirish """
    print(f"""                      Assalomu alaykum hurmatli mijoz 
                        serverga o'langan nomeringizni kiriting""")
    phone_number = input("Enter your phone number: ")
    if main.Check.phone(phone_number):
        return password_admin()
    else:
        print("""Hurmatli admin siz kiritgan nomer malumotlar bazasidan topilmadi
        Iltimos qaytadan kiring yoki sizda adminlik huquqi mavjud emas""")
        return login_admin()


def password_admin():
    password = input("Enter your password: ")
    if main.Check.admin_password(password):
        return admin.account()
    else:
        return admin_add()


if __name__ == '__main__':
    project()
