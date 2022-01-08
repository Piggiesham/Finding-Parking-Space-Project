import cv2
import csv
import easyocr
import glob

# ทำให้ภาพตรงใช้ imutils https://pythonrepo.com/repo/jrosebr1-imutils-python-deep-learning#4-point-perspective-transform
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
# (thresh, image) = cv2.threshold(bfilter, 185, 255, cv2.THRESH_BINARY)
path = glob.glob("CarNo/*.jpg")
for file in path:
    img = cv2.imread(file)
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(img)
    text1 = result[0][1]
    print(text1)
    with open('data\CarList.csv', 'a', newline='') as car:
        c = csv.writer(car)
        c.writerow([text1])
