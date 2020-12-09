import re

DREAMERS = ["Herrah", "Monomon", "Lurien", "Dreamer"]
KEY_ITEMS = [
    "Isma's Tear",
    "Descending Dark",
    "Monarch Wings",
    "Crystal Heart",
    "Shade Soul",
    "Howling Wraiths",
    "Mantis Claw",
    "Shade Cloak",
    "Abyss Shriek",
    "Vengeful Spirit",
    "Mothwing Cloak",
]
KEYS = ["Simple Key"]


class DreamerSpoiler:
    def __init__(self, spoiler_txt):
        self.spoiler_txt = spoiler_txt

        self.parse_spoiler_data()
        self.dreamer_locs = self.find_items(DREAMERS)
        self.key_item_locs = self.find_items(KEY_ITEMS)

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
                if self.data_dict.get(vv.split("<---at--->")[0]):
                    pass  # TODO: what to do with dupes?
                else:
                    self.data_dict[vv.split("<---at--->")[0]] = k

    def find_items(self, item_list):
        list_of_locs = [
            {"item": item, "location": self.data_dict.get(item, "???")}
            for item in item_list
        ]

        return list_of_locs
