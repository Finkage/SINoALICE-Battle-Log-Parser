import pytesseract as tess
import cv2

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class ReadImage():
    """description of class"""

    # properties
    cong = r'--oem 1 --psm 6'
    img = None
    imgHt = 0
    imgWd = 0

    # on contstruction, an image is brought in and converted to greyscale and put through binary threshold
    def __init__(self, rawImage):
        self.img = cv2.cvtColor(rawImage, cv2.COLOR_BGR2GRAY)
        thresh, self.img = cv2.threshold(self.img, 115, 255, cv2.THRESH_BINARY)
        imgHt, imgWd = self.img.shape

    # returns the text inside the image using tesseract OCR
    def imageText(self):
        return tess.image_to_string(self.img, lang = 'eng', config = self.cong)

    # debugging tool to see the image that was captured on screen
    def DEBUG_showImageOnScreen(self, rectanglesOn = False):
        if rectanglesOn:
            imgH, imgW = self.img.shape
            boxes = tess.image_to_boxes(self.img, lang = 'eng', config=self.cong)
            for box in boxes.splitlines():
                box = box.split(' ')
                x,y,w,h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
                cv2.rectangle(self.img, (x,imgH - y), (w,imgH - h), (0, 0, 255), 1)

        cv2.imshow('debug tool', self.img)

        # allows to stop if necessary
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            return True

        return False