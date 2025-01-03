'''
    This is the Configuration File for the game. 
    Here, we will be defining: 
        - Size of the Game
        - Covers of the Game
        - Font of the Game
        - Frames per second (fps) and so on. 
'''

import os   # 

# Defining ScreenSize
ScreenSize=(640, 640)

# Path of Directory for Reading Image Files
imgRootDir = os.path.join(os.getcwd(), r"C:/Users/Sheewakoti-Manish/Documents/My-Codes/Python/Pokemon-Puzzle/resources/images")



# Path of Directory for Reading Font 
# "Little Lord Fontleroy NF" Font by Nick Curtis
# Source: https://www.1001fonts.com/stylish-fonts.html
fontPath=os.path.join(os.getcwd(), r"C:/Users/Sheewakoti-Manish/Documents/My-Codes/Python/Pokemon-Puzzle/resources/font/Poppins-Regular.ttf")
boldFontPath=os.path.join(os.getcwd(), r"C:/Users/Sheewakoti-Manish/Documents/My-Codes/Python/Pokemon-Puzzle/resources/font/Poppins-Extrabold.ttf")

# Adding Background Color to the Game 
bgColor=(255, 255, 255)     # Array of RGB value for White Color

# Creating RGB Colors along with Black
Red=(255, 0, 0)
Green=(0, 255, 0)
Blue=(0, 0, 255)
Black=(0, 0, 0)
Blank=(254, 243, 168)

# Defining Frames per Second
fps=40

# Defining Random Number for refering the images
randomNum=100