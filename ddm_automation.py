# Credits for dc post:
# Konami
# TextStudio

import json
import pyperclip

areas = [
    "wetlands",
    "ancient_forest",
    "cynet_universe",
    "dark_world",
    "deepest_depths",
    "world_armor",
    "geartown",
    "world_tree",
    "psychic_feel_zone",
    "venom_swamp",
    "grand_spellbook_tower",
]
special_area_names = {
    "dark_world": "The Dark World",
    "deepest_depths": "The Most Distant, Deepest Depths",
}
types = [
    "aqua",
    "beast",
    "cyberse",
    "fiend",
    "fish",
    "insect",
    "machine",
    "plant",
    "psychic",
    "reptile",
    "spellcaster",
]
characters = [
    "ronintoadin",
    "baby_raccoon_ponpoko",
    "stack_reviver",
    "dark_beckoning_beast",
    "paces_light_of_the_ghoti",
    "crusadia_krawler",
    "crystron_citree",
    "predaplant_chlamydosundew",
    "psy_frame_driver",
    "reptilianne_lamia",
    "gagaga_sister",
]
special_charater_names = {
    "paces_light_of_the_ghoti": "Paces, Light of the Ghoti",
    "psy_frame_driver": "PSY-Frame Driver",
    "fallen_of_argyros": "Fallen of Argyros",
    "therion_empress_alasia": 'Therion "Empress" Alasia'
}
featured_archetypes = {
    "wetlands": "Frog, Paleozoic",
    "ancient_forest": "Raccoon, Mystical Beast, Melffy, Tri-Brigade",
    "cynet_universe": "Code Talker, Cyberse",
    "dark_world": "Malicevorous, Resonator, Dark World",
    "deepest_depths": "Nimble, Ghoti, Deep Sea",
    "world_armor": "Krawler, Ninja",
    "geartown": "Crystron, Ancient Gear, Synchron",
    "world_tree": "Predaplant, Naturia, Aroma",
    "psychic_feel_zone": "Psy-Frame, Psychic",
    "venom_swamp": "Reptilianne, Alien",
    "grand_spellbook_tower": "Gagaga, Spellbook",
}
dialogs = {
    "beginning": {
        "start": {
            "micon": "fallen_of_argyros_event.webp",
            "mdesc": "Start",
            "image": "great_sand_sea_gold_golgonda.webp",
            "parts": [
                {"type": "bust", "content": "fallen_of_argyros_bust.webp"},
                {"type": "name", "content": "Fallen of Argyros"},
                {"type": "text", "content": "Where am I?"},
                {"type": "text", "content": "I..."},
                {"type": "text", "content": "I need to find them..."},
            ],
        },
        "starter_deck": {
            "micon": "pack.webp",
            "mdesc": "Look for Sprights",
            "image": "great_sand_sea_gold_golgonda.webp",
            "parts": [
                {"type": "bust", "content": "fallen_of_argyros_bust.webp"},
                {"type": "name", "content": "Fallen of Argyros"},
                {"type": "text", "content": "There you are! Where are all the others?"},
                {"type": "bust", "content": "spright_blue_bust.webp"},
                {"type": "name", "content": "Spright Blue"},
                {"type": "text", "content": "We're the only ones left..."},
                {"type": "bust", "content": "fallen_of_argyros_bust.webp"},
                {"type": "name", "content": "Fallen of Argyros"},
                {"type": "text", "content": "..."},
            ],
            "chain": "pack: STARTER_DECK",
        },
        "starter_bonus": {
            "image": "great_sand_sea_gold_golgonda.webp",
            "parts": [
                {"type": "bust", "content": "spright_pixies_bust.webp"},
                {"type": "name", "content": "Spright Pixies"},
                {
                    "type": "text",
                    "content": "Uhm, I found some scraps on the battlefield that could be useful... Maybe that cheers you up?",
                },
            ],
            "chain": "pack: STARTER_BONUS",
        },
        "starter_end": {
            "image": "great_sand_sea_gold_golgonda.webp",
            "parts": [
                {"type": "bust", "content": "fallen_of_argyros_bust.webp"},
                {"type": "name", "content": "Fallen of Argyros"},
                {
                    "type": "text",
                    "content": "Thanks for trying... Just give me a moment...",
                },
            ],
        },
        "select_path": {
            "micon": "area.webp",
            "mdesc": "Moving on",
            "image": "great_sand_sea_gold_golgonda.webp",
            "parts": [
                {"type": "bust", "content": "spright_jet_bust.webp"},
                {"type": "name", "content": "Spright Jet"},
                {
                    "type": "text",
                    "content": "But now that you're here, we can travel and find new allies!",
                },
                {"type": "bust", "content": "fallen_of_argyros_bust.webp"},
                {"type": "name", "content": "Fallen of Argyros"},
                {"type": "text", "content": "Let's go then..."},
                {"type": "bust", "content": "spright_pixies_bust.webp"},
                {"type": "name", "content": "Spright Pixies"},
                {"type": "text", "content": "Alright, you lead the way!"},
            ],
            "chain": "choice: select_path",
        },
    },
    "duel": {
        "duel_0": [
            ("therion_irregular", "!!!"),
            ("fallen_of_argyros", "More Sprights? Why are they attacking us?!"),
        ],
        "duel_0_win": [
            (
                "fallen_of_argyros",
                "Somehow we managed to defend ourselves against that ambush, and that thing left just as quickly as it appeared...",
            ),
            (
                "spright_blue",
                "I'm sure that was not the last time we saw it, but since we won, we should have time to repair some of that scrap Pixies found earlier.",
            ),
        ],
        "duel_0_lose": [
            (
                "fallen_of_argyros",
                "That thing really showed us... and it left just as quickly as it appeared...",
            ),
            (
                "spright_blue",
                "I'm sure that was not the last time we saw it, let's prepare better next time.",
            ),
        ],
        "duel_1": [
            ("therion_irregular", "You can't stop me!!"),
            ("fallen_of_argyros", "Just like you said Blue, time to show what we prepared for!"),
        ],
        "duel_1_win": [
            (
                "fallen_of_argyros",
                "Finnally that guy is dealt with. And the Spright Energy can rest in peace...",
            ),
            (
                "spright_jet",
                "I feel like there's more to this tho... Let's not relax just yet.",
            ),
        ],
        "duel_1_lose": [
            (
                "fallen_of_argyros",
                "That thing is just too strong... It should leave us alone for now tho...",
            ),
            (
                "spright_jet",
                "You're probably right. I feel like there's more to this tho... Let's not relax just yet.",
            ),
        ],
        "duel_2": [
            ("therion_empress_alasia", "You're the one who defeated the king? I expected someone with a higher level..."),
            ("fallen_of_argyros", "So you're the one who sent that thing!"),
        ],
        "duel_2_win": [
            (
                "fallen_of_argyros",
                "That empress is way stronger than that other guy! We got lucky and escpaed without any major injuries...",
            ),
            (
                "spright_pixies",
                "I'm confident we'll defeat her with more preparation!",
            ),
        ],
        "duel_2_lose": [
            (
                "fallen_of_argyros",
                "That empress is way stronger than that other guy! I don't know if we'd survive another battle...",
            ),
            (
                "spright_pixies",
                "I'm confident we'll defeat her with more preparation!",
            ),
        ],
        "duel_3": [
            ("therion_empress_alasia", "Do you think you can run away from me? After the failed experiment of \"The Irregular\" I have no use left for Sprights, so you must die!"),
            ("fallen_of_argyros", "You don't know who you're fighting!"),
        ],
        "duel_3_win": [
            (
                "fallen_of_argyros",
                "The empress isn't as strong as she thinks, next time we'll finish her for sure!",
            ),
            (
                "spright_blue",
                "Let's keep our guard up just in case...",
            ),
        ],
        "duel_3_lose": [
            (
                "fallen_of_argyros",
                "I don't think we can defeat her...",
            ),
            (
                "spright_blue",
                "We can't give up... the next battle will decide it all...",
            ),
        ],
        "duel_4": [
            ("therion_empress_alasia", "You still haven't given up? This is gonna be your demise!"),
            ("fallen_of_argyros", "You underestimate the power of Level 2!"),
        ],
    },
    "wetlands": {
        "start": [
            (
                "ronintoadin",
                "Halt! Why are you traveling through these lands?",
            ),
            (
                "fallen_of_argyros",
                "Our home was destroyed, we're just looking for allies!",
            ),
            (
                "ronintoadin",
                "Then my honor requests me to accompany you.",
            ),
        ],
        "pack": [
            (
                "ronintoadin",
                "Let me introduce you to some of my best men!",
            )
        ],
        "pack_1": [
            (
                "ronintoadin",
                "Many people were inspired by your fight and joined our cause!",
            )
        ]
    },
    "ancient_forest": {
        "start": [
            (
                "baby_raccoon_ponpoko",
                "Welcome to our forest! I've never seen any beasts like you before! Do you wanna be friends??",
            ),
            (
                "fallen_of_argyros",
                "(Oh no...) I guess that sounds okay...",
            ),
            (
                "baby_raccoon_ponpoko",
                "Yay ^^",
            ),
        ],
        "pack": [
            (
                "baby_raccoon_ponpoko",
                "Come meet some of my friends!",
            )
        ],
        "pack_1": [
            (
                "baby_raccoon_ponpoko",
                "That dude was scary looking, I'll ask some more friends to join us!",
            )
        ]
    },
    "cynet_universe": {
        "start": [
            (
                "stack_reviver",
                "00111110 00100000 01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100 00100001 00001010 00111110 00100000 01001100 01101111 01100011 01100001 01110100 01101001 01101111 01101110 00111010 00100000 01000011 01111001 01101110 01100101 01110100 00100000 01010101 01101110 01101001 01110110 01100101 01110010 01110011 01100101 00001010 00111110 00100000 01010100 01100001 01110010 01100111 01100101 01110100 00100000 01000101 01101110 01110100 01101001 01110100 01111001 00100000 01000001 01101110 01100001 01101100 01111001 01110011 01101001 01110011 00111010 00100000 01000110 01110010 01101001 01100101 01101110 01100100 01101100 01111001 00001010 00111110 00100000 01000001 01100011 01110100 01101001 01101111 01101110 00111010 00100000 01010011 01100101 01101110 01100100 00100000 01000110 01110010 01101001 01100101 01101110 01100100 00100000 01010010 01100101 01110001 01110101 01100101 01110011 01110100",
            ),
            (
                "fallen_of_argyros",
                "Ehm... Yes?",
            ),
            (
                "stack_reviver",
                "00111110 00100000 01010010 01100101 01110011 01110000 01101111 01101110 01110011 01100101 00111010 00100000 01010011 01110101 01100011 01100011 01100101 01110011 01110011 00001010 00111110 00100000 01000001 01100011 01110100 01101001 01101111 01101110 00111010 00100000 01000011 01101111 01101110 01101110 01100101 01100011 01110100 00100000 01110100 01101111 00100000 01001110 01100101 01110100 01110111 01101111 01110010 01101011",
            ),
        ],
        "pack": [
            (
                "stack_reviver",
                "00111110 00100000 01010011 01110100 01100001 01110100 01110101 01110011 00111010 00100000 01000011 01101111 01101110 01101110 01100101 01100011 01110100 01100101 01100100 00100000 01110100 01101111 00100000 01001110 01100101 01110100 01110111 01101111 01110010 01101011 00001010 00111110 00100000 01010011 01110100 01100001 01110100 01110101 01110011 00111010 00100000 01000100 01101111 01110111 01101110 01101100 01101111 01100001 01100100 01101001 01101110 01100111 00101110 00101110 00101110",
            )
        ],
        "pack_1": [
            (
                "stack_reviver",
                "00111110 00100000 01000001 01101100 01101100 01101001 01100101 01110011 00101011 00101011",
            )
        ]
    },
    "dark_world": {
        "start": [
            (
                "dark_beckoning_beast",
                "I don't know how you managed to get here, but you're a part of the Dark World now.",
            ),
            (
                "fallen_of_argyros",
                "What does that even mean?",
            ),
            (
                "dark_beckoning_beast",
                "I'll show you around...",
            ),
        ],
        "pack": [
            (
                "dark_beckoning_beast",
                "Here are the other lost souls that are stuck here...",
            )
        ],
        "pack_1": [
            (
                "dark_beckoning_beast",
                "Look, we have some newcommers...",
            )
        ]
    },
    "deepest_depths": {
        "start": [
            (
                "paces_light_of_the_ghoti",
                "...",
            ),
            (
                "fallen_of_argyros",
                "...",
            ),
            (
                "paces_light_of_the_ghoti",
                "^^",
            ),
        ],
        "pack": [
            (
                "paces_light_of_the_ghoti",
                "!",
            )
        ],
        "pack_1": [
            (
                "paces_light_of_the_ghoti",
                "!!",
            )
        ]
    },
    "world_armor": {
        "start": [
            (
                "crusadia_krawler",
                "Travelers, watch out when traversing this nest!",
            ),
            (
                "fallen_of_argyros",
                "Watch out for what?",
            ),
            (
                "crusadia_krawler",
                "There are a lot more of me here... However they're less welcoming.\nAlthough you have quite a unique Energy surrounding you, they might accept you...\nFollow me.",
            ),
        ],
        "pack": [
            (
                "crusadia_krawler",
                "If they start acting hostile, I sure hope that you can run quickly...",
            )
        ],
        "pack_1": [
            (
                "paces_light_of_the_ghoti",
                "!!",
            )
        ]
    },
    "geartown": {
        "start": [
            ("crystron_citree", "Beep Boop!"),
            (
                "fallen_of_argyros",
                "Sprights, I think if the only sound this creature can produce is beeping, we should look for allies somewhere else...",
            ),
            (
                "crystron_citree",
                "Haha, I was just kidding. You're looking for allies? You seem to fit in quite nicely here! Beep Boop ;P",
            ),
        ],
        "pack": [
            (
                "crystron_citree",
                "We have a lot of different machines here, make sure to be nice to everyone!",
            )
        ],
        "pack_1": [
            (
                "crystron_citree",
                "For the next battle we started mass-producing new machines!",
            )
        ]
    },
    "world_tree": {
        "start": [
            (
                "predaplant_chlamydosundew",
                "You look... tasty...",
            ),
            (
                "fallen_of_argyros",
                "What if we let you feed off our energies, if you become our allies in return? A symbiosis if you will...",
            ),
            (
                "predaplant_chlamydosundew",
                "You know how to negotiate... We'd welcome a symbiosis... We'll consider it...",
            ),
        ],
        "pack": [
            (
                "predaplant_chlamydosundew",
                "Say hello to the forest...",
            )
        ],
        "pack_1": [
            (
                "predaplant_chlamydosundew",
                "Your energy makes new plants grow so quickly...",
            )
        ]
    },
    "psychic_feel_zone": {
        "start": [
            (
                "psy_frame_driver",
                "Look at you! Your energy seems to be compatible with the PSY-Frame Circuit!",
            ),
            (
                "fallen_of_argyros",
                "I don't know Sprights, this thing is not even a level 2 monster...",
            ),
            (
                "psy_frame_driver",
                "Come on, please! I swear I have a lot of level 2 friends, I'll show you!!",
            ),
        ],
        "pack": [
            (
                "psy_frame_driver",
                "See! You guys would work great together! (Just don't draw me)",
            )
        ],
        "pack_1": [
            (
                "psy_frame_driver",
                "If we accelerate we might find more psychics soon!",
            )
        ]
    },
    "venom_swamp": {
        "start": [
            (
                "reptilianne_lamia",
                "Oh! You seem to be a little bit lost, no?",
            ),
            (
                "fallen_of_argyros",
                "This swamp is indeed very hard to get through...",
            ),
            (
                "reptilianne_lamia",
                "Yes! Yes! Follow me, you can trust me!",
            ),
        ],
        "pack": [
            (
                "reptilianne_lamia",
                "Be careful with some of these reptiles, they will bite. But don't worry, I'll protect you... you're my treat!",
            )
        ],
        "pack_1": [
            (
                "reptilianne_lamia",
                "More and more reptiles seem to be interested in you... I'm not letting them touch you tho, so all good!",
            )
        ]
    },
    "grand_spellbook_tower": {
        "start": [
            (
                "gagaga_sister",
                "You don't look like a spellcaster!",
            ),
            (
                "fallen_of_argyros",
                "Is there a problem with that?",
            ),
            (
                "gagaga_sister",
                "You must be from outside! I've never seen somebody from outside! You look so cool!",
            ),
        ],
        "pack": [
            (
                "gagaga_sister",
                "Look at the other masters! Their spells are so powerful!",
            )
        ],
        "pack_1": [
            (
                "gagaga_sister",
                "The masters were impressed by your techniques, more of them came to learn from you!",
            )
        ]
    },
}
# Issue: Remove redundant? (pack, pick; like with dupe where it works idk) -> issue with ddm
# TODO: implement game mode setting
# TODO: end campaign based on wins/losses (duels cost 0 lives, manage lives and ends manually?)
# TODO: change icon to argyros

