import cv2
import numpy as np

img = cv2.imread("images/objects.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

win_name = "Color Segmentation"

cv2.namedWindow(win_name)

class MouseTracker:
    def __init__(self):
        self.is_clicked = False
        self.colors = set()
    
    def on_mouse_click(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.is_clicked = True
            self.colors = set()
        elif event == cv2.EVENT_LBUTTONUP:
            self.is_clicked = False
        
        if self.is_clicked:
            self.colors.add(tuple([int(p) for p in img_hsv[y, x]]))

tracker = MouseTracker()

cv2.setMouseCallback(win_name, tracker.on_mouse_click)

while True:
    mask = np.zeros(img.shape[:2], dtype=np.uint8)

    for color in tracker.colors:
        lower = np.array(color) - 10
        upper = np.array(color) + 10

        mask = cv2.bitwise_or(mask, cv2.inRange(img_hsv, lower, upper))
    
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    composite = np.hstack([img, mask_bgr])

    cv2.imshow(win_name, composite)

    k = cv2.waitKey(1) & 0xFF
    if k == ord("q"):
        break

cv2.destroyAllWindows()
