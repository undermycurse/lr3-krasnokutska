from main import User, Dish, Menu
import pytest


def test_register_valid_email():
    user = User(1, "Maria", "maria@gmail.com", "1234")
    assert user.register() == True


def test_register_invalid_email():
    user = User(1, "Maria", "mariagmail.com", "1234")

    with pytest.raises(ValueError):
        user.register()


def test_login_success():
    user = User(1, "Maria", "maria@gmail.com", "1234")
    assert user.login("1234") == True


def test_login_fail():
    user = User(1, "Maria", "maria@gmail.com", "1234")
    assert user.login("wrong") == False


def test_add_dish():
    menu = Menu(1, "Main Menu")
    dish = Dish(1, "Pizza", 250, "Cheese pizza")

    menu.add_dish(dish)

    assert len(menu.dishes) == 1


def test_generate_qr():
    menu = Menu(1, "Main Menu")
    assert menu.generate_qr_code() == "QR-1"


def test_dish_get_info():
    dish = Dish(1, "Pizza", 250, "Cheese pizza")
    assert dish.get_info() == "Pizza - 250 грн"


def test_add_invalid_dish():
    menu = Menu(1, "Main Menu")

    with pytest.raises(TypeError):
        menu.add_dish("not a dish")


def test_qr_code_generate():
    from main import QRCode

    qr = QRCode(1, "https://menuqr.com/menu/1")
    assert qr.generate() == "Generated: https://menuqr.com/menu/1"

    def test_login_empty_password():
        # Arrange
        user = User(1, "Maria", "maria@gmail.com", "1234")
    
        # Act
        result = user.login("")
    
        # Assert
        assert result == False 