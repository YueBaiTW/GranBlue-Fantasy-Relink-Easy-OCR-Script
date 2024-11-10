import pyautogui
import time

print("移動滑鼠到目標位置，3秒後開始顯示座標")
time.sleep(3)

try:
    while True:
        x, y = pyautogui.position()
        print("滑鼠座標位置:", x, y)
        time.sleep(0.5)  # 每半秒更新一次座標
except KeyboardInterrupt:
    print("結束座標擷取")
