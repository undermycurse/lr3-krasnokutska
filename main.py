class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def register(self):
        if "@" not in self.email:
            raise ValueError("Invalid email")
        return True

    def login(self, password):
        return self.password == password


class Dish:
    def __init__(self, dish_id, name, price, description):
        self.dish_id = dish_id
        self.name = name
        self.price = price
        self.description = description

    def get_info(self):
        return f"{self.name} - {self.price} грн"


class Menu:
    def __init__(self, menu_id, title):
        self.menu_id = menu_id
        self.title = title
        self.dishes = []

    def add_dish(self, dish):
        if not isinstance(dish, Dish):
            raise TypeError("Only Dish objects allowed")
        self.dishes.append(dish)

    def generate_qr_code(self):
        return f"QR-{self.menu_id}"


class QRCode:
    def __init__(self, qr_id, qr_link):
        self.qr_id = qr_id
        self.qr_link = qr_link

    def generate(self):
        return f"Generated: {self.qr_link}"


if __name__ == "__main__":
    user = User(1, "Maria", "maria@gmail.com", "1234")
    user.register()

    dish = Dish(1, "Pizza", 250, "Cheese pizza")

    menu = Menu(1, "Main Menu")
    menu.add_dish(dish)

    print(dish.get_info())
    print(menu.generate_qr_code())