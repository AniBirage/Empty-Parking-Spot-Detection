import cv2

draw = False
ix, iy = -1, -1
img = cv2.imread("image.jpg")


def draw_rect(event, x, y, frames, param):
    global ix, iy, draw
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            img_rect = img.copy()
            cv2.rectangle(img_rect, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow("Image", img_rect)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        cv2.imshow("Image", img)
        print(f"{[(ix, iy), (x, y)]},")


cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw_rect)
cv2.imshow("Image", img)

while True:
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
