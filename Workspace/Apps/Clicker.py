import pyautogui
import time

# Define the number of clicks and the interval between each click
num_clicks = 100

# Give some time to switch to the target application
print("You have 5 seconds to switch to the target window...")
time.sleep(5)

print("Starting auto-clicker...")

for x in range(num_clicks):
    pyautogui.click()

print("Auto-clicker finished.")
