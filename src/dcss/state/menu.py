from enum import Enum


class Menu(Enum):
    NO_MENU = 1
    CHARACTER_CREATION_SELECT_SPECIES = 2
    CHARACTER_CREATION_SELECT_BACKGROUND = 3
    CHARACTER_CREATION_SELECT_WEAPON = 4
    CHARACTER_INVENTORY_MENU = 5
    CHARACTER_ITEM_SPECIFIC_MENU = 6
    TUTORIAL_SELECTION_MENU = 7
    SPRINT_MAP_SELECTION_MENU = 8
    ABILITY_MENU = 9
    ALL_SPELLS_MENU = 10
    SKILL_MENU = 11
    ATTRIBUTE_INCREASE_TEXT_MENU = 12
    WALK_INTO_TELEPORT_TRAP_TEXT_MENU = 13
    EXAMINE_MAP_MENU = 14
    INDIVIDUAL_INVENTORY_ITEM_MENU = 15
    SCROLL_OF_IDENTIFY_MENU = 16
