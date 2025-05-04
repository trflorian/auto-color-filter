# Color Spaces

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![GitHub License](https://img.shields.io/github/license/trflorian/auto-color-filter)

Undestaning different color spaces is crucial for Computer Vision projects. In this project I explore different examples where switching between color spaces is extremely useful.

![color_transition_rgb_vs_hsv](https://github.com/user-attachments/assets/ba15e0c7-10e8-413c-9cc5-2bad189e6e86)

## Prerequisites

- [uv](https://docs.astral.sh/uv/)


## Quickstart

You can run the `main.py` file for the main application:

```bash
uv run src/auto_color_filter/main.py
```

By clicking and holding the left mouse button you can add pixels from the image to an inclusion list. Based on this list, a color range will be defined and based on that a mask image is generated.

![auto_filter_demo](https://github.com/user-attachments/assets/9e654688-39d4-4f95-935b-3d36134cc9a4)

## More Demos

### Manual Segmentation

The example provided in `segmentation.py` creates a mask image based on a static HSV range defined in the arguments.

```bash
uv run src/auto_color_filter/segmentation.py
```

### Color Transition

In this demo we compare two different ways to interpolate between two colors:
- Directly with RGB values interpolated -> changes in brightness and saturation even if start and end color have the same brightness/saturation
- Interpolate in HSV color space -> constant brightness/saturation if start and end values match or linear interpolation in case of difference between start and end color

```bash
uv run src/auto_color_filter/segmentation.py
```

## Tests

Using pytest you can run the test suite:

```bash
uv run pytest
```
