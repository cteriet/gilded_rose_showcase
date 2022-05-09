# -*- coding: utf-8 -*-
import pytest
from gilded_rose.gilded_rose import ItemType, RarityType


def test_rarity_type():
    with pytest.raises(ValueError):
        RarityType('lskdfjlsdkjflskdfjlkdsj')


def test_required_rarity_types():
    required_types = {'Poor',
                      'Common',
                      'Uncommon',
                      'Rare',
                      'Epic',
                      'Legendary',
                      'Artifact'}

    assert RarityType.allowed_types.issubset(required_types)


def test_item_type():
    with pytest.raises(ValueError):
        ItemType('lskdfjlsdkjflskdfjlkdsj')


def test_required_item_types():
    required_types = {
        'General',
        'Fermented',
        'Ticket',
        'Conjured'
    }

    assert ItemType.allowed_types.issubset(required_types)


