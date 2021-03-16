TOTAL_CHARACTERS = "SELECT COUNT(*) FROM charactercreator_character AS cc_char"
TOTAL_SUBCLASS = "SELECT * FROM subclass_counts"
TOTAL_ITEMS = "SELECT COUNT(*) FROM armory_item"
WEAPONS = "SELECT COUNT(*) FROM armory_weapon"
NON_WEAPONS = "SELECT COUNT(*) FROM armory_item as item LEFT JOIN armory_weapon as weapon ON weapon.item_ptr_id = item.item_id WHERE item_ptr_id IS NULL"
CHARACTER_ITEMS = "SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory GROUP BY character_id"
CHARACTER_WEAPONS = "SELECT character_id, COUNT(item_ptr_id) as number_of_weapons FROM armory_weapon as weapon LEFT JOIN charactercreator_character_inventory as cc_char_inv ON weapon.item_ptr_id = cc_char_inv.item_id GROUP BY character_id"
AVG_CHARACTER_ITEMS = "SELECT AVG(number_of_items) FROM(SELECT COUNT(item_id) as number_of_items FROM charactercreator_character_inventory GROUP BY character_id)"
AVG_CHARACTER_WEAPONS = "SELECT AVG(number_of_weapons) FROM(SELECT COUNT(item_ptr_id) as number_of_weapons FROM armory_weapon as weapon LEFT JOIN charactercreator_character_inventory as cc_char_inv ON weapon.item_ptr_id = cc_char_inv.item_id GROUP BY character_id)"

all_queries = [TOTAL_CHARACTERS, TOTAL_SUBCLASS, TOTAL_ITEMS, WEAPONS, NON_WEAPONS, CHARACTER_ITEMS, CHARACTER_WEAPONS, AVG_CHARACTER_ITEMS, AVG_CHARACTER_WEAPONS]
