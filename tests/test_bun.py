import pytest
from praktikum.bun import Bun

class TestBun:

    # Тест на получение названия модели булки
    @pytest.mark.parametrize('name',
                             [
                                 "Космическая булка",
                                 "Млечная булка",
                                 "Булка созвездий"
                             ])
    def test_get_name(self, name):
        bun = Bun(name, 1022)

        assert bun.get_name() == name

    # Тест на получение цены модели булки
    @pytest.mark.parametrize('price',
                             [
                                 123456,
                                 1234.123,
                                 123-123,
                                 123+123
                             ])
    def test_get_price(self, price):
        bun = Bun('Космическая булка', price)

        assert bun.get_price() == price