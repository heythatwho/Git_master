import time
import pyautogui

def click_mouse_every_15_minutes():
    while True:
        try:
            # Click the mouse at the current cursor position
            pyautogui.click()

            # Sleep for 15 minutes (900 seconds)
            time.sleep(900)

        except KeyboardInterrupt:
            # Handle the case when the user interrupts the program (e.g., by pressing Ctrl+C)
            print("Program interrupted.")
            break

if __name__ == "__main__":
    print("Mouse clicker started. Press Ctrl+C to stop.")
    click_mouse_every_15_minutes()
