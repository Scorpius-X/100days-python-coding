import os

def clear_terminal():
    # Detect the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For MacOS and Linux
        os.system('clear')
    pass