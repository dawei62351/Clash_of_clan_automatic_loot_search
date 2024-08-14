import pyautogui
import cv2
import pytesseract
import re
import time
import numpy as np
from playsound import playsound


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Screenshot the full screen
screenshot = pyautogui.screenshot(region=(0, 0, 1050, 620))
screenshot.save("screenshot.png")

# Convert screenshot to OpenCV format
screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
gray_screenshot = cv2.cvtColor(screenshot_cv, cv2.COLOR_BGR2GRAY)


# Coordinates and dimensions for the regions (replace with actual values)
gold_regions = (50, 110, 100, 20)  # replace with actual coordinates
elixir_regions = (50, 145, 100, 20)  # replace with actual coordinates


def capture_and_extract(region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save("loot.png")

    image = cv2.imread("loot.png")
    # image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    # binary_image = cv2.adaptiveThreshold(
    #     gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    # )
    loot_text = pytesseract.image_to_string(image, config='--psm 7 -c tessedit_char_whitelist=0123456789')
    # loot_text = pytesseract.image_to_string(binary_image, config='--psm 7 -c tessedit_char_whitelist=0123456789')
    match = re.findall(r'\d+', loot_text)

    if match:
        loot_amount = int(''.join(match))
        return loot_amount
    return 0


def find_match():
    pyautogui.click(x=71, y=550)  # attack!
    time.sleep(0.3)
    pyautogui.click(x=739, y=372)  # find a match
    time.sleep(3)


def train_troops():
    time.sleep(1)
    pyautogui.click(x=779, y=193)  # click camp
    time.sleep(0.3)
    pyautogui.click(x=700, y=448)  # train troops
    time.sleep(0.3)
    pyautogui.click(x=829, y=78)  # quick train
    time.sleep(0.3)
    pyautogui.click(x=892, y=179)  # click train
    time.sleep(0.3)
    pyautogui.click(x=939, y=72)  # close page
    time.sleep(1)


def main():
    time.sleep(2)
    train_troops()
    find_match()
    while True:
        gold_amount = capture_and_extract(gold_regions)
        elixir_amount = capture_and_extract(elixir_regions)

        print(f"Gold: {gold_amount}, Elixir: {elixir_amount}")

        if gold_amount >= 1_000_000 and elixir_amount >= 1_000_000:
            playsound('alert.mp3')
            pyautogui.alert("Both gold and elixir are over 1 million. Proceeding...")
            break
        else:
            print("Gold or elixir is less than 1 million. Skipping...")
            pyautogui.click(x=966, y=453)
        time.sleep(3.5)


if __name__ == "__main__":
    main()