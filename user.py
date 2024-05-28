import classes
import project
from classes import *


def person(password):
    web = input(f"""
                1.  My profile
                2.  Shop
                3.  Order
                """)
    if web == '1':
        return profile(password)
    elif web == '2':
        return shop(password)
    elif web == '3':
        return buyurtma(password)
    else:
        print("Wrong input")
        return person(password)


def profile(password):
    web = input(f"""
                1.  Setting
                2.  Money to the card
                0.  Back
                >>>>> """)
    if web == '1':
        return setting(password)
    elif web == '2':
        return card(password)
    elif web == '0':
        return person(password)
    else:
        print("Wrong input")
        return profile(password)


def setting(password):
    web = input(f"""
                1.  Select
                2.  Update
                3.  Delete => Account exit
                0.  Back
                >>>>>> """)
    if web == "1":
        print(classes.User.select(password))
        back = input(f"""
                    0.  back
                    >>>> """)
        if back == "0":
            setting(password)

    elif web == "2":
        column = input("Column Name: ")
        old_name = input("Old Name: ")
        new_name = input("New Name: ")
        print(Country.update(column, old_name, new_name, "persons"))
        return setting(password)

    elif web == "3":
        ism = ""
        column = input("Column Name: ")
        name = input(" Name: ")
        print(Country.delete(column, name, "persons"))
        return setting(password)
    elif web == '0':
        return profile(password)


def card(password):
    money = float(input("Kartangizga pul o'tqazish: "))
    print()


def shop(password):
    print("""Hurmatli mijoz siz quyidagi malumotlarni tuldirmasdan buyurtma berolmaysiz
        Agar oldin manzillaringizni kiritgan bulsangiz bemalol harid qilishingiz mumkun """)
    web = input(f"""
                1.  Country
                2.  City
                3.  Address
                4.  Payment Type
                5.  Haridor
                6.  market
                0.  Back
                >>>>>>> """)
    if web == '1':
        return country(password)
    elif web == '2':
        return city_table(password)
    elif web == '3':
        return address_table(password)
    elif web == '4':
        return payment_status(password)
    elif web == '5':
        return haridor_table(password)
    elif web == "6":
        return market(password)
    elif web == "0":
        return person(password)


def country(password):
    web = input("""
                1.  Select
                2.  Insert
                3.  Update
                4.  Delete
                0.  back
                >>>>>> """)
    if web == "1":
        print(Country.select())
        back = input(f"""
                        0.  back
                        >>>> """)
        if back == "0":
            return country(password)

    elif web == "2":
        name = input("Country Name: ")
        print(Country.insert(name))
        return country(password)

    elif web == "3":
        column = input("Column Name: ")
        old_name = input("Old Name: ")
        new_name = input("New Name: ")
        print(Country.update(column, old_name, new_name, "country"))
        return country(password)

    elif web == "4":
        column = input("column name: ")
        name = input("Name: ")
        print(Country.delete(column, name, "country"))
        return country(password)
    elif web == "0":
        return shop(password)


def city_table(password):
    web = input("""
                1.  Select
                2.  Insert
                3.  Update
                4.  Delete
                0.  back
                >>>>>> """)
    if web == "1":
        print(City.select())
        back = input(f"""
                        0.  back
                        >>>> """)
        if back == "0":
            return city_table(password)

    elif web == "2":
        name = input("Country Name: ")
        print(City.insert(name))
        return city_table(password)

    elif web == "3":
        column = input("Column Name: ")
        old_name = input("Old Name: ")
        new_name = input("New Name: ")
        print(City.update(column, old_name, new_name, "city"))
        return city_table(password)

    elif web == "4":
        column = input("column name: ")
        name = input("Name: ")
        print(City.delete(column, name, "city"))
        return city_table(password)
    elif web == "0":
        return shop(password)


def address_table(password):
    web = input("""
                    1.  Select
                    2.  Insert
                    3.  Update
                    4.  Delete
                    0.  back
                    >>>>>> """)
    if web == "1":
        print(Address.select())
        return address_table(password)

    elif web == "2":
        name = input("Address Name : ")
        mfy_name = input("MFY Name : ")
        hous_number = input("House Number : ")
        print(Address.insert(name, mfy_name, hous_number))
        return address_table(password)

    elif web == "3":
        column = input("Column Name: ")
        name = input("City Name: ")
        new_name = input("New City Name: ")
        print(City.update(column, name, new_name, "address"))
        return address_table(password)

    elif web == "4":
        column = input("Column Name: ")
        name = input("City Name: ")
        print(City.delete(column, name, "address"))
        return address_table(password)

    elif web == "0":
        return shop(password)


def payment_status(password):
    web = input("""
            1.  Select
            2.  Insert
            3.  Update
            4.  Delete
            0.  back
            >>>>>> """)
    if web == "1":
        print(Status.select())
        back = input(f"""
                    0.  back
                    >>>> """)
        if back == "0":
            return payment_status(password)

    elif web == "2":
        name = input("payment name: ")
        print(Status.insert(name))
        return payment_status(password)

    elif web == "3":
        column = input("Column name: ")
        old_name = input("Old payment_status name: ")
        new_name = input("New payment_status name: ")
        print(Status.update(column, old_name, new_name, "payment"))
        return payment_status(password)

    elif web == "4":
        column = input("column name: ")
        name = input("payment name: ")
        print(Status.delete(column, name, "payment"))
        return payment_status(password)
    elif web == "0":
        return shop(password)


def haridor_table(password):
    web = input("""
                    1.  Select
                    2.  Insert
                    3.  Update
                    4.  Delete
                    0.  back
                    >>>>>> """)
    if web == "1":
        print(Haridor.select())
        back = input(f"""
                            0.  back
                            >>>> """)
        if back == "0":
            return haridor_table(password)

    elif web == "2":
        first_name = input("First name : ")
        phone_number = input("Phone number  : ")
        address_id = input("address_id  : ")
        persons_id = input("persons_id  : ")
        print(Haridor.insert(first_name, phone_number, address_id, persons_id))
        return haridor_table(password)

    elif web == "3":
        column = input("Column Name: ")
        old_name = input("City Name: ")
        new_name = input("New City Name: ")
        print(Haridor.update(column, old_name, new_name))
        return haridor_table(password)

    elif web == "4":
        column = input("Column Name: ")
        name = input("City Name: ")
        print(Haridor.delete(column, name))

    elif web == "0":
        return shop(password)


def market(password):
    web = input(f"""
                1.  Laptop
                2.  Phone
                3.  Buy market
                0.  Back
                """)
    if web == "1":
        print(classes.Laptop.select())
        back = input(f"""
                                0.  back
                                >>>> """)
        if back == "0":
            return market(password)
    elif web == "2":
        print(classes.Phone.select())
        return market(password)

    elif web == "3":
        buyurtma_name = input("Buyurtma Name : ")
        count = int(input("Count : "))
        color = input("Color: ")
        laptop_id = input("Laptop ID : ")
        phone_id = input("Phone ID : ")
        pay_id = input("Payment ID : ")
        address_id = input("Address ID : ")
        persons_id = input("Persons ID : ")
        print(classes.Product.insert(buyurtma_name, count, color, laptop_id, phone_id, pay_id, address_id, persons_id))
        return market(password)
    elif web == "0":
        return shop(password)
    else:
        print("Wrong input")
        return market(password)


def buyurtma(password):
    web = input(f"""
                1.  Buyurtmalar ruyhati
                0.  Back
                """)
    if web == "1":
        print(classes.Buyurtma.select())
        return buyurtma(password)
    elif web == "0":
        return shop(password)
