import os
import cv2
import sys
import time
import win32gui
import win32api
import win32con
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget


# Get window by name
class ReadWindow(QWidget):

    def __init__(self, window_name, parent=None):
        super(ReadWindow, self).__init__(parent=parent)

        self.hwnd = win32gui.FindWindow(None, window_name)
        self.screen = QApplication.primaryScreen()
        self.window_shape = win32gui.GetWindowRect(self.hwnd)
        print(f'Window shape: {self.window_shape}')

    def capture_window(self):
        qimg = self.screen.grabWindow(self.hwnd).toImage()
        ptr = qimg.constBits()
        ptr.setsize(qimg.byteCount())
        img = np.array(ptr).reshape(qimg.height(), qimg.width(), 4)
        return img[:, :, :3]

    def click(self, x, y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


class HeyBoxFish:

    def __init__(self, rock_tmp='rock_template.png'):

        self.phone_screen = ReadWindow('夜神模拟器')
        self.rock_template = cv2.imread(rock_tmp)

        self.resolution = self.get_resolution()
        self.area_height = (560, 650)
        self.area_erroe = (200, 280, 360, 400)

        self.start_center = (self.resolution[0] // 2, 920)
        self.left_center = (170, 920)
        self.right_center = (380, 920)

    def __match_template(self, img, tmp, threshold=0.5):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        tmp = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(img, tmp, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val > threshold:
            return max_loc
        else:
            return 0, 0

    def __start(self):
        pos_x = self.start_center[0] + self.phone_screen.window_shape[0]
        pos_y = self.start_center[1] + self.phone_screen.window_shape[1]
        self.phone_screen.click(pos_x, pos_y)

    def __left(self):
        pos_x = self.left_center[0] + self.phone_screen.window_shape[0]
        pos_y = self.left_center[1] + self.phone_screen.window_shape[1]
        self.phone_screen.click(pos_x, pos_y)
        print('<--')

    def __right(self):
        pos_x = self.right_center[0] + self.phone_screen.window_shape[0]
        pos_y = self.right_center[1] + self.phone_screen.window_shape[1]
        self.phone_screen.click(pos_x, pos_y)
        print('-->')

    def play_game(self, step: float=0.2):
    
        # start
        self.__start()
        time.sleep(3)
        t_time = time.time()
        
        # detect rock
        while True:
            st_time = time.time()
            img = self.phone_screen.capture_window()

            cap_time = time.time()
            # find rock
            area = img[self.area_height[0]: self.area_height[1], :, :]
            x, y = self.__match_template(area, self.rock_template)
            # find error
            area_error = img[self.area_erroe[1]: self.area_erroe[3], self.area_erroe[0]: self.area_erroe[2], :]
            area_error = area_error[:, :, 2]
            average_error = np.average(area_error)
            img_time = time.time()

            if average_error > 200:
                break

            # if detected
            if x > 0:
                if x > self.resolution[0] // 2:
                    self.__left()
                else:
                    self.__right()
            else:
                self.__right()
            
            print(f'Capture time: {cap_time - st_time:.4}, image process time: {img_time - cap_time:.4}, wait time: {step}\n')
            time.sleep(step)

    def get_resolution(self):
        img = self.phone_screen.capture_window()
        cv2.imwrite('tmp_screen.png', img)
        h, w, c = img.shape
        print(f'Snapshot resolution: {w, h}')
        return w, h


if __name__ == '__main__':
    app = QApplication(sys.argv)
    get_fish = HeyBoxFish()

    arg_n = len(sys.argv)
    if arg_n >= 2:
        time_wait = float(sys.argv[1])
    else:
        time_wait = 0.15

    print(f'Wait time each loop: {time_wait} S\n')
    get_fish.play_game(time_wait)

