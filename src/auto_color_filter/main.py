import cv2
import numpy as np


class MouseTracker:
    def __init__(self, img_hsv: np.ndarray, radius: int = 10, tolerance: int = 10) -> None:
        self.is_clicked = False
        self.colors = set()
        self.mouse_pos = (0, 0)

        self.img_hsv = img_hsv
        self.mask = np.zeros(img_hsv.shape[:2], dtype=np.uint8)

        self.radius = radius
        self.tolerance = tolerance

    def on_mouse_click(self, event: int, x: int, y: int, flags: int, param: None) -> None:
        self.mouse_pos = (x, y)
        if event == cv2.EVENT_LBUTTONDOWN:
            self.is_clicked = True

            # reset the colors and mask when a new click is detected
            self.colors = set()
            self.mask = np.zeros(self.img_hsv.shape[:2], dtype=np.uint8)
        elif event == cv2.EVENT_LBUTTONUP:
            self.is_clicked = False

        if self.is_clicked:
            self.mouse_pos = (x, y)

            # circle maskaround the clicked point
            img_mask = np.zeros(self.img_hsv.shape[:2], dtype=np.uint8)
            cv2.circle(img_mask, (x, y), self.radius, 255, -1)

            img_hsv_points = self.img_hsv[img_mask == 255]
            if len(img_hsv_points) == 0:
                return

            hsv_pixel = img_hsv_points.mean(axis=0)
            hsv_color = tuple(hsv_pixel.tolist())
            self.colors.add(hsv_color)

            lower = np.clip(hsv_pixel - self.tolerance, [0, 0, 0], [179, 255, 255])
            upper = np.clip(hsv_pixel + self.tolerance, [0, 0, 0], [179, 255, 255])
            mask_for_this_pixel = cv2.inRange(self.img_hsv, lower, upper)
            self.mask = cv2.bitwise_or(self.mask, mask_for_this_pixel)

            if hsv_pixel[0] + self.tolerance > 179:
                lower = np.clip(hsv_pixel - self.tolerance, [0, 0, 0], [179, 255, 255])
                upper = np.clip(hsv_pixel + self.tolerance - 179, [0, 0, 0], [179, 255, 255])
                mask_for_this_pixel = cv2.inRange(self.img_hsv, lower, upper)
                self.mask = cv2.bitwise_or(self.mask, mask_for_this_pixel)

            if hsv_pixel[0] - self.tolerance < 0:
                lower = np.clip(hsv_pixel - self.tolerance + 179, [0, 0, 0], [179, 255, 255])
                upper = np.clip(hsv_pixel + self.tolerance, [0, 0, 0], [179, 255, 255])
                mask_for_this_pixel = cv2.inRange(self.img_hsv, lower, upper)
                self.mask = cv2.bitwise_or(self.mask, mask_for_this_pixel)


img = cv2.imread("images/notes3.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

win_name = "Color Segmentation"

cv2.namedWindow(win_name)

tracker = MouseTracker(img_hsv)

cv2.setMouseCallback(win_name, tracker.on_mouse_click)

while True:
    img_annotated = img.copy()

    # Create the combined mask using the optimized function
    mask = tracker.mask
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    # Stack the original and mask images side by side
    composite = np.hstack([img_annotated, mask_bgr])

    cv2.imshow(win_name, composite)

    k = cv2.waitKey(10) & 0xFF
    if k == ord("q"):
        break

cv2.destroyAllWindows()
