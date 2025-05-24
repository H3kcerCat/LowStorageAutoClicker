import pyautogui
import keyboard
import time

click_interval = 0.5  # Corrected variable name
clicking = False

print("Press F6 to toggle ROSQ auto-input system.")

while True:
    if keyboard.is_pressed('F6'):
        clicking = not clicking
        if clicking:
            print("AUTO-CLICKER ON")
        else:
            print("AUTO-CLICKER OFF")
        time.sleep(0.5)  # Prevents multiple toggles in a short time

    if clicking:
        pyautogui.click()
        time.sleep(click_interval)






