import sqlite3


conn = sqlite3.connect('hw.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL CHECK (LENGTH(product_title) <= 200),
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
''')

# Функция для добавления товаров
def add_products():
    products = [
        ("Мыло", 10.99, 20),
        ("Шампунь", 15.49, 30),
        ("Гель для душа", 12.99, 25),
        ("Зубная паста", 5.99, 40),
        ("Лосьон", 18.49, 15),
        ("Крем", 20.00, 10),
        ("Маска для лица", 9.99, 5),
        ("Мыло жидкое", 11.49, 12),
        ("Дезодорант", 7.99, 18),
        ("Косметичка", 14.99, 8),
        ("Бритва", 6.49, 22),
        ("Масло для тела", 17.99, 9),
        ("Скраб", 13.49, 16),
        ("Тонер", 8.99, 11),
        ("Парфюм", 25.00, 3),
        ("Лак для ногтей", 4.99, 14)
    ]
    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)
    conn.commit()

# Функция для изменения количества товара по id
def update_quantity(product_id, quantity):
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (quantity, product_id))
    conn.commit()

# Функция для изменения цены товара по id
def update_price(product_id, price):
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (price, product_id))
    conn.commit()

# Функция для удаления товара по id
def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()

# Функция для вывода всех товаров
def print_all_products():
    cursor.execute('SELECT * FROM products')
    for row in cursor.fetchall():
        print(row)

# Функция для поиска дешевых товаров с достаточным количеством
def find_cheap_products():
    cursor.execute('SELECT * FROM products WHERE price < 100 AND quantity > 5')
    for row in cursor.fetchall():
        print(row)

# Функция для поиска товаров по названию
def search_products_by_title(search_term):
    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%' + search_term + '%',))
    for row in cursor.fetchall():
        print(row)


add_products()
print_all_products()
update_quantity(1, 50)
update_price(1, 12.99)
delete_product(2)
print_all_products()
find_cheap_products()
search_products_by_title('мыло')


conn.close()
