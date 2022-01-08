import cv2
import numpy as np

cap = cv2.VideoCapture(0)
suc, image = cap.read()
cv2.imwrite('cctv.jpg', image)
img_path = "cctv.jpg"
img_raw = cv2.imread(img_path)
ROIs = cv2.selectROIs("Select Rois", img_raw, showCrosshair=False, fromCenter = False)
crop_number = 1
for rect in ROIs:
    x1 = rect[0]
    y1 = rect[1]
    x2 = rect[2]
    y2 = rect[3]
    img_crop = img_raw[y1:y1+y2, x1:x1+x2]
    cv2.imwrite("Namelist\Carname_"+str(crop_number)+".jpg", img_crop)
    crop_number += 1