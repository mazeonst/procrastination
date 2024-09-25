import pyautogui
import threading
import math

# Flag to stop the program
stop_movement = False

def stop_on_enter():
    global stop_movement
    input("Press Enter to stop the Program...\n")
    stop_movement = True

# Start the thread to listen for Enter key press
stop_thread = threading.Thread(target=stop_on_enter)
stop_thread.start()

# Main loop for simulating mouse movement
screen_width, screen_height = pyautogui.size()

# Move the mouse to the center of the screen
pyautogui.moveTo(screen_width // 2, screen_height // 2, duration=2)

# Move the mouse in a circle until Enter is pressed
i = 0
while not stop_movement:
    x = screen_width // 2 + 100 * math.cos(i / 10)  # Use math.cos
    y = screen_height // 2 + 100 * math.sin(i / 10)  # Use math.sin
    pyautogui.moveTo(x, y, duration=0.1)
    i += 1

print("Mouse movement stopped.")

# Wait for the thread to finish
stop_thread.join()
