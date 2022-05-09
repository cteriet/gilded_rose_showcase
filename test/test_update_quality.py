import pytest
from gilded_rose.gilded_rose import GildedRoseItem, GildedRose


@pytest.mark.parametrize("input, expected", [
    # Test if quality decreases by 1 under normal circumstances and cap out a 0
    (GildedRoseItem(name="+5 Dexterity Vest", sell_in=10, quality=20, rarity_type='Common', item_type='General'), 19),
    (GildedRoseItem(name="+5 Dexterity Vest", sell_in=10, quality=0, rarity_type='Common', item_type='General'), 0),

    # Test if quality decreases by 2 for conjured items
    (GildedRoseItem(name="Conjured Mana Cake", sell_in=3, quality=6, rarity_type='Common', item_type='Conjured'), 4),

    # Test if quality deceases twice as fast, if sell_in < 0
    (GildedRoseItem(name="Elixir of the Mongoose",
                    sell_in=-1, quality=10, rarity_type='Common', item_type='General'), 8),
    (GildedRoseItem(name="Conjured Mana Cake",
                    sell_in=-1, quality=10, rarity_type='Common', item_type='Conjured'), 6),

    # Test if 'Fermented' items increase in quality and cap out at 50
    (GildedRoseItem(name="Aged Brie", sell_in=2, quality=0, rarity_type='Common', item_type='Fermented'), 1),
    (GildedRoseItem(name="Aged Brie", sell_in=2, quality=50, rarity_type='Common', item_type='Fermented'), 50),

    # Test if 'Legendary' items don't decrease in quality and aren't resetted to 50
    (GildedRoseItem(name="Sulfuras, Hand of Ragnaros",
                    sell_in=0, quality=80, rarity_type='Legendary', item_type='General'), 80),
    (GildedRoseItem(name="Sulfuras, Hand of Ragnaros",
                    sell_in=-1, quality=80, rarity_type='Legendary', item_type='General'), 80),

    # Test if 'Ticket' items increase by (1, 2, 3) as sell_in value is  (>10, <=10, <=5), and drop to 0 if sell_in<0
    (GildedRoseItem(name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=15, quality=20, rarity_type='Common', item_type='Ticket'), 21),
    (GildedRoseItem(name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=10, quality=20, rarity_type='Common', item_type='Ticket'), 22),
    (GildedRoseItem(name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=5, quality=20, rarity_type='Common', item_type='Ticket'), 23),
    (GildedRoseItem(name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=-1, quality=20, rarity_type='Common', item_type='Ticket'), 0)
])
def test_update_quality(input, expected):
    assert GildedRose.calculate_new_item_quality(input) is expected


def test_update_item():
    test_item = GildedRoseItem(name="+5 Dexterity Vest",
                               sell_in=10, quality=20, rarity_type='Common', item_type='General')

    test_item = GildedRose.update_item(test_item)

    expected_output = GildedRoseItem(name="+5 Dexterity Vest",
                                     sell_in=9, quality=19, rarity_type='Common', item_type='General')

    assert test_item == expected_output


