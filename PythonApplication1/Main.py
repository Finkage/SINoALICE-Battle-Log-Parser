import time
from WinCap import WindowCapture
from ReadImage import ReadImage
from RunThroughLogs import TaskMaster

screen = WindowCapture('BlueStacks')
pageScreen = WindowCapture('BlueStacks', -10, 380, 900, 510)

moveLog = TaskMaster()
pageNum = 1
loopTime = time.time()

page = ReadImage(pageScreen.get_screenshot())
pagetxt = page.imageText()

if '/' in pagetxt:
        pagetxt = pagetxt[:pagetxt.find('/')] + pagetxt[pagetxt.find('/') + 1:]
    
totalPages = int(pagetxt[1:])
print(totalPages)

while True:
    parse = ReadImage(screen.get_screenshot())
    
    moveLog.clickNextPage()
    
    print(str(pageNum) + '/' + str(totalPages))
    time.sleep(2)

    if(pageNum == totalPages):
        break
    
    pageNum = pageNum + 1


    #moveLog.scrollThroughPage(50)
    
    '''# debug the loop rate
    print('FPS {}'.format(1 / (time() - loopTime)))
    loopTime = time()
    '''