from main import Database


class Admin:
    """Bu yerda adminlik huquqlari buyicha class
    admin qushish, adminlar ruyhati va h.k"""
    def __init__(self, first_name: str, last_name: str, phone_number: str, card: str, password: str, money: float):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.card = card
        self.password = password
        self.money = money

    @staticmethod
    def select():
        query = f"SELECT * FROM admin order by id"
        # return Database.connect(query, "select")
        data = Database.connect(query, "select")
        for row in data:
            print(row)

    @staticmethod
    def insert(first_name, last_name, phone_number, password, card, money):
        query = f"""
                insert into admin(first_name, last_name, phone_number, password, card, money) 
                values('{first_name}', '{last_name}', '{phone_number}', '{password}', '{card}', '{money}')
                    """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, old_name, new_name):
        query = f"""
                    update admin set {column} = '{new_name}' where {column} = '{old_name}'
                        """
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name):
        query = f"""
                        delete from admin where {column} = '{name}'
                        """
        return Database.connect(query, "delete")


class User:
    """
    Bu yerda user yani foydalanuvchilar
    ruyhati va foydalanuvchilar ruyhatdan o'tishi
    """
    def __init__(self, first_name: str, last_name: str, phone_number: str, card: str, password: str, money: float):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.card = card
        self.password = password
        self.money = money

    @staticmethod
    def select(password):
        query = f"SELECT * FROM persons where password = '{password}'"
        # return Database.connect(query, "select")
        data = Database.connect(query, "select")
        for row in data:
            print(row)

    @staticmethod
    def insert(first_name, last_name, phone_number, password, card, money):
        query = f"""
                insert into persons(first_name, last_name, phone_number, password, card, money) 
                values('{first_name}', '{last_name}', '{phone_number}', '{password}', '{card}', '{money}')
                    """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, old_name, new_name):
        query = f"""
                    update persons set {column} = '{new_name}' where {column} = '{old_name}'
                        """
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name):
        query = f"""
                        delete from persons where {column} = '{name}'
                        """
        return Database.connect(query, "delete")


class Users:
    """
    Bu yerda foydalanuvchilarni admin ruyhatini
    ko'rish , o'chirish, uzgartirish huquqlari berilgan class
    """
    @staticmethod
    def select():
        query = f"SELECT * FROM persons order by id"
        # return Database.connect(query, "select")
        data = Database.connect(query, "select")
        for row in data:
            print(row)

    @staticmethod
    def update(column, old_name, new_name):
        query = f"""
                        update persons set {column} = '{new_name}' where {column} = '{old_name}'
                            """
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name):
        query = f"""
                        delete from persons where {column} = '{name}'
                        """
        return Database.connect(query, "delete")

    @staticmethod
    def search_name(search):
        query = f"SELECT * FROM persons WHERE name like '%{search}%'"
        return Database.connect(query, query_type='select')


class Country:
    """
    Bu yerda country yani foydalanuvchilar Davlatini kiritish buyicha class
    """
    def __init__(self, name):
        self.name = name

    @staticmethod
    def select():
        query = f"SELECT * FROM country order by id"
        # return Database.connect(query, "select")
        data = Database.connect(query, "select")
        for row in data:
            print(row)

    @staticmethod
    def insert(name):
        query = f"""
                insert into country(name) values('{name}')
                    """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, old_name, new_name, table):
        query = f"""
                    update {table} set {column} = '{new_name}' where {column} = '{old_name}'
                        """
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name, table):
        query = f"""
                        delete from {table} where {column} = '{name}'
                        """
        return Database.connect(query, "delete")


class City(Country):
    """
    Bu yerda city yani foydalanuvchilar shaharni kiritish buyicha class
    """
    def __init__(self, name, country_id):
        Country.__init__(self, name)
        self.country_id = country_id

    @staticmethod
    def select():
        query = "SELECT * FROM city order by id"
        # return Database.connect(query, "select")
        data = Database.connect(query, "select")
        for row in data:
            print(row)

    @staticmethod
    def insert(name):
        query = f"""
                insert into city(name) values('{name}')
                    """
        return Database.connect(query, "insert")


class Address(Country):
    """
    Bu yerda address yani foydalanuvchilar manzilini kiritish
    """
    def __init__(self, name, mfy_name, hous_number):
        Country.__init__(self, name)
        self.mfy_name = mfy_name
        self.hous_number = hous_number

    @staticmethod
    def select():
        query = "SELECT * FROM address order by id"
        # return Database.connect(query, "select")
        data = Database.connect(query, "select")
        for row in data:
            print(row)

    @staticmethod
    def insert(name, mfy_name, hous_number):
        query = f"""
                insert into address(name, mfy_name, hous_number) values('{name}', '{mfy_name}', '{hous_number}')
                    """
        return Database.connect(query, "insert")


class Status(Country):
    """
    Bu yerda status yani foydalanuvchilar buyurtmalari uchun qanday
    to'lov yani karta nomi
    """
    def __init__(self, name):
        Country.__init__(self, name)
        self.name = name

    @staticmethod
    def select():
        query = "SELECT * FROM payment order by id"
        # return Database.connect(query, "select")
        data = Database.connect(query, "select")
        for row in data:
            print(row)

    @staticmethod
    def insert(name):
        query = f"""
                   insert into payment(name) values('{name}')
                       """
        return Database.connect(query, "insert")