def area_stages(area):
    return [
        [
            [f"text: {area}_start"],
            [f"text: {area}_pack"],
            [f"text: {area}_spell_trap"],
            [f"text: {area}_special"],
            [f"text: {area}_dupe"],
            ["text: duel_0"],
            [f"area: {area}_1"]
        ],
        [
            [f"text: {area}_pack_1"],
            [f"pick: {type_dict[area].upper()}_MD_PACK", "pick: SPELL_TRAP_PACK"],
            [f"pick: {type_dict[area].upper()}_ED_PACK", "pick: SPECIAL_PACK"],
            ["text: duel_1"],
            [f"area: {area}_2"]
        ],
        [
            ["pick: SPELL_TRAP_PACK", "pick: SPECIAL_PACK"],
            [f"pick: {type_dict[area].upper()}_POWER_PACK"],
            ["text: duel_2"],
            [f"text: {area}_select_path"]
        ],
        [
            [f"text: {area}_start"],
            [f"text: {area}_pack"],
            ["pick: SPELL_TRAP_PACK", "pick: SPECIAL_PACK"],
            [f"pick: {type_dict[area].upper()}_POWER_PACK", "text: old_power_pick"],
            ["text: duel_3"],
            [f"area: {area}_4"]
        ],
        [
            [f"text: old_maindeck_pick", f"pick: {type_dict[area].upper()}_MD_PACK", "text: old_extradeck_pick", f"pick: {type_dict[area].upper()}_ED_PACK", "pick: SPELL_TRAP_PACK", "pick: SPECIAL_PACK"],
            [f"pick: {type_dict[area].upper()}_POWER_PACK", "text: old_power_pick"],
            ["text: duel_4"]
        ]
    ]


