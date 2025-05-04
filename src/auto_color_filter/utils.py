import numpy as np
import cv2


def convert_color_space(input: tuple[int, int, int], mode: int) -> tuple[int, int, int]:
    """
    Converts between color spaces

    Args:
        input: A tuple representing the color in any color space (e.g., RGB or HSV).
        mode: The conversion mode (e.g., cv2.COLOR_RGB2HSV or cv2.COLOR_HSV2RGB).

    Returns:
        A tuple representing the color in the target color space.
    """
    px_img_hsv = np.array([[input]], dtype=np.uint8)
    px_img_bgr = cv2.cvtColor(px_img_hsv, mode)
    b, g, r = px_img_bgr[0][0]
    return int(b), int(g), int(r)


def interpolate_color_rgb(
    start_rgb: tuple[int, int, int], end_rgb: tuple[int, int, int], t: float
) -> tuple[int, int, int]:
    """
    Interpolates between two colors in RGB color space.
    Args:
        start_rgb: The starting color in RGB format.
        end_rgb: The ending color in RGB format.
        t: A float between 0 and 1 representing the interpolation factor.
    Returns:
        The interpolated color in RGB format.
    """
    return (
        int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * t),
        int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * t),
        int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * t),
    )


def interpolate_color_hsv(
    start_rgb: tuple[int, int, int], end_rgb: tuple[int, int, int], t: float
) -> tuple[int, int, int]:
    """
    Interpolates between two colors in HSV color space.
    Args:
        start_rgb: The starting color in RGB format.
        end_rgb: The ending color in RGB format.
        t: A float between 0 and 1 representing the interpolation factor.
    Returns:
        The interpolated color in RGB format.
    """
    start_hsv = convert_color_space(start_rgb, cv2.COLOR_RGB2HSV)
    end_hsv = convert_color_space(end_rgb, cv2.COLOR_RGB2HSV)

    hue = int(start_hsv[0] + (end_hsv[0] - start_hsv[0]) * t)
    saturation = int(start_hsv[1] + (end_hsv[1] - start_hsv[1]) * t)
    value = int(start_hsv[2] + (end_hsv[2] - start_hsv[2]) * t)

    return convert_color_space((hue, saturation, value), cv2.COLOR_HSV2RGB)


def add_caption(
    img: np.ndarray,
    text: str,
) -> np.ndarray:
    """
    Adds a caption to the image.

    Args:
        img: The image to add the caption to.
        text: The caption text.

    Returns:
        The image with the caption added.
    """
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 255, 255)
    thickness = 2

    # Get the text size
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_x = (img.shape[1] - text_size[0]) // 2
    text_y = img.shape[0] - 25 + text_size[1] // 2

    # add a blac bor to the bottom of the image
    cv2.rectangle(
        img, (0, img.shape[0] - 50), (img.shape[1], img.shape[0]), (0, 0, 0), -1
    )

    # Add the text to the image
    cv2.putText(img, text, (text_x, text_y), font, font_scale, color, thickness)

    return img

