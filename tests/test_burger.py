import allure
import pytest

from data import Values
from unittest.mock import Mock
from praktikum.burger import Burger

from conftest import *

class TestBurger:
    # Тест на выбор булки
    def test_set_buns_successful(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    # Тест на добавление ингредиентов
    def test_add_ingredients_successful(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1

    # Тест на удаление ингредиентов
    def test_remove_ingredients_successful(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    # Тест на перемещение ингредиентов
    def test_move_ingredients_successful(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 2

    # Тест на получение цены бургера
    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        expected_price = Values.bun_price * 2 + Values.ingredient_price * 2

        assert burger.get_price() == expected_price

    # Тест на получение чека с рецептом бургера
    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_receipt() == Values.expected_receipt