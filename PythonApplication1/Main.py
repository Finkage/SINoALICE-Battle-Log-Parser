import time
from WinCap import WindowCapture
from ReadImage import ReadImage
from RunThroughLogs import TaskMaster

#img = cv2.imread('test_log2.jpg')
screen = WindowCapture('BlueStacks')
#buttonCheck = WindowCapture('BlueStacks', )

moveLog = TaskMaster()

loopTime = time.time()

while True:
    parse = ReadImage(screen.get_screenshot())

    print(parse.imageText())
    if parse.DEBUG_showImageOnScreen():
        break

    moveLog.scrollThroughPage(50)
    
    '''# debug the loop rate
    print('FPS {}'.format(1 / (time() - loopTime)))
    loopTime = time()
    '''