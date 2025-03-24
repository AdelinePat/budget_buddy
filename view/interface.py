import customtkinter
from view.utiltool import UtilTool
from view.__settings__ import DARK_BLUE

class Interface(customtkinter.CTk):
    def __init__(self, window_title, column_number):
        super().__init__()
        self.current_scene = "broad_view"
        self.geometry("820x700")
        self.config(background = DARK_BLUE)
        self.title(window_title)
        self.column_number = column_number
        
        self.columnconfigure((self.column_number), weight=1)

        # self.scrollable_frame = customtkinter.CTkScrollableFrame(self, bg_color=DARK_BLUE, fg_color=DARK_BLUE)
        # self.scrollable_frame.columnconfigure(0, weight=1)
        # self.scrollable_frame.pack(fill='both', expand=1)

        self.util = UtilTool()
        self.title_font = self.util.get_title_font(30)
        self.text_font = self.util.get_text_font(15)
        self.subtitle_font = self.util.get_text_font(25)