# region utility
def transformToName(val, special={}):
    if not val in special.keys():
        result = ""
        result += val[0].upper()
        skip = False
        for i in range(1, len(val)):
            if skip:
                skip = False
                continue
            if val[i] == "_":
                result += " "
                result += val[i + 1].upper()
                skip = True
            else:
                result += val[i]
        return result
    else:
        return special[val]


type_dict = dict(zip(areas, types))
stage_count = len(area_stages("wetlands"))
# endregion


# region area_objects
area_objects = {
    "START": {
        "image": "great_sand_sea_gold_golgonda.webp",
        "mdata": [
            ["text: START_settings", "text: START_start_game"],
            ["none"]
        ]
    },
    "settings": {
        "micon": "settings.webp",
        "mdesc": "Settings",
        "iconSize": 70,
        "image": "great_sand_sea_gold_golgonda.webp",
        "mdata": [
            ["choice: game_mode_setting", "choice: dialog_setting", "area: beginning"],
            ["none"]
        ]
    },
    "beginning": {
        "micon": "start_game.webp",
        "mdesc": "Start Game",
        "iconSize": 70,
        "image": "great_sand_sea_gold_golgonda.webp",
        "mdata": [
            ["text: start"],
            ["text: starter_deck"],
            ["text: select_path"],
        ],
    }
}
for area in areas:
    stages = area_stages(area)
    for i in range(len(stages)):
        area_objects[f"{area}_{i}"] = {
            "image": f"{area}.webp",
            "micon": "area.webp",
            "mdesc": "Continue",
            "mdata": stages[i],
            "vars": f"stage=>{i}"
        }
