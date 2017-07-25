#from products_app.py import enlarage
from app.products_app import *


def test_enlarage():
    result = enlarage(3)
    assert result
