from dcss.actions.command import Command
from dcss.actions.menuchoice import MenuChoice
import string


class Action:
    """
    This class represents an action that the agent can take.

    This file contains messages for key actions and text inputs to be
    sent to webserver, including:
    * moving around
    * accessing the inventory
    * using items
    * ... etc


    These keycodes were identified manually be testing commands using
    Chrome's develop tools and observing the communications sent through
    the websockets.


    """

    command_to_msg = {
        # Command.NOTHING: None,
        Command.MOVE_OR_ATTACK_N: {'msg': 'key', "keycode": -254},  # <up>
        Command.MOVE_OR_ATTACK_S: {'msg': 'key', "keycode": -253},  # <down>
        Command.MOVE_OR_ATTACK_E: {'msg': 'key', "keycode": -251},  # <right>
        Command.MOVE_OR_ATTACK_W: {'msg': 'key', "keycode": -252},  # <left>
        Command.MOVE_OR_ATTACK_NW: {'msg': 'key', "keycode": -249},  # <home>
        Command.MOVE_OR_ATTACK_SW: {'msg': 'key', "keycode": -248},  # <end>
        Command.MOVE_OR_ATTACK_SE: {'msg': 'key', "keycode": -245},  # <pgDown>
        Command.MOVE_OR_ATTACK_NE: {'msg': 'key', "keycode": -246},  # <pgUp>

        Command.REST_AND_LONG_WAIT: {'msg': 'key', 'keycode': ord('5')},
        Command.WAIT_1_TURN: {'msg': 'key', 'keycode': ord('.')},

        Command.AUTO_EXPLORE: {'msg': 'key', 'keycode': ord('o')},
        # Command.INTERLEVEL_TRAVEL: {'text': 'G', 'msg': 'input'},
        # Command.FIND_ITEMS: {'msg': 'key', "keycode": 6},
        #  Todo - see github issue 9
        # Command.SET_WAYPOINT: {...}

        # Command.LONG_WALK_N: {'msg': 'key', "keycode": -243},
        # Command.LONG_WALK_S: {'msg': 'key', "keycode": -242},
        # Command.LONG_WALK_E: {'msg': 'key', "keycode": -240},
        # Command.LONG_WALK_W: {'msg': 'key', "keycode": -241},
        # Command.LONG_WALK_NW: {'msg': 'key', "keycode": -238},
        # Command.LONG_WALK_NE: {'msg': 'key', "keycode": -235},
        # Command.LONG_WALK_SW: {'msg': 'key', "keycode": -237},
        # Command.LONG_WALK_SE: {'msg': 'key', "keycode": -234},

        Command.ATTACK_WITHOUT_MOVE_N: {'msg': 'key', "keycode": -232},  # <ctrl-up>
        Command.ATTACK_WITHOUT_MOVE_S: {'msg': 'key', "keycode": -231},  # <ctrl-down>
        Command.ATTACK_WITHOUT_MOVE_E: {'msg': 'key', "keycode": -229},  # <ctrl-right>
        Command.ATTACK_WITHOUT_MOVE_W: {'msg': 'key', "keycode": -230},  # <ctrl-left>
        Command.ATTACK_WITHOUT_MOVE_NW: {'msg': 'key', "keycode": -227},  # <ctrl-home>
        Command.ATTACK_WITHOUT_MOVE_SW: {'msg': 'key', "keycode": -226},  # <ctrl-end>
        Command.ATTACK_WITHOUT_MOVE_NE: {'msg': 'key', "keycode": -224},  # <ctrl-pgUp>
        Command.ATTACK_WITHOUT_MOVE_SE: {'msg': 'key', "keycode": -223},  # <ctrl-pgDown>

        Command.AUTO_FIGHT: {'msg': 'key', 'keycode': 9},  # <tab>

        #  Todo - similar issue to github issue 9
        # Command.AUTO_FIGHT_WITHOUT_MOVE:

        # Command.WIELD_HAND_WEAPON: {'text': 'w', 'msg': 'input'},
        # Command.QUIVER_MISSILE: {'text': 'Q', 'msg': 'input'},
        # Command.FIRE_MISSILE: {'text': 'f', 'msg': 'input'},
        # Command.SELECT_MISSILE_AND_FIRE: {'text': 'F', 'msg': 'input'},
        # Command.CYCLE_MISSILE_FORWARD: {'text': '(', 'msg': 'input'},
        # Command.CYCLE_MISSILE_BACKWARD: {'text': ')', 'msg': 'input'},
        # Command.WEAR_ARMOUR: {'text': 'W', 'msg': 'input'},
        # Command.TAKE_OFF_ARMOUR: {'text': 'T', 'msg': 'input'},
        # Command.UNEQUIP: {'text': 'c', 'msg': 'input'},
        # Command.EQUIP: {'text': 'e', 'msg': 'input'},
        # Command.QUAFF: {'text': 'q', 'msg': 'input'},
        # Command.READ: {'text': 'r', 'msg': 'input'},
        # Command.PUT_ON_JEWELLERY: {'text': 'P', 'msg': 'input'},
        # Command.REMOVE_JEWELLERY: {'text': 'R', 'msg': 'input'},
        # Command.EVOKE: {'text': 'v', 'msg': 'input'},
        # Command.EXAMINE_TILE_IN_EXPLORE_MENU: {'text': 'v', 'msg': 'input'},
        # Command.SELECT_ITEM_TO_EVOKE: {'text': 'V', 'msg': 'input'},
        # Command.MEMORISE: {'text': 'M', 'msg': 'input'},
        # Command.COUNT_GOLD: {'text': '$', 'msg': 'input'},

        Command.USE_SPECIAL_ABILITY: {'text': 'a', 'msg': 'input'},
        # Command.CAST_SPELL_ABORT_WITHOUT_TARGETS: {'text': 'z', 'msg': 'input'},
        # Command.CAST_SPELL_NO_MATTER_WHAT: {'text': 'Z', 'msg': 'input'},
        # Command.LIST_ALL_SPELLS: {'text': 'I', 'msg': 'input'},
        # Command.TELL_ALLIES: {'text': 'I', 'msg': 'input'},
        # Command.REDO_PREVIOUS_COMMAND: {'text': '`', 'msg': 'input'},

        # Command.DISPLAY_CHARACTER_STATUS: {'text': '@', 'msg': 'input'},
        # Command.SHOW_SKILL_SCREEN: {'text': 'm*', 'msg': 'input'},
        # Command.CHARACTER_OVERVIEW: {'text': '%', 'msg': 'input'},
        # Command.SHOW_RELIGION_SCREEN: {'text': '^', 'msg': 'input'},
        # Command.SHOW_ABILITIES_AND_MUTATIONS: {'text': 'A', 'msg': 'input'},
        # Command.SHOW_ITEM_KNOWLEDGE: {'text': '\\', 'msg': 'input'},
        # Command.SHOW_RUNES_COLLECTED: {'text': '}', 'msg': 'input'},
        # Command.DISPLAY_WORN_ARMOUR: {'text': '[', 'msg': 'input'},
        # Command.DISPLAY_WORN_JEWELLERY: {'text': '\"', 'msg': 'input'},
        # Command.DISPLAY_EXPERIENCE_INFO: {'text': 'E', 'msg': 'input'},

        Command.OPEN_DOOR: {'text': 'O', 'msg': 'input'},
        Command.CLOSE_DOOR: {'text': 'C', 'msg': 'input'},
        Command.TRAVEL_STAIRCASE_UP: {'text': '<', 'msg': 'input'},
        Command.TRAVEL_STAIRCASE_DOWN: {'text': '>', 'msg': 'input'},
        # Command.EXAMINE_CURRENT_TILE_PICKUP_PART_OF_SINGLE_STACK: {'text': ';', 'msg': 'input'},
        # Command.EXAMINE_SURROUNDINGS_AND_TARGETS: {'text': 'x', 'msg': 'input'},
        # Command.EXAMINE_LEVEL_MAP: {'text': 'X', 'msg': 'input'},
        # Command.LIST_MONSTERS_ITEMS_FEATURES_IN_VIEW: {'msg': 'key', "keycode": 24},
        # Command.TOGGLE_VIEW_LAYERS: {'text': '|', 'msg': 'input'},
        # Command.SHOW_DUNGEON_OVERVIEW: {'msg': 'key', "keycode": 15},
        # Command.TOGGLE_AUTO_PICKUP: {'msg': 'key', "keycode": 1},
        # Command.SET_TRAVEL_SPEED_TO_CLOSEST_ALLY: {'msg': 'key', "keycode": 5},

        # Command.SHOW_INVENTORY_LIST: {'text': 'i', 'msg': 'input'},
        # Command.INSCRIBE_ITEM: {'msg': 'input', 'data': [123]},

        Command.PICKUP_ITEM: {'text': 'g', 'msg': 'input'},
        Command.SELECT_ITEM_FOR_PICKUP: {'text': ',', 'msg': 'input'},
        # Command.DROP_ITEM: {'text': 'd', 'msg': 'input'},
        # Command.DROP_LAST_ITEMS_PICKED_UP: {'text': 'D', 'msg': 'input'},

        Command.EXIT_MENU: {'msg': 'key', 'keycode': 27},  # <esc>
        # Command.SHOW_PREVIOUS_GAME_MESSAGES: {'msg': 'key', 'keycode': 16},
        # Command.RESPOND_YES_TO_PROMPT: {'text': 'Y', 'msg': 'input'},
        # Command.RESPOND_YES_TO_PROMPT_FULL: {'text': 'Yes\r', 'msg': 'input'},
        # Command.RESPOND_NO_TO_PROMPT: {'text': 'N', 'msg': 'input'},
        Command.ENTER_KEY: {'text': '\r', 'msg': 'input'},
        Command.SPACE: {'text': ' ', 'msg': 'input'},
        # Command.SAVE_GAME_AND_EXIT: {'text': 'S', 'msg': 'input'},
        # Command.SAVE_AND_EXIT_WITHOUT_QUERY: {'msg': 'key', "keycode": 19},
        # Command.ABANDON_CURRENT_CHARACTER_AND_QUIT_GAME: {'msg': 'key', "keycode": 17},
    }

    # the order of letters and symbols in this string should match the order of MenuChoice enum options
    dcss_menu_chars = list(string.ascii_lowercase + string.ascii_uppercase + '0123456789' + '*!/?<>\r.-^\t\\_\x1b')

    @staticmethod
    def get_execution_repr(command_or_menu_choice):
        if isinstance(command_or_menu_choice, Command):
            return Action.get_execution_repr_command(command_or_menu_choice)
        elif isinstance(command_or_menu_choice, MenuChoice):
            return Action.get_execution_repr_menuchoice(command_or_menu_choice)
        else:
            raise Exception("{} is not a Command or MenuChoice enum".format(command_or_menu_choice))

    @staticmethod
    def get_execution_repr_command(command: Command):
        """
        Given a command, return the data that can be sent directly to the game to execute the command.
        :return: a message data structure that can be sent directly to the game to execute the command.
        """
        # print("Command is {}".format(command))
        # for c,m in Action.command_to_msg.items():
        #    print("\t{}:{}".format(c,m))

        return Action.command_to_msg[command]

    @staticmethod
    def get_execution_repr_menuchoice(choice: MenuChoice):
        """
        Given a menuchoice, return the data that can be sent directly to the game to execute the menu selection.
        :return: a message data structure that can be sent directly to the game to select the desired menu option.
        """
        menu_choice_value = choice.value
        menu_choice_letter = Action.dcss_menu_chars[menu_choice_value]
        json_repr = {"text": "{}".format(menu_choice_letter), "msg": "input"}
        return json_repr

    @staticmethod
    def get_all_commands():
        return list(Action.command_to_msg.keys())

    @staticmethod
    def get_all_move_commands():
        return [Command.MOVE_OR_ATTACK_N,
                Command.MOVE_OR_ATTACK_S,
                Command.MOVE_OR_ATTACK_E,
                Command.MOVE_OR_ATTACK_W,
                Command.MOVE_OR_ATTACK_NW,
                Command.MOVE_OR_ATTACK_SW,
                Command.MOVE_OR_ATTACK_SE,
                Command.MOVE_OR_ATTACK_NE]
