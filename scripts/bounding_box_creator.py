# pylint: disable=missing-module-docstring, too-many-arguments, bad-continuation
# pylint: disable=too-many-instance-attributes, invalid-name, missing-function-docstring
# pylint: disable=too-many-function-args, line-too-long

import typing  # pylint: disable=unused-import
import os
from datetime import datetime

import numpy as np
from PIL import Image


def __hex_to_rgba(c):
    c = c.replace("#", "")
    if len(c) == 6:  # If alpha not specified...
        c += "ff"

    rgba = np.array([int(f"{c[idx]}{c[idx + 1]}", 16) for idx in [0, 2, 4, 6]])
    return rgba


class BoundingBox:  # pylint: disable=
    """ Class for creating bounding boxes for Twitch things. """

    def __init__(
        self,  # pylint: disable=
        height: int = 480,
        width: int = 640,
        color_hex: str = "#09386b",
        bound_thickness: int = 8,
        save_file=True,
        save_loc: str = ".",
        outer_corner_ornament=True,
        inner_corner_ornament=True,
        make_inner_bounding_box=False,
        inner_bounding_color_hex: str = "#09386b",
        inner_bounding_thickness: int = 4,
    ):
        self.height = height
        self.width = width
        self.inner_height = 0
        self.inner_width = 0
        self.color_hex = color_hex
        self.bound_thickness = bound_thickness
        self.color = __hex_to_rgba(self.color_hex)
        self.outer_corner_ornament = outer_corner_ornament
        self.inner_corner_ornament = inner_corner_ornament
        self.make_inner_bounding_box = make_inner_bounding_box
        self.inner_bounding_color_hex = inner_bounding_color_hex
        self.inner_bounding_thickness = inner_bounding_thickness
        self.save_loc = save_loc
        self.save_file = save_file
        self.N = None  # inits the inner bounding box.

        self.main()

    def main(self):
        """ Main function for the bounding box creator. """
        self.M = self.draw_bounding_box()
        self.M = self.draw_bounding_box_ornaments()
        if self.make_inner_bounding_box:
            self.draw_inner_bounding_box()

        # Formatting the array and translating to Image.
        self.M = self.M.astype(np.uint8)
        self.im = Image.fromarray(self.M, mode="RGBA")
        if self.save_file:
            date_uuid = datetime.now().strftime("%Y_%m_%d_%H%M%S")  # to not overwrite files
            self.im.save(
                os.path.join(
                    os.path.abspath(self.save_loc),
                    f"bounding_box_{self.width}_{self.height}_{self.bound_thickness}_{date_uuid}.png",
                )
            )

    def draw_bounding_box(self):
        M_left_right = np.array(
            [
                self.color
                for _ in range(self.bound_thickness * (self.height - (2 * self.bound_thickness)))
            ]
        ).reshape((self.height - (2 * self.bound_thickness)), self.bound_thickness, 4)
        M_top_bottom = np.array(
            [
                self.color
                for _ in range(self.bound_thickness * (self.width - (2 * self.bound_thickness)))
            ]
        ).reshape(self.bound_thickness, (self.width - (2 * self.bound_thickness)), 4)
        M_center = np.zeros(
            (self.height - (2 * self.bound_thickness), self.width - (2 * self.bound_thickness), 4)
        )

        if not self.outer_corner_ornament:
            # Iif we're not making ornaments on the outer box, fill it in...
            M_corner = np.array(
                [self.color for _ in range(self.bound_thickness * self.bound_thickness)]
            ).reshape(self.bound_thickness, self.bound_thickness, 4)

        else:
            # Otherwise, put a transparency for a placeholder.
            M_corner = np.array(
                [[0, 0, 0, 0] for _ in range(self.bound_thickness * self.bound_thickness)]
            ).reshape(self.bound_thickness, self.bound_thickness, 4)

        M_left_center_right = np.concatenate([M_left_right, M_center, M_left_right], axis=1)
        M_top_bottom = np.concatenate([M_corner, M_top_bottom, M_corner], axis=1)
        return np.concatenate([M_top_bottom, M_left_center_right, M_top_bottom], axis=0)

    def draw_bounding_box_ornaments(self):
        ornament_size = int(self.bound_thickness / 2)
        ornament = np.array([self.color for _ in range(ornament_size ** 2)]).reshape(
            ornament_size, ornament_size, 4
        )

        if self.outer_corner_ornament:
            self.M[
                ornament_size : (2 * ornament_size), ornament_size : (2 * ornament_size)
            ] = ornament  # UL

            self.M[
                ornament_size : (2 * ornament_size), (-2 * ornament_size) : (-1 * ornament_size)
            ] = ornament  # UR

            self.M[
                (-2 * ornament_size) : (-1 * ornament_size),  # LL
                ornament_size : (2 * ornament_size),
            ] = ornament

            self.M[
                (-2 * ornament_size) : (-1 * ornament_size),  # LR
                (-2 * ornament_size) : (-1 * ornament_size),
            ] = ornament

        if self.inner_corner_ornament:
            self.M[
                (2 * ornament_size) : (3 * ornament_size),  # UL
                (2 * ornament_size) : (3 * ornament_size),
            ] = ornament

            self.M[
                (2 * ornament_size) : (3 * ornament_size),  # UR
                (-3 * ornament_size) : (-2 * ornament_size),
            ] = ornament

            self.M[
                (-3 * ornament_size) : (-2 * ornament_size),  # LL
                (2 * ornament_size) : (3 * ornament_size),
            ] = ornament

            self.M[
                (-3 * ornament_size) : (-2 * ornament_size),  # LR
                (-3 * ornament_size) : (-2 * ornament_size),
            ] = ornament

        return self.M

    def draw_inner_bounding_box(self):
        self.inner_height = self.height - (2 * self.bound_thickness)
        self.inner_width = self.width - (2 * self.bound_thickness)

        self.N = BoundingBox(
            height=self.inner_height,
            width=self.inner_width,
            color_hex=self.inner_bounding_color_hex,
            bound_thickness=self.inner_bounding_thickness,
            save_file=False,
            outer_corner_ornament=False,
        ).M

        self.M[
            self.bound_thickness : (-1 * self.bound_thickness),
            self.bound_thickness : (-1 * self.bound_thickness),
        ] = self.N


def make_boxes(width, height, inner_bounding_color_hex, outer_color_hex="#000000"):
    """Creates boxes."""
    outer_thickness = 6
    inner_thickness = 4

    bounding_box = BoundingBox(
        height=height,
        width=width,
        color_hex=outer_color_hex,
        bound_thickness=outer_thickness,
        save_file=True,
        save_loc="/mnt/c/Users/james",
        make_inner_bounding_box=True,
        inner_bounding_color_hex=inner_bounding_color_hex,
        inner_bounding_thickness=inner_thickness,
    )

    return bounding_box


if __name__ == "__main__":
    BOXES = [[506, 632, "#d6f58e"]]

    for box in BOXES:
        make_boxes(box[0], box[1], box[2])
