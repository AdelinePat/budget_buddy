import customtkinter
from view.utiltool import UtilTool
from view.__settings__ import DARK_BLUE, SOFT_BLUE, LIGHT_BLUE, YELLOW, SOFT_YELLOW, PINK

class Interface(customtkinter.CTk):
    def __init__(self, window_title, column_number):
        super().__init__()
        self.current_scene = "broad_view"
        self.geometry("640x480")
        self.config(background = DARK_BLUE)
        self.title(window_title)
        self.columnconfigure((column_number), weight=1)
        self.util = UtilTool()
        self.title_font = self.util.get_title_font(30)
        self.text_font = self.util.get_text_font(15)
    
