from Menu import Menu
from Order import Order
from MenuRepository import MenuRepository


def test_set_menu_item():
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Test 1", 10)
    menu2 = Menu(2, "Test 2", 5)
    menu3 = Menu(3, "Test 3", 2)
    # Act

    menu_repository.set_menu_item(menu1)
    menu_repository.set_menu_item(menu2)

    # Assert
    assert len(menu_repository.menu_itens) == 2
    assert not menu3 in menu_repository.menu_itens
    assert type(menu_repository.menu_itens) == list


def test_check_if_itens_exists():
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Test 1", 10)
    order1 = Order(1,2)
    order2 = Order(9,2)
    # Act

    menu_repository.set_menu_item(menu1)
    resultOK = menu_repository.check_if_itens_exists(order1)
    resultNOK = menu_repository.check_if_itens_exists(order2)

    # Assert
    assert len(menu_repository.menu_itens) == 1
    assert resultOK == True
    assert resultNOK == False
