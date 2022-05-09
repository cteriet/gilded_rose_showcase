import pytest
from gilded_rose.gilded_rose import Item, GildedRose


def test_item_has_properties():
    item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
    assert hasattr(item, 'name') and hasattr(item, 'sell_in') and hasattr(item, 'quality')


def test_gilded_rose_has_item():
    gilded_rose = GildedRose([])

    assert hasattr(gilded_rose, 'items')