class Haridor:
    """
    Bu yerda foydalanuvchilarning ruyhatini ko'rish adminlar uchun
    Yani har bir foydalanuvchi ruyhatdan o'tgan bilan mahsulot harid qilmasligi mumkun
    Shu sababdan harid qilmasdan oldin first_name, last_name phone_number, address
    suraladi sabab buyurtma yetkazilishi uchun kimga qayerga borishini bilishi kerak admin
    """
    def __init__(self, first_name: str, last_name: str, phone_number, address_id, persons_id):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address_id = address_id
        self.persons_id = persons_id

    @staticmethod
    def select():
        query = "SELECT * FROM haridor order by id"
        # return Database.connect(query, "select")
        data = Database.connect(query, "select")
        for row in data:
            print(row)

    @staticmethod
    def insert(first_name, phone_number, address_id, persons_id):
        query = f""" insert into haridor(first_name, phone_number, address_id, persons_id) 
                   values('{first_name}', '{phone_number}', '{address_id}', '{persons_id}')
                       """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, old_name, new_name):
        query = f"""
                    update haridor set {column} = '{new_name}' where {column} = '{old_name}'
                        """
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name):
        query = f"""
                        delete from haridor where {column} = '{name}'
                        """
        return Database.connect(query, "delete")


class Laptop:
    """
    Bu class faqat adminlar uchun huquq berilgan admin tamonidan mahsulotni
    bozorga chiqarish uchun class
    """
    def __init__(self, name, price, description, count, serial_number, admin_id):
        self.name = name
        self.price = price
        self.description = description
        self.count = count
        self.serial_number = serial_number
        self.admin_id = admin_id

    @staticmethod
    def select():
        query = "SELECT * FROM laptop order by id"
        data = Database.connect(query, "select")
        for row in data:
            print(row)

    @staticmethod
    def insert(name, price, description, count, serial_number, admin_id):
        query = f"""
                           insert into laptop(name, price, description, count, serial_number, admin_id) 
                           values('{name}', '{price}', '{description}', '{count}', '{serial_number}', '{admin_id}')
                               """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, old_name, new_name, table):
        query = f"""
                    update {table} set {column} = '{new_name}' where {column} = '{old_name}'
                        """
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name, table):
        query = f"""
                        delete from {table} where {column} = '{name}'
                        """
        return Database.connect(query, "delete")

    @staticmethod
    def search_name(search):
        query = f"SELECT * FROM laptop WHERE name like '%{search}%'"
        return Database.connect(query, query_type='select')


class Phone(Laptop):
    def __init__(self, name, price, description, count, serial_number, admin_id):
        Laptop.__init__(self, name, price, description, count, serial_number, admin_id)
        self.name = name
        self.price = price
        self.description = description
        self.count = count
        self.serial_number = serial_number
        self.admin_id = admin_id

    @staticmethod
    def select():
        query = "SELECT * FROM phone order by id"
        data = Database.connect(query, "select")
        for row in data:
            print(row)

    @staticmethod
    def insert(name, price, description, count, serial_number, admin_id):
        query = f"""
                           insert into phone(name, price, description, count, serial_number, admin_id) 
                           values('{name}', '{price}', '{description}', '{count}', '{serial_number}', '{admin_id}')
                               """
        return Database.connect(query, "insert")

    @staticmethod
    def search_name(search):
        query = f"SELECT * FROM phone WHERE name like '%{search}%'"
        return Database.connect(query, query_type='select')


class Product:
    """
    Bu class foydalanuvchi buyurtma berishi uchun
    """
    def __init__(self, name, count, color, laptop_id, phone_id, payment_id, address_id, persons_id):
        self.name = name
        self.count = count
        self.color = color
        self.laptop_id = laptop_id
        self.phone_id = phone_id
        self.payment_id = payment_id
        self.address_id = address_id
        self.persons_id = persons_id

    @staticmethod
    def select(password):
        query = f"SELECT * FROM buyurtma where password = '{password}'"
        # return Database.connect(query, "select")
        data = Database.connect(query, "select")
        for row in data:
            print(row)

    @staticmethod
    def insert(buyurtma_name, count, color, laptop_id, phone_id, pay_id, address_id, persons_id):
        query = f"""
                       insert into buyurtma(buyurtma_name, count, color, laptop_id, phone_id, pay_id, address_id, persons_id) 
                       values('{buyurtma_name}', '{count}', '{color}', '{laptop_id}', '{phone_id}', '{pay_id}', '{address_id}', '{persons_id}')
                           """
        return Database.connect(query, "insert")


class Buyurtma:
    def __init__(self, name, count, color, laptop_id, phone_id, payment_id, address_id, persons_id):
        self.name = name
        self.count = count
        self.color = color
        self.laptop_id = laptop_id
        self.phone_id = phone_id
        self.payment_id = payment_id
        self.address_id = address_id
        self.persons_id = persons_id

    @staticmethod
    def select():
        query = "SELECT * FROM buyurtma order by id"
        data = Database.connect(query, "select")
        for row in data:
            print(row)

    @staticmethod
    def search_name(search):
        query = f"SELECT * FROM buyurtma WHERE name like '%{search}%'"
        return Database.connect(query, query_type='select')

