import re

DREAMERS = ["Herrah", "Monomon", "Lurien", "Dreamer"]

BASIC_ABILITIES = [
    "Vengeful Spirit",
    "Desolate Dive",
    "Isma's Tear",
    "Mothwing Cloak",
    "Crystal Heart",
    "Mantis Claw",
    "Dream Nail",
    "Monarch Wings",
]
ADVANCED_ABILITIES = [
    "Abyss Shriek",
    "Shade Soul",
    "Howling Wraiths",
    "Shade Cloak",
    "Awoken Dream Nail",
    "Great Slash",
    "Descending Dark",
]

STANDARD_ITEMS = [
    "Lumafly Lantern",
    "Simple Key-Sly",
    "Simple Key-Lurker",
    "Simple Key-Basin",
    "Simple Key-City",
    "Grimmchild",
]

OTHER_KEYS = [
    "Elegant Key",
    "King's Brand",
    "Shopkeeper's Key",
    "City Crest",
    "Tram Pass",
    "Love Key",
]

PALE_ORE = [
    "Pale Ore-Seer",
    "Pale Ore-Colosseum",
    "Pale Ore-Nosk",
    "Pale Ore-Grubs",
    "Pale Ore-Basin",
    "Pale Ore-Crystal Peak",
]


class DreamerSpoiler:
    def __init__(self, spoiler_txt):
        self.spoiler_txt = spoiler_txt
        self.parse_spoiler_data()

        self.dreamers = self.find_items(DREAMERS)
        self.basic_abilities = self.find_items(BASIC_ABILITIES)
        self.advanced_abilities = self.find_items(ADVANCED_ABILITIES)
        self.standard_items = self.find_items(STANDARD_ITEMS)
        self.other_keys = self.find_items(OTHER_KEYS)
        self.pale_ore = self.find_items(PALE_ORE)

    def parse_spoiler_data(self):
        pat_all_items = "ALL ITEMS.*"

        data_0 = re.sub(r"\r", "", self.spoiler_txt)
        data_1 = re.findall(pat_all_items, data_0, re.DOTALL)[0]
        data_1 = re.sub(r"\(\d+\) ", "", data_1).split("\n\n")[1:-3]
        data_2 = [i.split(":\n") for i in data_1]
        data_3 = {i[0]: i[1].split("\n") for i in data_2}

        self.data_dict = {}
        for k, v in data_3.items():
            for vv in v:
                item = self.data_dict.get(vv.split("<---at--->")[0])
                if item is not None:
                    if item.count("_") == 0:
                        # if it has no suffix add a _1 to the end.
                        item_w_new_suffix = f"{item}_1"
                        self.data_dict[item_w_new_suffix] = k
                    else:
                        # If the item is already has a suffix, incredment it by 1.
                        item_parts = item.split("_")
                        item_w_new_suffix = (
                            f"{item_parts[0]}_{str(int(item_parts[1]) + 1)}"
                        )
                        self.data_dict[item_w_new_suffix] = k

                else:
                    self.data_dict[vv.split("<---at--->")[0]] = k

    def find_items(self, item_list):
        list_of_locs = [
            {"item": item, "location": self.data_dict.get(item)}
            for item in item_list
            if self.data_dict.get(item) is not None
        ]

        return list_of_locs
