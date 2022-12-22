import pyautogui
import webbrowser

# Open the website you want to take a screenshot of
# in your default web browser

website=input("Enter URL: ")

webbrowser.open(website)

# Wait for the website to load
pyautogui.sleep(5)

# Take a screenshot of the entire screen
screenshot = pyautogui.screenshot()


# Save the screenshot to a file
screenshot.save('screenshot.png')
