import sqlite3
import os


def create_and_populate_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS store (
        store_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        code TEXT PRIMARY KEY,
        title TEXT NOT NULL
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        category_code TEXT,
        unit_price REAL,
        stock_quantity INTEGER,
        store_id INTEGER,
        FOREIGN KEY (category_code) REFERENCES categories(code),
        FOREIGN KEY (store_id) REFERENCES store(store_id)
    )""")


    stores = [(1, 'Asia'), (2, 'Globus'), (3, 'Spar')]
    categories = [('FD', 'Food products'), ('HH', 'Household goods')]
    products = [
        (1, 'Chocolate', 'FD', 10.5, 129, 1),
        (2, 'Milk', 'FD', 2.5, 200, 2),
        (3, 'Soap', 'HH', 1.2, 300, 3)
    ]

    cursor.executemany("INSERT OR IGNORE INTO store (store_id, title) VALUES (?, ?)", stores)
    cursor.executemany("INSERT OR IGNORE INTO categories (code, title) VALUES (?, ?)", categories)
    cursor.executemany(
        "INSERT OR IGNORE INTO products (id, title, category_code, unit_price, stock_quantity, store_id) VALUES (?, ?, ?, ?, ?, ?)",
        products)

    conn.commit()
    conn.close()
    print("База данных успешно создана и заполнена данными.")


def show_stores(cursor):
    cursor.execute("SELECT store_id, title FROM store")
    print("Выберите id магазина (0 для выхода):")
    for store_id, title in cursor.fetchall():
        print(f"{store_id}. {title}")


def show_products(cursor, store_id):
    cursor.execute("""
        SELECT products.title, categories.title, products.unit_price, products.stock_quantity
        FROM products
        JOIN categories ON products.category_code = categories.code
        WHERE products.store_id = ?
    """, (store_id,))
    products = cursor.fetchall()

    if products:
        for title, category, price, quantity in products:
            print(f"Продукт: {title}, Категория: {category}, Цена: {price}, Количество: {quantity}\n")
    else:
        print("Продукты не найдены.")


def main():

    if not os.path.exists("database.db"):
        create_and_populate_database()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    while True:
        show_stores(cursor)
        store_id = input("Введите id магазина: ")

        if store_id == '0':
            print("Выход.")
            break
        elif store_id.isdigit():
            show_products(cursor, int(store_id))
        else:
            print("Некорректный id.")

    conn.close()


if __name__ == "__main__":
    main()