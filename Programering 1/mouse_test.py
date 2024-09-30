import pyautogui
import os
import sys
import threading
import ctypes

# Function to check if the USB is inserted using ctypes
def is_usb_inserted(drive_letter):
    drive_type = ctypes.windll.kernel32.GetDriveTypeW(f"{drive_letter}:/")
    return drive_type != 1  # DRIVE_UNKNOWN or DRIVE_NO_ROOT_DIR

# Function to move the mouse to keep the PC awake
def move_mouse():
    while True:
        pyautogui.move(1, 0)  # Move mouse 1 pixel to the right
        pyautogui.move(-1, 0) # Move mouse back to the original position

# Function to stop the program when USB is removed
def monitor_usb(drive_letter):
    while is_usb_inserted(drive_letter):
        pass  # Continuously check if the USB is still connected
    print("USB removed, stopping the mouse movement.")
    sys.exit(0)  # Gracefully exit the program

# Main function to start the program
def main(drive_letter):
    if is_usb_inserted(drive_letter):
        print("USB detected, starting the program...")

        # Start a daemon thread to monitor USB status
        usb_monitor_thread = threading.Thread(target=monitor_usb, args=(drive_letter,))
        usb_monitor_thread.daemon = True
        usb_monitor_thread.start()

        # Start moving the mouse
        move_mouse()
    else:
        print(f"USB with drive letter {drive_letter} not detected. Exiting program.")
        sys.exit(1)

if __name__ == "__main__":
    usb_drive_letter = "D"  # Drive letter changed to D
    main(usb_drive_letter)
