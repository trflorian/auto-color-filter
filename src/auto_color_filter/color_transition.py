import cv2
import numpy as np

from auto_color_filter.utils import (
    add_caption,
    interpolate_color_hsv,
    interpolate_color_rgb,
)


def run_transition_loop(
    color_start_rgb: tuple[int, int, int],
    color_end_rgb: tuple[int, int, int],
    fps: int,
    time_duration_secs: float,
    image_size: tuple[int, int],
) -> None:
    """
    Runs the color transition loop.

    Args:
        color_start_rgb: The starting color in RGB format.
        color_end_rgb: The ending color in RGB format.
        time_steps: The number of time steps for the transition.
        time_duration_secs: The duration of the transition in seconds.
        image_size: The size of the images to be generated.
    """

    video_writer = cv2.VideoWriter(
        filename="media/color_transition.avi",
        fourcc=cv2.VideoWriter.fourcc(*"XVID"),
        fps=fps,
        frameSize=(image_size[0] * 2, image_size[1]),
    )

    img_shape = (image_size[1], image_size[0], 3)
    num_steps = int(fps * time_duration_secs)

    for t in np.linspace(0, 1, num_steps):
        color_rgb_trans = interpolate_color_rgb(color_start_rgb, color_end_rgb, t)
        color_hue_trans = interpolate_color_hsv(color_start_rgb, color_end_rgb, t)

        img_rgb = np.full(shape=img_shape, fill_value=color_rgb_trans, dtype=np.uint8)
        img_hsv = np.full(shape=img_shape, fill_value=color_hue_trans, dtype=np.uint8)

        # add titles to the images
        img_rgb = add_caption(
            img_rgb,
            "Transition using RGB",
        )
        img_hsv = add_caption(
            img_hsv,
            "Transition using HSV",
        )

        composite = cv2.hconcat((img_rgb, img_hsv))
        composite_bgr = cv2.cvtColor(composite, cv2.COLOR_RGB2BGR)

        video_writer.write(composite_bgr)

        cv2.imshow("Color Transition", composite_bgr)

        key = cv2.waitKey(1000 // fps) & 0xFF
        if key == ord("q"):
            break

    video_writer.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Run the color transition loop
    run_transition_loop(
        color_start_rgb=(0, 0, 255),  # Blue
        color_end_rgb=(255, 255, 0),  # Yellow
        fps=25,
        time_duration_secs=5,
        image_size=(1280, 720),
    )
