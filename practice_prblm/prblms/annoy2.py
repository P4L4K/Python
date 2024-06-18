import random
import pyautogui as pg
import time

# Ensure you have the correct coordinates for your sticker menu
sticker_menu_x = 100  # Replace with the actual x-coordinate
sticker_menu_y = 100  # Replace with the actual y-coordinate

# Simulate opening the sticker menu
pg.click(sticker_menu_x, sticker_menu_y)
time.sleep(2)  # Add a delay to allow the sticker menu to open

# Your list of stickers or paths to stickers
stickers = [
    r"C:\Users\hp\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\LocalState\shared\transfers\2023_42\7b43dd0b-597f-40f0-9e9e-0d18d83d6e11.webp",
    r"C:\Users\hp\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\LocalState\shared\transfers\2023_42\96c9746b-a217-47b2-8cc7-472ce024019c.webp",
    r"C:\Users\hp\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\LocalState\shared\transfers\2023_42\5c7e651a-4d4b-48ac-9338-c0da898c10cb.webp"
]

time.sleep(5)  # Add a delay if needed

for i in range(200):
    sticker = random.choice(stickers)
    
    # Click on the sticker to select it
    pg.click(sticker)
    
    # Simulate sending by pressing "Enter"
    pg.press("enter", interval=0.1)  # Add a slight delay
    time.sleep(1)

print("done")
