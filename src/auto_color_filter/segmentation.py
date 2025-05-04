import cv2
import numpy as np

img_bgr = cv2.imread("images/notes.png")
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(
    src=img_hsv,
    lowerb=np.array([160, 80, 170]),
    upperb=np.array([175, 110, 210]),
)

mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
img_bgr_masked = cv2.bitwise_and(img_bgr, img_bgr, mask=mask)

composite = cv2.hconcat([img_bgr, mask_bgr, img_bgr_masked])

cv2.imshow("Original Image", img_bgr)
cv2.imshow("Mask", mask)
cv2.imshow("Composite", composite)

cv2.waitKey(0)
cv2.destroyAllWindows()
