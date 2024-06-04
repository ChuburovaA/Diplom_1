from praktikum.ingredient import Ingredient
from data import Values

# Тесты на Ингредиенты
class TestIngredient:

    # Тест на получение цены ингредиента
    def test_get_price(self):
        ingredient = Ingredient(
            Values.ingredient_type,
            Values.ingredient_name,
            Values.ingredient_price
        )

        assert ingredient.get_price() == Values.ingredient_price

    # Тест на получение имени ингредиента
    def test_get_name(self):
        ingredient = Ingredient(
            Values.ingredient_type,
            Values.ingredient_name,
            Values.ingredient_price
        )

        assert ingredient.get_name() == Values.ingredient_name

    # Тест на получение типа ингредиента
    def test_get_type(self):
        ingredient = Ingredient(
            Values.ingredient_type,
            Values.ingredient_name,
            Values.ingredient_price
        )

        assert ingredient.get_type() == Values.ingredient_type