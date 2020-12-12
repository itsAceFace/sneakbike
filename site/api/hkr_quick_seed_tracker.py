import re
import typing
from collections import defaultdict

import pandas as pd

from hkr_standardize_names import standardized_items, standardized_locations

DREAMERS = set(["Herrah", "Monomon", "Lurien", "Dreamer"])

MAIN_ABILITIES = set(
    [
        "Awoken_Dream_Nail",
        "Crystal_Heart",
        "Desolate_Dive",
        "Dream_Gate",
        "Dream_Nail",
        "Ismas_Tear",
        "Mantis_Claw",
        "Monarch_Wings",
        "Mothwing_Cloak",
        "Shade_Cloak",
        "Shade_Soul",
        "Vengeful_Spirit",
    ]
)

ADVANCED_ABILITIES = set(
    [
        "Abyss_Shriek",
        "Cyclone_Slash",
        "Dash_Slash",
        "Descending_Dark",
        "Great_Slash",
        "Howling_Wraiths",
    ]
)

USEFUL_ITEMS = set(["Grimmchild", "Lumafly_Lantern", "Simple_Key"])

OTHER_USEFUL_ITEMS = set(
    [
        "City_Crest",
        "Elegant_Key",
        "Kings_Brand",
        "Love_Key",
        "Pale_Ore",
        "Shopkeepers_Key",
        "Tram_Pass",
    ]
)


class DreamerSpoiler:
    def __init__(self, spoiler_txt: str):
        self.spoiler_txt = spoiler_txt
        self.data_standardized = self.parse_spoiler_data()

        self.dreamers = self.restrict_items(
            self.data_standardized, restricted_set=DREAMERS
        )
        self.main_abilities = self.restrict_items(
            self.data_standardized, restricted_set=MAIN_ABILITIES
        )
        self.advanced_abilities = self.restrict_items(
            self.data_standardized, restricted_set=ADVANCED_ABILITIES
        )
        self.useful_items = self.restrict_items(
            self.data_standardized, restricted_set=USEFUL_ITEMS
        )
        self.other_useful_items = self.restrict_items(
            self.data_standardized, restricted_set=OTHER_USEFUL_ITEMS
        )

    def parse_spoiler_data(self):
        pat_all_items = "ALL ITEMS.*"

        data = re.sub(r"\r", "", self.spoiler_txt)
        data = re.findall(pat_all_items, data, re.DOTALL)[0]
        data = re.sub(r"\(\d+\) ", "", data).split("\n\n")[1:-3]
        data = [i.split(":\n") for i in data]
        data = [(i[0], i[1].split("\n")) for i in data]
        data = [(i[0], j.split("<---at--->")[0]) for i in data for j in i[1]]

        # At ths point, the data is like [[loc, item], [loc, item], ...] nonstandardized names.
        data_standardized = [
            [standardized_locations[i[0]], standardized_items[i[1]]]
            for i in data
            if standardized_items.get(i[1]) is not None
        ]

        return data_standardized

    def restrict_items(self, items, restricted_set):
        """ Restricts a set [[loc, item], [loc, item], ...] to the
            restriction_set on the "item" part.
        """

        return [item for item in items if item[1] in restricted_set]

