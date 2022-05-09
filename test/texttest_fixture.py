# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from gilded_rose.gilded_rose import *

if __name__ == "__main__":
    days = 2
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1

    items = [
        GildedRoseItem(name="+5 Dexterity Vest", sell_in=10, quality=20, rarity_type='Common', item_type='General'),
        GildedRoseItem(name="Conjured Mana Cake", sell_in=3, quality=30, rarity_type='Common', item_type='Conjured'),
        GildedRoseItem(name="Aged Brie", sell_in=2, quality=45, rarity_type='Common', item_type='Fermented'),
        GildedRoseItem(name="Sulfuras, Hand of Ragnaros",
                       sell_in=0, quality=80, rarity_type='Legendary', item_type='General'),
        GildedRoseItem(name="Backstage passes to a TAFKAL80ETC concert",
                       sell_in=15, quality=20, rarity_type='Common', item_type='Ticket')
            ]

    gilded_rose = GildedRose(items)

    print ("OMGHAI!")
    for day in range(days):

        print("-------- day %s --------" % day)
        print(f"{'name':<45} {'sellIn':<10} {'quality':<10} {'itemType':<10} {'rarityType':<10}")
        for item in items:
            print(f"{item.name:<45} {item.sell_in:<10} {item.quality:<10} {item.item_type.value:<10} {item.rarity_type.value:<10}")
        print("")

        gilded_rose.update_quality()
