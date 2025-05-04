import cv2
import numpy as np
import pytest

from auto_color_filter.utils import convert_color_space


@pytest.mark.parametrize(
    "color_rgb, color_hsv",
    [
        ((255, 0, 0), (0, 255, 255)),  # Red
        ((0, 255, 0), (60, 255, 255)),  # Green
        ((0, 0, 255), (120, 255, 255)),  # Blue
        ((0, 0, 0), (0, 0, 0)),  # Black
        ((255, 255, 255), (0, 0, 255)),  # White
    ],
)
def test_convert_color_space_rgb_to_hsv(
    color_rgb: tuple[int, int, int],
    color_hsv: tuple[int, int, int],
) -> None:
    """
    Test the conversion from RGB to HSV color space.
    """
    output_hsv = convert_color_space(color_rgb, cv2.COLOR_RGB2HSV)
    assert output_hsv == color_hsv, f"Expected {color_hsv}, but got {output_hsv}"

    output_rgb = convert_color_space(color_hsv, cv2.COLOR_HSV2RGB)
    assert output_rgb == color_rgb, f"Expected {color_rgb}, but got {output_rgb}"


def test_convert_color_space_back() -> None:
    """
    Test the conversion from RGB to HSV and back to RGB.
    """

    num_values_per_channel = 10

    for r in np.linspace(0, 255, num_values_per_channel, dtype=int):
        for g in np.linspace(0, 255, num_values_per_channel, dtype=int):
            for b in np.linspace(0, 255, num_values_per_channel, dtype=int):
                color_rgb = (int(r), int(g), int(b))
                color_hsv = convert_color_space(color_rgb, cv2.COLOR_RGB2HSV)
                output_rgb = convert_color_space(color_hsv, cv2.COLOR_HSV2RGB)

                # Allow for some tolerance in the conversion, up to 15% mis-match!!
                assert color_rgb == pytest.approx(
                    output_rgb, rel=0.15
                ), f"Expected {color_rgb}, but got {output_rgb}"
