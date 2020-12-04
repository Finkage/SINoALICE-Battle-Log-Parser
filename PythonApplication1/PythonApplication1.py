import cv2
from time import time
import pytesseract as tess
from class1 import WindowCapture

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cong = r'--oem 1 --psm 6'

#img = cv2.imread('test_log2.jpg')
screen = WindowCapture('BlueStacks')

loopTime = time()
while True:
    #capture an image from the window
    img = screen.get_screenshot()

    #converting jpg into binary color so only text is visable
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh, img = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
    text = tess.image_to_string(img, lang = 'eng', config=cong)

    '''
    #debugging tool to see the recognized characters
    imgH, imgW = img.shape
    boxes = tess.image_to_boxes(img, lang = 'eng', config=cong)
    for box in boxes.splitlines():
        box = box.split(' ')
        x,y,w,h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
        cv2.rectangle(img, (x,imgH - y), (w,imgH - h), (0, 0, 255), 1)
    '''

    cv2.imshow('result', img)
    print(text)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loopTime)))
    loopTime = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break