# endregion


# region text_objects
def dialogToParts(dialog):
    parts = []
    for character, text in dialog:
        parts += ({"type": "bust", "content": f"{character}_bust.webp"},)
        parts += (
            {
                "type": "name",
                "content": transformToName(character, special_charater_names),
            },
        )
        parts += ({"type": "text", "content": text},)
    return parts


def getAreaTextObjects(area):
    return {
        "start": {
            "micon": "fallen_of_argyros_event.webp",
            "mdesc": "Encounter",
            "image": f"{area}.webp",
            "parts": dialogToParts(dialogs[area]["start"]),
            "chain": f"pack: {type_dict[area].upper()}_BONUS_PACK",
        },
        "pack": {
            "micon": "pack.webp",  # TODO: more custom event icons
            "mdesc": "Growing the party",
            "image": f"{area}.webp",
            "parts": dialogToParts(dialogs[area]["pack"]),
            "vars": "chain_to_ed=>true",
            "chain": f"pack: {type_dict[area].upper()}_MD_PACK",
        },
        "spell_trap": {
            "micon": "pack.webp",  # TODO: more custom event icons
            "mdesc": "Learning new Techniques",
            "image": f"{area}.webp",
            "parts": [],
            "chain": f"pick: SPELL_TRAP_PACK",
            "vars": "loop=>3",
        },
        "special": {
            "micon": "pack.webp",  # TODO: more custom event icons
            "mdesc": "Special Finds",
            "image": f"{area}.webp",
            "parts": [],
            "chain": f"pick: SPECIAL_PACK",
        },
        "dupe": {
            "micon": "pack.webp",  # TODO: more custom event icons
            "mdesc": "Expanding on available Ressources",
            "image": f"{area}.webp",
            "parts": [],
            "chain": "bans: before_dupe",
            "vars": "loop=>2",
        },
        "pack_1": {
            "micon": "pack.webp",  # TODO: more custom event icons
            "mdesc": "Growing the party",
            "image": f"{area}.webp",
            "parts": dialogToParts(dialogs[area]["pack_1"]),
            "vars": "chain_to_ed=>false",
            "chain": f"pack: {type_dict[area].upper()}_MD_PACK",
        },
        "select_path": {
            "micon": "area.webp",
            "mdesc": "Continue Traveling",
            "image": f"{area}.webp",
            "parts": [], # TODO: write more dialog
            "chain": f"choice: {area}_select_path",
        }
    }


