import pyautogui
import pyperclip
import time

# Small delay so you can switch to the target window
time.sleep(2)

# Step 1: Click on the icon
pyautogui.click(541,981
)
time.sleep(0.5)

# Step 2: Drag to select text
pyautogui.moveTo(
     607,131
     
)
pyautogui.dragTo(
     682,972
, duration=1, button='left')

# Step 3: Copy selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Get clipboard content into variable
copied_text = pyperclip.paste()

# Print or use the variable
print("Copied Text:")
print(copied_text)



