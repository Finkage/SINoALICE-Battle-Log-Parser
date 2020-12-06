import pyautogui

class TaskMaster():
    """description of class"""

    # properties

    def scrollThroughPage(self, pageLen):
        # move to center of screen
        pyautogui.moveTo(960, 540, duration = 0)

        # scroll exactly the amount given
        pyautogui.dragRel(0, pageLen, duration = 1)

    def clickNextPage(self):
        # move to next page button
        pyautogui.click(x = 0, y = 0) #need to discover location of button