def getDuelTextObjects(num):
    objs = {
        num: {
            "micon": f"{'therion_irregular' if i <= 1 else 'therion_empress_alasia'}.webp",
            "mdesc": f"{'The Irregular' if i <= 1 else 'The Empress'}",
            "image": "endless_engine_argyro_system.webp",
            "parts": dialogToParts(dialogs["duel"][f"duel_{num}"]),
            "chain": f"duel: duel_{num}",
        }
    }
    if f"duel_{num}_win" in dialogs["duel"]:
        objs[f"{num}_win"] = {
            "image": "endless_engine_argyro_system.webp",
            "parts": dialogToParts(dialogs["duel"][f"duel_{num}_win"]),
            "chain": f"swap: repair_sword",
        }
    if f"duel_{num}_lose" in dialogs["duel"]:
        objs[f"{num}_lose"] = {
            "image": "endless_engine_argyro_system.webp",
            "parts": dialogToParts(dialogs["duel"][f"duel_{num}_lose"]),
            "chain": f"choice: duel_lose",
        }
    return objs

text_objects = {}
for key, val in dialogs["beginning"].items():
    text_objects[key] = val
for area in areas:
    for key, val in getAreaTextObjects(area).items():
        text_objects[f"{area}_{key}"] = val
for i in range(stage_count):
    for key, val in getDuelTextObjects(i).items():
        text_objects[f"duel_{key}"] = val
