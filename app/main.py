from logic.characters import Knight
from logic.belongings import Weapon, Potion


def parse_dict(
        knights_dict: dict
) -> list[Knight]:
    participants = {}
    for knight, value in knights_dict.items():
        new_knight = Knight(value["name"],
                            value["power"],
                            value["hp"],
                            Knight.init_armor(value["armour"]),
                            Weapon.initialize(value["weapon"]),
                            Potion.initialize(value["potion"])
                            )
        new_knight.initialize()
        participants[knight] = new_knight
    return participants


def battle(
        knights_config: dict
) -> dict:
    knights = parse_dict(knights_config)
    # BATTLE:
    # 1 Lancelot vs Mordred:
    knights["lancelot"].battle(knights["mordred"])
    # 2 Arthur vs Red Knight:
    knights["arthur"].battle(knights["red_knight"])

    # Return battle results:
    return {
        knights["lancelot"].name: knights["lancelot"].hp,
        knights["arthur"].name: knights["arthur"].hp,
        knights["mordred"].name: knights["mordred"].hp,
        knights["red_knight"].name: knights["red_knight"].hp,
    }
