from Menu import Menu
from config import menu_list
import time
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class Screen:
    def __init__(self):
        self.menu = Menu(menu_list)

        # Screen size
        self.WIDTH = 128
        self.HEIGHT = 64

        # Icon positions
        self.FIRST_ICON_POSITION = (4,2)
        self.SECOND_ICON_POSITION = (4,24)
        self.THIRD_ICON_POSITION = (4,46)

        # Bar position
        self.SIDEBAR_POSITION = (0,22)

        # Text positions
        self.TEXT_1_POSITION = (30,2)
        self.TEXT_2_POSITION = (30,24)
        self.TEXT_3_POSITION = (30,45)

        # Connection with the oled screen
        self.i2c = board.I2C()
        self.oled = adafruit_ssd1306.SSD1306_I2C(self.WIDTH, self.HEIGHT, self.i2c, addr=0x3C)

        # Clean screen
        self.oled.fill(0)
        self.oled.show()

        self.__load_assets()

        # Create a new black image the size of the scree
        background = Image.new("1", (self.WIDTH, self.HEIGHT), 0)  
        draw = ImageDraw.Draw(background)
        
        # Put the icons in their position
        background.paste(self.icon_auto_copy, self.FIRST_ICON_POSITION) 
        background.paste(self.sidebar, self.SIDEBAR_POSITION)
        background.paste(self.icon_read_tag, self.SECOND_ICON_POSITION)
        background.paste(self.icon_scan_tag, self.THIRD_ICON_POSITION)

        text = "Auto Copy"
        draw.text(self.TEXT_1_POSITION, text, font=self.normal_font, fill=1)

        text = "Scan Tag"
        draw.text(self.TEXT_2_POSITION,text, font=self.bold_font, fill=1)

        text = "Read Tag"
        draw.text(self.THIRD_ICON_POSITION, text, font=self.normal_font, fill=1)

        while True:
            self.oled.image(background)
            self.oled.show()
            time.sleep(1.0)
        
    # Load the diferent assets for the project
    def __load_assets(self):
        self.icon_auto_copy = Image.open("pbm_assets/icon-auto-copy.pbm").convert("1")
        self.icon_read_tag = Image.open("pbm_assets/icon-read-tag.pbm").convert("1")
        self.icon_scan_tag = Image.open("pbm_assets/icon-scan-tag.pbm").convert("1")
        self.icon_gear_tag = Image.open("pbm_assets/icon-gear.pbm").convert("1")
        self.icon_glasses_tag = Image.open("pbm_assets/icon-glasses.pbm").convert("1")
        self.icon_info_tag = Image.open("pbm_assets/icon-info.pbm").convert("1")
        self.icon_pencil_tag = Image.open("pbm_assets/icon-pencil.pbm").convert("1")
        self.icon_script_tag = Image.open("pbm_assets/icon-script.pbm").convert("1")
        self.icon_waves_tag = Image.open("pbm_assets/icon-waves.pbm").convert("1")

        self.sidebar = Image.open("pbm_assets/item-selected-backgraund.pbm").convert("1")

        self.normal_font = ImageFont.truetype("fonts/pixelOperator.ttf", 16)
        self.bold_font = ImageFont.truetype("fonts/pixelOperator-Bold.ttf",16)

    def lenght(self):
        return self.menu.lenght()

    def next(self):
        pass
    def previous(self):
        pass
