from Menu import Menu
import time
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class Screen:
    def __init__(self, menu_list):
        self.menu = Menu(menu_list)

        # Screen size
        self.WIDTH = 128
        self.HEIGHT = 64

        # Icon positions
        self.FIRST_ICON_POSITION = (4,2)
        self.SECOND_ICON_POSITION = (4,24)
        self.THIRD_ICON_POSITION = (4,46)

        # Bar position
        self.BAR_POSITION = (0,22)

        # Text positions
        self.TEXT_1_POSITION = (30,2)
        self.TEXT_2_POSITION = (30,24)
        self.TEXT_3_POSITION = (30,45)

        self.i2c = board.I2C()
        self.oled = adafruit_ssd1306.SSD1306_I2C(self.WIDTH, self.HEIGHT, self.i2c, addr=0x3C)

        self.oled.fill(0)
        self.oled.show()

        self.__load_assets()
        
    # Load the diferent assets for the project
    def __load_assets(self):
        self.icon_auto_copy = Image.open("pbm_assets/icon-auto-copy.pbm").convert("1")
        self.icon_read_tag = Image.open("pbm_assets/icon-read-tag.pbm").convert("1")
        self.icon_scan_tag = Image.open("pbm_assets/icon-scan-tag.pbm").convert("1")
        self.icon_gear_tag = Image.open("pbm_assets/icon-scan-tag.pbm").convert("1")
        self.icon_scan_tag = Image.open("pbm_assets/icon-scan-tag.pbm").convert("1")
        self.icon_scan_tag = Image.open("pbm_assets/icon-scan-tag.pbm").convert("1")
        self.icon_scan_tag = Image.open("pbm_assets/icon-scan-tag.pbm").convert("1")
        self.icon_scan_tag = Image.open("pbm_assets/icon-scan-tag.pbm").convert("1")
        self.icon_scan_tag = Image.open("pbm_assets/icon-scan-tag.pbm").convert("1")

        self.barra_lateral = Image.open("pbm_assets/item-selected-backgraund.pbm").convert("1")

        self.font_normal = ImageFont.truetype("fuentes/pixelOperator.ttf", 16)
        self.font_negreta = ImageFont.truetype("fuentes/pixelOperator-Bold.ttf",16)

    def lenght(self):
        pass

    def next(self):
        pass
    def previous(self):
        pass
