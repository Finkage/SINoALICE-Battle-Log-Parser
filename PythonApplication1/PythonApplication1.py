import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cong = r'--oem 1 --psm 6'

img = cv2.imread('test_log2.jpg')

#converting jpg into binary color so only text is visable
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, img = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

#debugging tool to see the recognized characters
imgH, imgW = img.shape
boxes = tess.image_to_boxes(img, lang = 'eng', config=cong)
text = tess.image_to_string(img, lang = 'eng', config=cong)

for box in boxes.splitlines():
    box = box.split(' ')
    print(box)
    x,y,w,h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(img, (x,imgH - y), (w,imgH - h), (0, 0, 255), 1)

cv2.imshow('result', img)
cv2.waitKey(0)

print(text)