text_objects["START_start_game"] = {
    "micon": "start_game.webp",
    "mdesc": "Start Game",
    "iconSize": 70,
    "parts": [],
    "vars": "game_mode_setting=>bo5&&dialog_setting=>true",
    "chain": "area: beginning",
}
text_objects["START_settings"] = {
    "micon": "settings.webp",
    "mdesc": "Settings",
    "iconSize": 70,
    "parts": [],
    "vars": "game_mode_setting=>bo5&&dialog_setting=>true",
    "chain": "area: settings",
}
text_objects["old_maindeck_pick"] = {
    "micon": "pack.webp",  # TODO: more custom event icons
    "mdesc": "Pick Archetypal Main Deck Cards of the previous area",
    "parts": [],
    "chain": "fork: archetypal_first_maindeck_pick",
}
text_objects["old_extradeck_pick"] = {
    "micon": "pack.webp",  # TODO: more custom event icons
    "mdesc": "Pick an Archetypal Extra Deck Card of the previous area",
    "parts": [],
    "chain": "fork: archetypal_first_extradeck_pick",
}
text_objects["old_power_pick"] = {
    "micon": "pack.webp",  # TODO: more custom event icons
    "mdesc": "Maximizing the Power Level of the previous area",
    "parts": [],
    "chain": "fork: archetypal_first_power_pick",
}
# endregion

# region choice_objects
choice_objects = {
    "game_mode_setting": {
        "micon": "area.webp",
        "mdesc": "Game Mode",
        "image": "great_sand_sea_gold_golgonda.webp",
        "title": "How many duels do you want to play?\n\nDefault: Best of 5",
        "list": [
            {
                "name": "Best of 5",
                "desc": "Play up to 5 duels and potentially unlock a second archetype\n\nDefault: Best of 5",
                "img": "best_of_5.webp",
                "vars": "game_mode_setting=>bo5",
                "chain": "area: settings"
            },
            {
                "name": "Best of 3",
                "desc": "Play up to 3 duels and play with only one archetype\n\nDefault: Best of 5",
                "img": "best_of_3.webp",
                "vars": "game_mode_setting=>bo3",
                "chain": "area: settings"
            }
        ],
    },
    "dialog_setting": {
        "micon": "dialog.webp",
        "mdesc": "Dialog",
        "image": "great_sand_sea_gold_golgonda.webp",
        "title": "Change wether dialog should be enabled for the campaign\n\nDefault: Enabled",
        "list": [
            {
                "name": "Dialog Enabled",
                "desc": "Display dialog during the campaign\n\nDefault: Enabled",
                "img": "dialog.webp",
                "vars": "dialog_setting=>true",
                "chain": "area: settings"
            },
            {
                "name": "Dialog Disabled",
                "desc": "Don't display dialog during the campaign\n\nDefault: Enabled",
                "img": "no_dialog.webp",
                "vars": "dialog_setting=>false",
                "chain": "area: settings"
            }
        ],
    },
    "select_path": {
        "micon": "area.webp",
        "image": "great_sand_sea_gold_golgonda.webp",
        "title": "Where do you want to travel to?",
        "list": [
            {
                "name": transformToName(area, special_area_names),
                "desc": f"This area is full of {transformToName(type_dict[area])} Monsters!\n\nFeatured Archetypes: {featured_archetypes[area]}",
                "img": f"{area}.webp",
                "vars": f"chosen_first_area=>{area}",
                "chain": f"area: {area}_0",
            }
            for area in areas
        ],
    },
    "duel_lose": {
        "image": "endless_engine_argyro_system.webp",
        "title": "What cards do you need more of?",
        "list": [
            {
                "name": "Archetypal Main Deck Cards",
                "desc": "Get more Main Deck cards from your area's pack",
                "img": "archetypal_maindeck_pack.webp",
                "chain": "fork: archetypal_current_maindeck_pick",
            },
            {
                "name": "Archetypal Extra Deck Card",
                "desc": "Get an Extra Deck card from your area's pack",
                "img": "archetypal_extradeck_pack.webp",
                "chain": "fork: archetypal_current_extradeck_pick",
            },
            {
                "name": "Generic Spell/Trap Cards",
                "desc": "Get more generic Spell/Trap cards",
                "img": "generic_spelltrap_pack.webp",
                "vars": "loop=>1",
                "chain": "pick: SPELL_TRAP_PACK",
            },
            {
                "name": "Generic Main Deck/Extra Deck Card",
                "desc": "Get a generic Main Deck/Extra Deck card",
                "img": "special_pack.webp",
                "chain": "pick: SPECIAL_PACK",
            }
        ],
    }
}
for area in areas:
    choice_objects[f"{area}_select_path"] = {
        "micon": "area.webp",
        "image": f"{area}.webp",
        "title": "Where do you want to travel to?",
        "list": [
            {
                "name": transformToName(second_area, special_area_names),
                "desc": f"This area is full of {transformToName(type_dict[second_area])} Monsters!\n\nFeatured Archetypes: {featured_archetypes[second_area]}",
                "img": f"{second_area}.webp",
                "vars": f"chosen_second_area=>{second_area}",
                "chain": f"area: {second_area}_3",
            }
            for second_area in areas if second_area != area
        ],
    }
