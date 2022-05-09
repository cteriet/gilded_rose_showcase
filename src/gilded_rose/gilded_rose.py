# -*- coding: utf-8 -*-
from dataclasses import dataclass


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


@dataclass
class ItemType:
    value: str
    allowed_types = {
        'General',
        'Fermented',
        'Ticket',
        'Conjured'
    }

    def __post_init__(self):
        if self.value not in self.allowed_types:
            raise ValueError("The specified item is of an unknown type!")


@dataclass
class RarityType:
    value: str
    allowed_types = {
        'Poor',
        'Common',
        'Uncommon',
        'Rare',
        'Epic',
        'Legendary',
        'Artifact'
    }

    def __post_init__(self):
        if self.value not in self.allowed_types:
            raise ValueError("The specified rarity is of an unknown type!")


@dataclass
class GildedRoseItem(Item):
    def __init__(self, name: str, sell_in: int, quality: int, item_type: str, rarity_type: str):
        super(GildedRoseItem, self).__init__(name, sell_in, quality)
        self.item_type = ItemType(item_type)
        self.rarity_type = RarityType(rarity_type)

    def __repr__(self):
        return f"{self.name} {self.sell_in} {self.quality} {self.item_type.value} {self.rarity_type.value}"


class GildedRose:
    def __init__(self, items: list):
        self.items = items

    @staticmethod
    def item_type_factor(sell_in: int, item_type: ItemType) -> int:
        match item_type.value:
            case 'Fermented':
                return -1
            case 'Ticket':
                if sell_in < 0:
                    return 0
                elif sell_in <= 5:
                    return -3
                elif sell_in <= 10:
                    return -2
                else:
                    return -1
            case 'Conjured':
                return 2
            case _:
                return 1

    @staticmethod
    def sell_in_factor(sell_in: int, item_type: ItemType) -> int:
        match item_type.value:
            case 'Fermented':
                return 1
            case _:
                return 2 if sell_in < 0 else 1

    @staticmethod
    def rarity_type_factor(rarity_type: RarityType) -> int:
        match rarity_type.value:
            case 'Legendary' | 'Artifact':
                return 0
            case _:
                return 1

    @staticmethod
    def calculate_new_item_quality(item: GildedRoseItem) -> int:

        # If Legendary or Artifact item, return original quality
        # TODO: Check with Alison if Legendary/Artifact tickets also keep their value
        if item.rarity_type.value in ['Legendary', 'Artifact']:
            return item.quality

        # If expired ticket, return 0
        if item.item_type.value == 'Ticket' and item.sell_in < 0:
            return 0

        update_factor = (GildedRose.item_type_factor(item.sell_in, item.item_type) *
                         GildedRose.rarity_type_factor(item.rarity_type) *
                         GildedRose.sell_in_factor(item.sell_in, item.item_type))

        # Calculate the new quality, and restrict to [0,50]
        return min(50, max(0, item.quality - update_factor))

    @staticmethod
    def update_item(item: GildedRoseItem) -> GildedRoseItem:
        item.quality = GildedRose.calculate_new_item_quality(item)
        item.sell_in -= 1

        return item

    def update_quality(self):
        self.items = list(map(self.update_item, self.items))
