import time
from WinCap import WindowCapture
from ReadImage import ReadImage
from RunThroughLogs import TaskMaster

screen = WindowCapture('BlueStacks')
pageNum = WindowCapture('BlueStacks', -10, 360, 850, 510)

moveLog = TaskMaster()

loopTime = time.time()

while True:
    parse = ReadImage(screen.get_screenshot())
    page = ReadImage(pageNum.get_screenshot())

    #print(parse.imageText())
    print(page.imageText())
    if page.DEBUG_showImageOnScreen():
        break

    #moveLog.scrollThroughPage(50)
    
    '''# debug the loop rate
    print('FPS {}'.format(1 / (time() - loopTime)))
    loopTime = time()
    '''