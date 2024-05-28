from main import Database


def create_table():
    admin = f"""
                create table admin(
                    id serial primary key,
                    first_name varchar(50),
                    last_name varchar(50),
                    password char(15),
                    phone_number varchar(20),
                    card char(20),
                    money numeric,
                    create_date timestamp default now());
                    """

    persons = f"""
                create table persons(
                    id serial primary key,
                    first_name varchar(50),
                    last_name varchar(50),
                    password char(15),
                    card char(20),
                    money numeric,
                    phone_number varchar(20),
                    bith_day date,
                    create_date timestamp default now());
                    """

    payment_type = f"""
                create table payment(
                    id serial primary key,
                    name varchar(50),
                    create_date timestamp default now());"""

    laptop = f"""
                create table laptop(
                    id serial primary key,
                    name varchar(50),
                    price numeric,
                    description varchar,
                    count smallint,
                    serial_number varchar(50),
                    admin_id int references admin(id),
                    create_date timestamp default now());"""

    phone = f"""
                create table phone(
                    id serial primary key,
                    name varchar(50),
                    price numeric,
                    description varchar,
                    count smallint,
                    serial_number varchar(50),
                    admin_id int references admin(id),
                    create_date timestamp default now());"""

    country = f"""
                create table country(
                    id serial primary key,
                    name varchar(50),
                    create_date timestamp default now());"""

    city = f"""
                create table city(
                    id serial primary key,
                    name varchar(50),
                    create_date timestamp default now());"""

    address = f"""
                create table address(
                    id serial primary key,
                    name varchar(50),
                    mfy_name varchar(50),
                    hous_number char(30),
                    create_date timestamp default now());"""

    haridor = f"""
                create table haridor(
                    id serial primary key,
                    first_name varchar(50),
                    phone_number char(20),
                    address int references address(id),
                    persons_id int references persons(id),
                    create_date timestamp default now());"""

    buyurtma = f"""
                create table buyurtma(
                    id serial primary key,
                    buyurtma_name varchar(50),
                    count smallint,
                    color varchar(20),
                    laptop_id int references laptop(id),
                    phone_id int references phone(id),
                    pay_id int references payment(id),
                    address_id int references address(id),
                    persons_id int references persons(id),
                    create_date timestamp default now());"""

    data = {
        'admin': admin,
        'persons': persons,
        'payment_type': payment_type,
        'laptop': laptop,
        'phone': phone,
        'country': country,
        'city': city,
        'address': address,
        'haridor': haridor,
        'buyurtma': buyurtma
    }
    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")

