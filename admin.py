import classes
import project


def account():
    web = input(f"""
                1.  My account
                2.  Foydalanuvchilar
                3.  Product
                4.  Haridlar
                    >>>>>>>> """)
    if web == '1':
        return profile()
    elif web == '2':
        return person()
    elif web == '3':
        return product()
    elif web == '4':
        return orders()
    else:
        print("Wrong input")
        return account()


def profile():
    web = input(f"""
                1.  Admin Add
                2.  Setting
                3.  Card money
                0.  Back
                >>>>>>> """)
    if web == '1':
        return admin_register()
    elif web == '2':
        return setting()
    elif web == '3':
        return card()
    elif web == '0':
        return account()
    else:
        print("Wrong input")
        return profile()


def admin_register():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    phone_number = input("Enter your phone number: ")
    password = input("Enter your password: ")
    card = input("Enter your card number: ")
    money = float(input("Enter your money: "))
    print(classes.Admin.insert(first_name, last_name, phone_number, password, card, money))
    return profile()


def setting():
    web = input(f"""
                1.  Select
                2.  Update
                0. Back
                >>>>>> """)
    if web == '1':
        print(classes.Admin.select())
        # for i in classes.Users.select():
        #     print(f"""
        #             ID: {i[0]}
        #             First Name: {i[1]}
        #             Last Name: {i[2]}
        #             Password: {i[3]}
        #             Card Number: {i[4]}
        #             Money: {i[5]}
        #             Phone Number: {i[6]}
        #             Birthday: {i[7]}
        #
        #             """)
        return setting()
    elif web == '2':
        return
    elif web == '0':
        return account()
    else:
        print("Wrong input")
        return setting()


def card():
    web = input(f"""
                1.  Card money
                2.  Card Number
                0. Back
                >>>>>>> """)
    if web == '1':
        return
    elif web == '2':
        return
    elif web == '0':
        return profile()
    else:
        print("Wrong input")
        return card()


def product():
    web = input(f"""
                
                1.  Laptop
                2.  Phone
                0.  back
                >>>>>>> """)
    if web == '1':
        return laptop()
    elif web == '2':
        return phone()
    elif web == '0':
        return account()
    else:
        print("Wrong input")
        return product()


def laptop():
    web = input(f"""
    
                s.  search 
                1.  Select
                2.  Insert
                3.  Update
                4.  Delete
                0.  Back
                """)
    if web == "1":
        print(classes.Laptop.select())
        return laptop()
        # for i in classes.Laptop.select():
        #     print(f"""
        #                         Name: {i[0]}
        #                         Price: {i[1]}
        #                         Description: {i[2]}
        #                         Count: {i[3]}
        #                         Serial Number: {i[4]}
        #                         Admin ID: {i[5]}
        #                         """)
        #     return laptop()
    elif web == "2":
        name = input("Laptop Name: ")
        price = int(input("Price: "))
        description = input("Description: ")
        count = int(input("Count: "))
        serial_number = input("Serial Number: ")
        admin_id = input("Admin ID: ")
        print(classes.Laptop.insert(name, price, description, count, serial_number, admin_id))
        return laptop()

    elif web == "3":
        column = input("Column Name: ")
        old_name = input("Old Name: ")
        new_name = input("New Name: ")
        print(classes.Laptop.update(column, old_name, new_name, "laptop"))
        return laptop()

    elif web == "4":
        column = input("column name: ")
        name = input("Name: ")
        print(classes.Laptop.delete(column, name, "laptop"))
        return laptop()
    elif web == "0":
        return product()
    elif web == 's':
        search = input("Search: ")
        print(classes.Laptop.search_name(search))
        return person()


def phone():
    web = input(f"""
                s.  search
                1.  Select
                2.  Insert
                3.  Update
                4.  Delete
                0.  Back
                """)

    if web == "1":
        print(classes.Phone.select())
        return phone()
        # for i in classes.Laptop.select():
        #     print(f"""
        #             Name: {i[0]}
        #             Price: {i[1]}
        #             Description: {i[2]}
        #             Count: {i[3]}
        #             Serial Number: {i[4]}
        #             Admin ID: {i[5]}
        #             """)
        #     return phone()
    elif web == "2":
        name = input("Phone Name: ")
        price = int(input("Price: "))
        description = input("Description: ")
        count = int(input("Count: "))
        serial_number = input("Serial Number: ")
        admin_id = input("Admin ID: ")
        print(classes.Phone.insert(name, price, description, count, serial_number, admin_id))
        return phone()

    elif web == "3":
        column = input("Column Name: ")
        old_name = input("Old Name: ")
        new_name = input("New Name: ")
        print(classes.Phone.update(column, old_name, new_name, "phone"))
        return phone()

    elif web == "4":
        column = input("column name: ")
        name = input("Name: ")
        print(classes.Phone.delete(column, name, "phone"))
        return phone()
    elif web == "0":
        return product()
    elif web == 's':
        search = input("Search: ")
        print(classes.Phone.search_name(search))
        return person()


def person():
    web = input(f"""
                s.  search
                1.  Select
                2.  Insert
                3.  Update
                4.  Delete
                0.  Back
                """)
    if web == '1':
        print(classes.Users.select())
        # for i in classes.Users.select():
        #     print(f"""
        #                 ID: {i[0][0]}
        #                 First Name: {i[0][1]}
        #                 Last Name: {i[0][2]}
        #                 Phone Number: {i[0][3]}
        #                 Address: {i[0][4]}
        #                 Personal ID: {i[0][5]}
        #                         """)
        return person()
    elif web == '2':
        return project.register()
    elif web == '3':
        column = input("Column Name: ")
        old_name = input("Old Name: ")
        new_name = input("New Name: ")
        print(classes.Users.update(column, old_name, new_name))
        return person()
    elif web == '4':
        column = input("column name: ")
        name = input("Name: ")
        print(classes.Users.delete(column, name))
        return person()
    elif web == '0':
        return account()
    elif web == 's':
        search = input("Search: ")
        print(classes.Users.search_name(search))
        return person()
    else:
        print("Wrong input")
        return person()


def orders():
    web = input(f"""
                s.  search
                1.  Select
                0.  Back""")
    if web == "1":
        return select()
    elif web == "0":
        return account()
    elif web == 's':
        search = input("Search: ")
        print(classes.Users.search_name(search))
        return person()


def select():
    print(classes.Buyurtma.select())
    # for i in data:
    #     print(f"""
    #                     Name: {i[0]}
    #                     Count: {i[1]}
    #                     Color: {i[2]}
    #                     Laptop: {i[3]}
    #                     Phone: {i[4]}
    #                     Payment: {i[5]}
    #                     Address: {i[6]}
    #                     Person: {i[7]}
    #                     """)
    return orders()
