import cv2

img = cv2.imread("images/objects.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(gray, 50, 150)

cv2.imshow("edges", edges)
cv2.waitKey(0)

cv2.destroyAllWindows()
