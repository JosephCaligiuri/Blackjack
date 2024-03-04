import colorama
import time
import os

# Initialize colorama
colorama.init()

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Define the ASCII art
ascii_art = [
    colorama.Fore.RED + r'''
  ___
 / _ \
| | | |
| |_| |
 \___/''' + colorama.Style.RESET_ALL,
    colorama.Fore.GREEN + r'''
__   __
\ \ / /
 \ V /
  | |
  |_|''' + colorama.Style.RESET_ALL,
    colorama.Fore.BLUE + r'''
_____
| ____|___   __
|  _| / _ \ / /
| |__| (_) / /
|_____\___/_/''' + colorama.Style.RESET_ALL
]

# Main loop
while True:
    clear_screen()
    for art in ascii_art:
        print(art)
        time.sleep(0.5)  # Adjust the delay as needed for animation
        clear_screen()  # Clear the screen before printing the next art
