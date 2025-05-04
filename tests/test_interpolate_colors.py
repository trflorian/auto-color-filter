import pytest

from auto_color_filter.utils import interpolate_color_hsv, interpolate_color_rgb


@pytest.mark.parametrize(
    "start_rgb, end_rgb, t, expected_rgb",
    [
        ((255, 0, 0), (0, 255, 0), 0.5, (127, 127, 0)),  # Red to Green
        ((0, 255, 0), (0, 0, 255), 0.5, (0, 127, 127)),  # Green to Blue
        ((0, 0, 255), (255, 0, 0), 0.5, (127, 0, 127)),  # Blue to Red
        ((255, 255, 255), (0, 0, 0), 0.5, (127, 127, 127)),  # White to Black
    ],
)
def test_interpolate_color_rgb(
    start_rgb: tuple[int, int, int],
    end_rgb: tuple[int, int, int],
    t: float,
    expected_rgb: tuple[int, int, int],
) -> None:
    """
    Test the RGB color interpolation function.
    """
    result = interpolate_color_rgb(start_rgb, end_rgb, t)
    assert result == expected_rgb, f"Expected {expected_rgb}, but got {result}"


@pytest.mark.parametrize(
    "color_rgb",
    [
        (255, 0, 0),  # Red
        (0, 255, 0),  # Green
        (0, 0, 255),  # Blue
        (255, 255, 255),  # White
        (0, 0, 0),  # Black
    ],
)
def test_interpolate_start_end_color(color_rgb: tuple[int, int, int]) -> None:
    """
    Test the RGB color interpolation function with t=0 and t=1.
    """
    arbitrary_color = (111, 111, 111)

    result = interpolate_color_rgb(
        start_rgb=color_rgb,
        end_rgb=arbitrary_color,
        t=0.0,
    )
    assert result == color_rgb, f"Expected {color_rgb}, but got {result}"

    result = interpolate_color_hsv(
        start_rgb=color_rgb,
        end_rgb=arbitrary_color,
        t=0.0,
    )
    assert result == color_rgb, f"Expected {color_rgb}, but got {result}"

    result = interpolate_color_rgb(
        start_rgb=arbitrary_color,
        end_rgb=color_rgb,
        t=1.0,
    )
    assert result == color_rgb, f"Expected {color_rgb}, but got {result}"
    
    result = interpolate_color_hsv(
        start_rgb=arbitrary_color,
        end_rgb=color_rgb,
        t=1.0,
    )
    assert result == color_rgb, f"Expected {color_rgb}, but got {result}"
