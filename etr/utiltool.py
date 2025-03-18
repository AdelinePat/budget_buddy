import customtkinter
from ..view.__settings__ import TITLE_FONT_PATH, TEXT_FONT_PATH

class UtilTool():
    
    def get_title_font(self, font_size):
        custom_font = customtkinter.FontManager.load_font(TITLE_FONT_PATH)
        custom_font = customtkinter.CTkFont(family="Leckerli One", size=font_size)
        custom_font = ("Leckerli One", font_size)
        return custom_font

    def get_text_font(self, font_size):
        custom_font = customtkinter.FontManager.load_font(TEXT_FONT_PATH)
        custom_font = customtkinter.CTkFont(family="Josefin Sans Regular", size=font_size)
        custom_font = ("Josefin Sans Regular", font_size)
        return custom_font