class User:
    def __init__(self, user_id, name, access_level='user'):

    # Атрибуты с инкапсуляцией
        self._id = user_id
        self._name = name
        self._access_level = access_level

    # Методы для получения данных
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Методы для изменения данных
    def set_name(self, name):
        self._name = name

    def set_access_level(self, access_level):
        self._access_level = access_level

    # Представление объекта для удобного чтения
    def __str__(self):
        return f"User(ID: {self._id}, Имя: {self._name}, Доступ: {self._access_level})"

class Admin(User):
    def __init__(self, user_id, name, admin_access_level='admin'):
        # Инициализация атрибутов через родительский класс
        super().__init__(user_id, name, access_level=admin_access_level)
        # Личный список пользователей, которым управляет администратор
        self._user_list = []

    # Метод для добавления пользователя
    def add_user(self, user):
        if isinstance(user, User):  # Проверяем, что добавляем объект класса User
            self._user_list.append(user)
            print(f"Пользователь {user.get_name()} успешно добавлен.")
        else:
            print("Ошибка: Добавляемый объект не является экземпляром класса User.")

    # Метод для удаления пользователя
    def remove_user(self, user_id):
        # Ищем пользователя с нужным ID
        for user in self._user_list:
            if user.get_id() == user_id:
                self._user_list.remove(user)
                print(f"Пользователь с ID {user_id} удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    # Метод для отображения всех пользователей
    def show_users(self):
        if self._user_list:
            print("Список пользователей:")
            for user in self._user_list:
                print(f"- {user}")
        else:
            print("Список пользователей пуст.")

# Создаем администратора
admin = Admin(0, "SuperAdmin")

# Создаем пользователей
user1 = User(1, "Alice")
user2 = User(2, "Bob")
user3 = User(3, "Charlie")

# Администратор добавляет пользователей
admin.add_user(user1)
admin.add_user(user2)
admin.show_users()

# Администратор удаляет пользователя
admin.remove_user(2)
admin.show_users()

# Пытаемся удалить несуществующего пользователя
admin.remove_user(42)

