from praktikum.database import Database

# Тесты на базу данных
class TestDatabase:
    # Тест на получение базы данных булок
    def test_available_buns(self):
        database = Database()

        assert len(database.available_buns()) == 3
        assert database.available_buns()[1].get_name() == "white bun"
        assert database.available_buns()[1].get_price() == 200

    # Тест на получение базы данных ингредиентов
    def test_available_ingredients(self):
        database = Database()

        assert len(database.available_ingredients()) == 6
        assert database.available_ingredients()[1].get_name() == 'sour cream'
        assert database.available_ingredients()[1].get_price() == 200