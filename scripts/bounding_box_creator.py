import typing
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


class BoundingBox:

    def __init__(
            self,
            height: int = 480,
            width: int = 640,
            outer_color_hex: str = "#09386bff",
            outer_width: int = 8):
        self.height = height
        self.width = width
        self.outer_color_hex = outer_color_hex
        self.outer_width = outer_width
        self.outer_color = self.__hex_to_rgba(self.outer_color_hex)

        self.M = self.make_bounding_box()
        self.M = self.make_bounding_box_ornaments()
        self.M = self.M.astype(np.uint8)
        self.im = Image.fromarray(self.M, mode="RGBA")
        self.im.save(
            f"/mnt/c/Users/james/bounding_box_{self.outer_color_hex[1:]}_{self.width}_{self.height}_{self.outer_width}_2.png")

    def __hex_to_rgba(self, c):
        c = c.replace("#", "")
        if len(c) == 6:
            # If alpha not specified...
            c += "ff"

        rgba = np.array([int(f"{c[idx]}{c[idx + 1]}", 16)
                         for idx in [0, 2, 4, 6]])
        return rgba

    def make_bounding_box(self):
        M_left_right = (np.array([self.outer_color for _ in range(self.outer_width * (self.height - self.outer_width))])
                        .reshape((self.height - self.outer_width), self.outer_width, 4))
        M_top_bottom = (np.array([self.outer_color for _ in range(self.outer_width * (self.width - self.outer_width))])
                        .reshape(self.outer_width, (self.width - self.outer_width), 4))
        M_center = np.zeros((self.height - self.outer_width,
                             self.width - self.outer_width, 4))
        M_corner = (np.array([[0, 0, 0, 0] for _ in range(self.outer_width * self.outer_width)])
                    .reshape(self.outer_width, self.outer_width, 4))

        M_left_center_right = np.concatenate(
            [M_left_right, M_center, M_left_right], axis=1)
        M_top_bottom = np.concatenate(
            [M_corner, M_top_bottom, M_corner], axis=1)
        return np.concatenate([M_top_bottom, M_left_center_right, M_top_bottom], axis=0)

    def make_bounding_box_ornaments(self):
        ornament_size = int(self.outer_width / 2)
        ornament = (np.array([self.outer_color for _ in range(ornament_size**2)])
                    .reshape(ornament_size, ornament_size, 4))

        # Upper-left
        self.M[ornament_size:(2 * ornament_size),
               ornament_size:(2 * ornament_size)] = ornament
        self.M[(2 * ornament_size):(3 * ornament_size),
               (2 * ornament_size):(3 * ornament_size)] = ornament

        # Upper-right
        self.M[ornament_size:(2 * ornament_size), (-2 *
                                                   ornament_size):(-1 * ornament_size)] = ornament
        self.M[(2 * ornament_size):(3 * ornament_size),
               (-3 * ornament_size):(-2 * ornament_size)] = ornament

        # Lower-left
        self.M[(-2 * ornament_size):(-1 * ornament_size),
               ornament_size:(2 * ornament_size)] = ornament
        self.M[(-3 * ornament_size):(-2 * ornament_size),
               (2 * ornament_size):(3 * ornament_size)] = ornament

        # Lower-right
        self.M[(-2 * ornament_size):(-1 * ornament_size),
               (-2 * ornament_size):(-1 * ornament_size)] = ornament
        self.M[(-3 * ornament_size):(-2 * ornament_size),
               (-3 * ornament_size):(-2 * ornament_size)] = ornament

        return self.M


if __name__ == "__main__":
    bb = BoundingBox()