# endregion

# region fork_objects
fork_objects = {
    "loop_SPELL_TRAP_PACK": [
        {"loop>0": "pick: SPELL_TRAP_PACK"}
    ],
    "loop_dupe": [
        {"loop>0": "bans: before_dupe"}
    ],
    "archetypal_first_maindeck_pick": [
        {
            f"chosen_first_area={area}": f"pick: {type_dict[area].upper()}_MD_PACK"
        }
        for area in areas
    ],
    "archetypal_first_extradeck_pick": [
        {
            f"chosen_first_area={area}": f"pick: {type_dict[area].upper()}_ED_PACK"
        }
        for area in areas
    ],
    "archetypal_first_power_pick": [
        {
            f"chosen_first_area={area}": f"pick: {type_dict[area].upper()}_POWER_PACK"
        }
        for area in areas
    ],
    "archetypal_second_maindeck_pick": [
        {
            f"chosen_second_area={area}": f"pick: {type_dict[area].upper()}_MD_PACK"
        }
        for area in areas
    ],
    "archetypal_second_extradeck_pick": [
        {
            f"chosen_second_area={area}": f"pick: {type_dict[area].upper()}_ED_PACK"
        }
        for area in areas
    ],
    "archetypal_current_maindeck_pick": [
        {
            "stage<=2": "fork: archetypal_first_maindeck_pick"
        },
        {
            "stage>2": "fork: archetypal_second_maindeck_pick"
        }
    ],
    "archetypal_current_extradeck_pick": [
        {
            "stage<=2": "fork: archetypal_first_extradeck_pick"
        },
        {
            "stage>2": "fork: archetypal_second_extradeck_pick"
        }
    ]
}
for area in areas:
    fork_objects[f"{area}_chain_to_ed"] = [
            {"chain_to_ed=true": f"pack: {type_dict[area].upper()}_ED_PACK"}
        ]
# endregion

# region pack_objects
pack_objects = {
    "STARTER_DECK": {"chain": "text: starter_bonus"},
    "STARTER_BONUS": {"chain": "text: starter_end"},
}
for area in areas:
    pack_objects[f"{type_dict[area].upper()}_MD_PACK"] = {"chain": f"fork: {area}_chain_to_ed"}
    pack_objects[f"{type_dict[area].upper()}_ED_PACK"] = {}
    pack_objects[f"{type_dict[area].upper()}_BONUS_PACK"] = {}
# endregion

# region pick_objects
pick_objects = {
    "SPELL_TRAP_PACK": {
        "micon": "pack.webp",
        "mdesc": "Pick Generic Spell/Trap Cards",
        "chain": "fork: loop_SPELL_TRAP_PACK", "vars": "loop=>-1"
    },
    "SPECIAL_PACK": {
        "micon": "pack.webp",
        "mdesc": "Pick Generic Main Deck/Extra Deck Cards",
    },
}
for area in areas:
    pick_objects[f"{type_dict[area].upper()}_MD_PACK"] = {
        "micon": "pack.webp",
        "mdesc": "Pick Archetypal Main Deck Cards",
    }
    pick_objects[f"{type_dict[area].upper()}_ED_PACK"] = {
        "micon": "pack.webp",
        "mdesc": "Pick an Archetypal Extra Deck Card",
    }
    pick_objects[f"{type_dict[area].upper()}_POWER_PACK"] = {
        "micon": "pack.webp",
        "mdesc": "Maximizing the Power Level",
    }
