import os
import math


def create_inner_bbox(
    box_height=200,
    box_width=200,
    box_x=1,
    box_y=1,
    box_stroke_width=2,
    bbox_stroke_width=2,
    bbox_color="#232666",
    bbox_r=2,
    xml_id="",
):

    stroke_total_width = bbox_stroke_width + box_stroke_width
    h = box_height - stroke_total_width
    w = box_width - stroke_total_width
    x = box_x + (stroke_total_width / 2)
    y = box_y + (stroke_total_width / 2)

    tmpl = (
        h,
        w,
        x,
        y,
        f"""<rect id="{xml_id}" style="fill:none; stroke:{bbox_color}; stroke-width:{bbox_stroke_width}px;" width="{w}px" height="{h}px" x="{x}px" y="{y}px" rx="{bbox_r}px" ry="{bbox_r}px"/>""",
    )

    return tmpl


def create_bbox(
    height=200,
    width=200,
    outer_border_color="#232666",
    inner_border_color="#5959c9",
    save_path=os.path.expanduser("~"),
):
    # We have to init an empty box with stroke width 2 to start at 1, 1.
    boundaries = [
        {"stroke_width": 2},
        {"stroke_width": 2, "color": "#000000", "r": 5, "id": "outer_border"},
        {"stroke_width": 2, "color": "#444fff", "r": 3, "id": "outer_outer_border"},
        {"stroke_width": 4, "color": "#fff444", "r": 0, "id": "inner"},
        {"stroke_width": 2, "color": "#444fff", "r": 0, "id": "inner_outer_border"},
        {"stroke_width": 2, "color": "#000000", "r": 0, "id": "inner_border"},
    ]

    stroke_width_sum = (
        sum([b["stroke_width"] for b in boundaries]) - 2
    )  # minus the init

    bounding_boxes_total_size = 2 * stroke_width_sum
    svg_height = height + bounding_boxes_total_size
    svg_width = width + bounding_boxes_total_size

    _xml = """<svg xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink= "http://www.w3.org/1999/xlink" width="{svg_width}px" height="{svg_height}px">"""

    h, w, x, y = svg_height, svg_width, 0, 0
    rect_list = []
    for idx in range(1, len(boundaries)):
        h, w, x, y, txt = create_inner_bbox(
            box_height=h,
            box_width=w,
            box_x=x,
            box_y=y,
            box_stroke_width=boundaries[idx - 1]["stroke_width"],
            bbox_stroke_width=boundaries[idx]["stroke_width"],
            bbox_color=boundaries[idx]["color"],
            bbox_r=boundaries[idx]["r"],
            xml_id=boundaries[idx]["id"],
        )
        rect_list.append(txt)

    # Inner has to be first to get overlapped.
    # This may not work for any more than N=5 borders.
    # TODO: Maybe make this cleaner.
    inner_bd = rect_list.pop(int(math.ceil(len(rect_list) / 2)))
    _xml += (inner_bd + "\n" + "\n".join(rect_list)) + "</svg>"

    file_name = f"{height}h_{width}w_{outer_border_color[1:]}out_{inner_border_color}in"
    with open(os.path.join(save_path, file_name), "w+") as f:
        f.write(_xml)


if __name__ == "__main__":
    create_bbox(
        height=100,
        width=333,
        outer_border_color="#232666",
        inner_border_color="#5959c9",
    )

