from time import time
from WinCap import WindowCapture
from ReadImage import ReadImage

#img = cv2.imread('test_log2.jpg')
screen = WindowCapture('BlueStacks')

loopTime = time()

while True:
    parse = ReadImage(screen.get_screenshot())

    print(parse.imageText())
    if parse.DEBUG_showImageOnScreen():
        break

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loopTime)))
    loopTime = time()