# endregion

#region swap_objects
swap_objects = {
    "repair_sword": {
        "title": "Repair a Broken Bamboo Sword",
        "swapLimit": 1,
        "showLimit": 9,
        "trades": [
            {"Broken Bamboo Sword": "Burning Bamboo Sword"},
            {"Broken Bamboo Sword": "Cursed Bamboo Sword"},
            {"Broken Bamboo Sword": "Golden Bamboo Sword"},
            {"Broken Bamboo Sword": "Original Bamboo Sword"},
            {"Broken Bamboo Sword": "Soul Devouring Bamboo Sword"},
            {"Broken Bamboo Sword": "Solitary Sword of Poison"},
            {"Broken Bamboo Sword": "Supermagic Sword of Raptinus"},
            {"Broken Bamboo Sword": "Sword of Dark Rites"},
            {"Broken Bamboo Sword": "Twin Swords of Flashing Light - Tryce"},
        ]
    }
}
#endregion

# region dupe_objects
dupe_objects = {
    "dupe": {
        "shows": 10,
        "removeRedundant": True,
        "chain": "bans: after_dupe",
        "vars": "loop=>-1",
    }
}
# endregion

#region bans_objects
bans_objects = {
    "before_dupe": {
        "changes": [
            {"Spright Double Cross": 1},
            {"Fallen of Argyros": 2},
            {"Spright Blue": 2},
            {"Spright Jet": 2},
            {"Spright Pixies": 2},
            {"Spright Starter": 2},
            {"Spright Elf": 2},
            {"Gigantic Spright": 2}
        ],
        "chain": "dupe: dupe",
    },
    "after_dupe": {
        "changes": [
            {"Spright Double Cross": 3},
            {"Fallen of Argyros": 3},
            {"Spright Blue": 3},
            {"Spright Jet": 3},
            {"Spright Pixies": 3},
            {"Spright Starter": 3},
            {"Spright Elf": 3},
            {"Gigantic Spright": 3}
        ],
        "chain": "fork: loop_dupe",
    }
}
#endregion

# region duel_objects
duel_objects = {}
for i in range(stage_count):
    enemy = "therion_irregular" if i <= 1 else "therion_empress_alasia"
    duel_objects[f"duel_{i}"] = {
        "image": "endless_engine_argyro_system.webp",
        "dbimg": f"{enemy}_avatar.webp",
        "title": transformToName(enemy),
        "lives": 1,
        "wins": f"text: duel_{i}_win",
        "lose": f"text: duel_{i}_lose",
    }
# endregion

# region vars_objects
vars_objects = {}
# endregion

#region ends_objects
ends_objects = {
    "win": {
        "image": "endless_engine_argyro_system.webp",
        "title": "The Sprights continue their path, exploring the worlds that lie ahead of them!"
    },
    "lose": {
        "image": "endless_engine_argyro_system.webp",
        "title": "The Empress was simply too strong. On a different day, the Sprights might have won that decisive duel, but their energy will soon completely fade away..."
    }
}
#endregion

#region dialog_setting
# TODO: remove unnecessaryoptions from copied objects
modified_text_objects = {}
for text_key, text_val in text_objects.items():
    new_object = text_val.copy()
    modified_text_objects[f"{text_key}_text"] = new_object.copy()
    
    new_object["parts"] = []
    modified_text_objects[f"{text_key}_no_text"] = new_object.copy()
    
    fork_objects[f"{text_key}_dialog_fork"] = [
        {"dialog_setting=true": f"text: {text_key}_text"},
        {"dialog_setting=false": f"text: {text_key}_no_text"}
    ]
    
    new_object["chain"] = f"fork: {text_key}_dialog_fork"
    modified_text_objects[text_key] = new_object
    
text_objects = modified_text_objects
#endregion

result = {
    "area": area_objects,
    "text": text_objects,
    "choice": choice_objects,
    "fork": fork_objects,
    "pack": pack_objects,
    "pick": pick_objects,
    "swap": swap_objects,
    "dupe": dupe_objects,
    "bans": bans_objects,
    "duel": duel_objects,
    "vars": vars_objects,
    "ends": ends_objects,
}


pyperclip.copy(json.dumps(result, indent=4))
