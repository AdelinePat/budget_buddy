# import customtkinter
# import tkinter as tk
# import pyglet, tkinter
# pyglet.font.add_file("your font path here")

import customtkinter as ctk
import tkinter.font as tkFont
from PIL import ImageFont
import json



## COLORS
DARK_BLUE = '#1D2F6F'
SOFT_BLUE = '#8390FA'
LIGHT_BLUE = 'D9DDFF'

YELLOW = '#FAC748'
SOFT_YELLOW = '#FFF6DE'

PINK = '#F88DAD'

## FONTS
def change_font(font_path, font_size):
    font_pil = ImageFont.truetype(font_path, font_size)
    police_tk = tkFont.Font(font_path, font_size)

    return police_tk

# import customtkinter
from tkinter import filedialog
import os

TITLE_FONT_PATH = './assets/fonts/LeckerliOne-Regular.ttf'
# TITLE_FONT = Font(file=TITLE_FONT_PATH, family="Lecker")
TITLE_FONT = ctk.FontManager.load_font(TITLE_FONT_PATH)
TEXT_FONT_PATH = './assets/fonts/JosefinSans-VariableFont_wght.ttf'
# TEXT_FONT = Font(file=TEXT_FONT_PATH, family="Josefin")
TEXT_FONT = ctk.FontManager.load_font(TEXT_FONT_PATH)


