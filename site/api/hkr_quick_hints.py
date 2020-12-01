import re

DREAMERS = ["Herrah", "Dreamer", "Monomon", "Lurien"]


class HKRQuickHints:
    def __init__(self, spoiler_text):
        self.spoiler_text = spoiler_text
        self.item_dict = None
        self.loc_dreamers = None
        self.loc_major_items = None

        self.parse_spoiler_data()

        self.dreamer_locs = self.find_collection(DREAMERS)

    def parse_spoiler_data(self):
        ptrn_prog_items = "PROGRESSION ITEMS(.*?)ALL ITEMS"
        item_data = re.findall(ptrn_prog_items, self.spoiler_text, re.DOTALL)[0]
        item_data = re.sub(r"\(\d+\) ", "", item_data)
        item_data = [d for d in item_data.split("\\r\\n") if d]
        item_data = [d.split("<---at--->") for d in item_data]

        self.item_dict = dict(item_data)

    def find_collection(self, items):
        """ Makes a dict of the location of `items`. """
        item_dict = {}
        for item in items:
            item_loc = self.item_dict.get(item)
            item_loc_na = item_loc if item_loc else "???"
            item_dict[item] = item_loc_na

        return item_dict

