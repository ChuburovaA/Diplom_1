import pytest

from unittest.mock import Mock
from data import Values

@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_price.return_value = Values.bun_price
    mock_bun.get_name.return_value = Values.bun_name

    return mock_bun

@pytest.fixture(scope='function')
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = Values.ingredient_price
    mock_ingredient.get_name.return_value = Values.ingredient_name
    mock_ingredient.get_type.return_value = Values.ingredient_type

    return mock_ingredient