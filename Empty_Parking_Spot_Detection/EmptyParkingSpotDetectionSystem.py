import cv2
import numpy as np
from keras.models import load_model

model = load_model("EPSDM.h5")
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

coordinates = [
    [(25, 26), (57, 98)],
    [(57, 26), (90, 98)],
    [(90, 27), (124, 98)],
    [(125, 28), (154, 94)],
    [(154, 28), (186, 98)],
    [(186, 20), (218, 98)],
    [(220, 28), (252, 98)],
    [(252, 27), (282, 97)],
    [(283, 32), (314, 97)],
    [(314, 30), (346, 97)],
    [(347, 30), (376, 97)],
    [(377, 31), (408, 97)],
    [(408, 32), (440, 96)],
    [(440, 33), (472, 93)],
    [(536, 99), (568, 160)],
    [(504, 91), (537, 160)],
    [(472, 96), (504, 159)],
    [(440, 96), (472, 160)],
    [(408, 97), (443, 167)],
    [(376, 98), (408, 161)],
    [(345, 98), (377, 160)],
    [(314, 97), (345, 162)],
    [(284, 97), (313, 162)],
    [(251, 98), (282, 163)],
    [(220, 99), (250, 163)],
    [(187, 98), (220, 159)],
    [(155, 99), (186, 160)],
    [(123, 97), (154, 162)],
    [(91, 100), (123, 162)],
    [(59, 97), (90, 160)],
    [(26, 100), (59, 160)],
    [(24, 238), (56, 305)],
    [(55, 235), (87, 304)],
    [(86, 235), (121, 305)],
    [(122, 234), (155, 305)],
    [(155, 235), (186, 306)],
    [(187, 234), (218, 305)],
    [(219, 234), (251, 305)],
    [(251, 235), (283, 305)],
    [(284, 236), (313, 305)],
    [(314, 236), (345, 305)],
    [(346, 237), (376, 306)],
    [(378, 237), (408, 305)],
    [(409, 237), (440, 305)],
    [(439, 237), (471, 306)],
    [(471, 237), (503, 305)],
    [(504, 238), (537, 304)],
    [(537, 233), (572, 306)],
    [(24, 304), (56, 376)],
    [(56, 305), (87, 376)],
    [(88, 306), (121, 376)],
    [(122, 306), (155, 375)],
    [(156, 305), (187, 376)],
    [(187, 305), (217, 374)],
    [(218, 305), (248, 375)],
    [(251, 305), (282, 374)],
    [(285, 306), (313, 375)],
    [(314, 304), (345, 374)],
    [(345, 306), (377, 375)],
    [(378, 306), (408, 375)],
    [(410, 306), (439, 382)],
    [(441, 306), (471, 382)],
    [(471, 305), (504, 374)],
    [(503, 304), (544, 377)],
    [(539, 304), (572, 382)],
]


def det_empty_parking(image, spot):
    x1, y1 = spot[0]
    (
        x2,
        y2,
    ) = spot[1]
    if (
        x1 >= x2
        or y1 >= y2
        or x1 < 0
        or y1 < 0
        or x2 > image.shape[1]
        or y2 > image.shape[0]
    ):
        print("Invalid Coordinates For ROI")
        return False
    roi = image[y1:y2, x1:x2]
    if roi.size == 0:
        print("Empty ROI")
        return False
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    resize_roi = cv2.resize(gray_roi, (48, 48))
    resize_roi = resize_roi.astype("float") / 255
    resize_roi = np.expand_dims(resize_roi, axis=0)
    resize_roi = np.expand_dims(resize_roi, axis=-1)
    prediction = model.predict(resize_roi)
    threshold = 0.01
    if prediction[0][0] > threshold:
        return True
    else:
        return False


curr_img = cv2.imread("image.jpg")
empty_count = 0

for spot in coordinates:
    if det_empty_parking(curr_img, spot):
        cv2.rectangle(curr_img, spot[0], spot[1], (0, 255, 0), 2)
        empty_count += 1
    else:
        cv2.rectangle(curr_img, spot[0], spot[1], (0, 0, 255), 2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(
    curr_img,
    f"Empty Parking Spots:{empty_count}",
    (50, 207),
    font,
    1.25,
    (255, 0, 0),
    3,
    cv2.LINE_AA,
)

cv2.imshow("Parking Lot", curr_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
