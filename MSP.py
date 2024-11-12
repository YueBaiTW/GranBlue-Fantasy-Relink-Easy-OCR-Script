from PIL import ImageGrab
import pytesseract
import pyautogui
import time
import subprocess

'''
# 設定截取區域，這裡是整個螢幕
def capture_and_show_text():
    # 擷取螢幕，這裡可以設定 bbox 來選擇範圍，如 bbox=(100, 100, 500, 500)
    screen = ImageGrab.grab(bbox=(1091, 622, 1484, 759))
    
    # 使用 pytesseract 來進行文字辨識
    text = pytesseract.image_to_string(screen, lang='chi_tra')  # 可根據需要切換語言
    if "要繼續挑戰此任務嗎" in text:
        subprocess.run(["AutoHotkey.exe", "send_w.ahk"])
        subprocess.run(["AutoHotkey.exe", "pressmouse.ahk"])
    elif "確定要結束結果確認嗎" in text:
        subprocess.run(["AutoHotkey.exe", "pressmouse.ahk"])
    else:
        subprocess.run(["AutoHotkey.exe", "pressmouse.ahk"])
    # print("辨識結果:", text)  # 顯示辨識出的文字

'''
def MSP_Get():
    subprocess.run(["AutoHotkey.exe", "send_f.ahk"])
    time.sleep(1)
    subprocess.run(["AutoHotkey.exe", "pressmouse.ahk"])
    time.sleep(1)
    subprocess.run(["AutoHotkey.exe", "send_f.ahk"])
    time.sleep(1)
    subprocess.run(["AutoHotkey.exe", "pressmouse.ahk"])
    time.sleep(3)
    subprocess.run(["AutoHotkey.exe", "pressmouse.ahk"])
    time.sleep(1)
    subprocess.run(["AutoHotkey.exe", "send_esc.ahk"])
    time.sleep(2)
    subprocess.run(["AutoHotkey.exe", "pressmouse.ahk"])
    time.sleep(5)
    subprocess.run(["AutoHotkey.exe", "send_esc.ahk"])
    time.sleep(1)
    subprocess.run(["AutoHotkey.exe", "pressmouse.ahk"])
    time.sleep(5)
    subprocess.run(["AutoHotkey.exe", "send_esc.ahk"])
    time.sleep(1)
    
executeTime = 50
# F->左鍵->F->左鍵->左鍵->Esc->左鍵->Esc->左鍵->Esc
try:
    while executeTime > 0:
        time.sleep(3)
        MSP_Get()
        executeTime = executeTime - 1
except KeyboardInterrupt:
    print("結束")
