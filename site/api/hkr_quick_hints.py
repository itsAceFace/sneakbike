import re
from collections import defaultdict

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

ALL_ITEMS = (
    DREAMERS
    + BASIC_ABILITIES
    + ADVANCED_ABILITIES
    + STANDARD_ITEMS
    + OTHER_KEYS
    + PALE_ORE
)

LOCATIONS_GENERAL_DICT = {
    "Abyss": "Abyss",
    "Ancestral Mound": "Forgotten Crossroads",
    "Ancient Basin": "Ancient Basin",
    "Beast's Den": "Deepnest",
    "Black Egg Temple": "Forgotten Crossroads",
    "Blue Lake": "Resting Grounds",
    "Cast Off Shell": "Kingdom's Edge",
    "City of Tears": "City of Tears",
    "Colosseum": "Kingdom's Edge",
    "Crystal Peak": "Crystal Peak",
    "Crystallized Mound": "Crystal Peak",
    "Deepnest": "Deepnest",
    "Dirtmouth": "Dirtmouth",
    "Distant Village": "Deepnest",
    "Failed Tramway": "Deepnest",
    "Fog Canyon": "Fog Canyon",
    "Forgotten Crossroads": "Forgotten Crossroads",
    "Fungal Core": "Fungal Wastes",
    "Fungal Wastes": "Fungal Wastes",
    "Greenpath": "Greenpath",
    "Hallownest's Crown": "Crystal Peak",
    "Hive": "Hive",
    "Howling Cliffs": "Howling Cliffs",
    "Iselda": "Forgotten Crossroads",
    "Isma's Grove": "Royal Waterways",
    "Junk Pit": "Royal Waterways",
    "King's Pass": "Dirtmouth",
    "King's Station": "City of Tears",
    "Kingdom's Edge": "Kingdom's Edge",
    "Lake of Unn": "Greenpath",
    "Leg Eater": "Fungal Wastes",
    "Mantis Village": "Fungal Wastes",
    "Overgrown Mound": "Fog Canyon",
    "Palace Grounds": "Ancient Basin",
    "Pleasure House": "City of Tears",
    "Queen's Gardens": "Queen's Gardens",
    "Queen's Station": "Fungal Wastes",
    "Resting Grounds": "Resting Grounds",
    "Royal Waterways": "Royal Waterways",
    "Salubra": "Forgotten Crossroads",
    "Sly (Key)": "Dirtmouth",
    "Sly": "Dirtmouth",
    "Soul Sanctum": "City of Tears",
    "Spirit's Glade": "Resting Grounds",
    "Stag Nest": "Howling Cliffs",
    "Stone Sanctuary": "Greenpath",
    "Teacher's Archives": "Fog Canyon",
    "Tower of Love": "City of Tears",
    "Weaver's Den": "Deepnest",
}


class DreamerSpoiler:
    def __init__(self, spoiler_txt):
        self.spoiler_txt = spoiler_txt
        self.parse_spoiler_data()

        self.all_items = self.find_items(ALL_ITEMS)
        self.all_items_gb_loc = self.groupby_location(self.all_items)
        self.all_items_gb_general_loc = self.groupby_location(
            self.all_items, generalize=True
        )

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

    def groupby_location(self, item_list, generalize=False):
        loc_dict = defaultdict(list)

        for item in item_list:
            if generalize:
                item_loc = LOCATIONS_GENERAL_DICT[item["location"]]
            else:
                item_loc = item["location"]

            loc_dict[item_loc].append(item["item"])

        return loc_dict

