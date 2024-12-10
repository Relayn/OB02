class Product:
    def __init__(self, product_id, name, price):
        # Инкапсуляция атрибутов
        self._product_id = product_id
        self._name = name
        self._price = price

    # Методы для получения данных
    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    # Метод для изменения цены с проверкой
    def set_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative!")
        self._price = new_price

    # Удобное представление объекта
    def __str__(self):
        return f"Product(ID: {self._product_id}, Name: {self._name}, Price: ${self._price:.2f})"

# Создаем товар
product = Product(1, "Laptop", 1000)

# Получаем данные
print(product.get_name())  # Laptop
print(product.get_price())  # 1000

# Обновляем цену
product.set_price(1200)
print(product.get_price())  # 1200

# Вывод объекта
print(product)  # Product(ID: 1, Name: Laptop, Price: $1200.00)

# Попытка установить отрицательную цену
try:
    product.set_price(-500)
except ValueError as e:
    print(e)  # Price cannot be negative!
