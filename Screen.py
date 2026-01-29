from Menu import Menu
from config import menu_list
import time
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from gpiozero import Button

class Screen:
    def __init__(self):
        self.names_menu = Menu(menu_list)

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

        self.__load_assets()
        self.__buttons()

        # Clean screen
        self.__clean_screen()
        
        # Initial draw
        self.__update_screen()

    def run(self):
        """Keep the script running"""
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            pass
        
    # Load the diferent assets for the project
    def __load_assets(self):
        self.icons_list = []
        # Auto Copy
        self.icon_auto_copy = Image.open("pbm_assets/icon-auto-copy.pbm").convert("1")
        self.icons_list.append(self.icon_auto_copy)

        # Read Tag
        self.icon_read_tag = Image.open("pbm_assets/icon-read-tag.pbm").convert("1")
        self.icons_list.append(self.icon_read_tag)

        # Scan Tag
        self.icon_scan_tag = Image.open("pbm_assets/icon-scan-tag.pbm").convert("1")
        self.icons_list.append(self.icon_scan_tag)

        # Edit Tag
        self.icon_pencil_tag = Image.open("pbm_assets/icon-pencil.pbm").convert("1")
        self.icons_list.append(self.icon_pencil_tag)

        # View Tag
        self.icon_glasses_tag = Image.open("pbm_assets/icon-glasses.pbm").convert("1")
        self.icons_list.append(self.icon_glasses_tag)

        # Scripts
        self.icon_script_tag = Image.open("pbm_assets/icon-script.pbm").convert("1")
        self.icons_list.append(self.icon_script_tag)

        # Acces Point
        self.icon_waves_tag = Image.open("pbm_assets/icon-waves.pbm").convert("1")
        self.icons_list.append(self.icon_waves_tag)

        # Settings
        self.icon_gear_tag = Image.open("pbm_assets/icon-gear.pbm").convert("1")
        self.icons_list.append(self.icon_gear_tag)

        # Information
        self.icon_info_tag = Image.open("pbm_assets/icon-info.pbm").convert("1")
        self.icons_list.append(self.icon_info_tag)

        # Menu with icons
        self.icons_menu = Menu(self.icons_list)

        # Sidebar bitmap
        self.sidebar = Image.open("pbm_assets/item-selected-backgraund.pbm").convert("1")

        # Fonts
        self.normal_font = ImageFont.truetype("fonts/PixelOperator.ttf", 16)
        self.bold_font = ImageFont.truetype("fonts/PixelOperator-Bold.ttf",16)

    # Draw the content in the screen
    def __draw_screen(self,background, draw, triplet_name_list, triplet_icon_list):
        background.paste(triplet_icon_list[0], self.FIRST_ICON_POSITION) 
        background.paste(self.sidebar, self.SIDEBAR_POSITION)
        background.paste(triplet_icon_list[1], self.SECOND_ICON_POSITION)
        background.paste(triplet_icon_list[2], self.THIRD_ICON_POSITION)

        text = triplet_name_list[0]
        draw.text(self.TEXT_1_POSITION, text, font=self.normal_font, fill=1)

        text = triplet_name_list[1]
        draw.text(self.TEXT_2_POSITION,text, font=self.bold_font, fill=1)

        text = triplet_name_list[2]
        draw.text(self.TEXT_3_POSITION, text, font=self.normal_font, fill=1)

    # Draw a black rectangle to clean the screen
    def __clean_screen(self):
        self.background = Image.new("1", (self.WIDTH, self.HEIGHT), 0)  
        self.draw = ImageDraw.Draw(self.background)

    # What happes when the ok button is pressed
    def __ok_button_pressed(self):
        pass
    
    # What happes when the down button is pressed
    def __down_button_pressed(self):
        self.next()

    # What happes when the up button is pressed
    def __up_button_pressed(self):
        self.previous()

    # Defining all the buttons and its funcionalitis
    def __buttons(self):
        self.up_button = Button(17)
        self.ok_button = Button(19)
        self.down_button = Button(11)

        self.up_button.when_pressed = self.__up_button_pressed
        self.ok_button.when_pressed = self.__ok_button_pressed
        self.down_button.when_pressed = self.__down_button_pressed

    # Update the content of the screen
    def __update_screen(self):
        self.__clean_screen()
        self.__draw_screen(self.background, self.draw, self.names_menu.get_triplet_value(), self.icons_menu.get_triplet_value())
        # Refresh OLED immediately
        self.oled.image(self.background)
        self.oled.show()

    # Go to the next elements of the screen and update them
    def next(self):
        self.icons_menu.next()
        self.names_menu.next()

        self.__update_screen()

    # Go to the previous elements of the screen and update them
    def previous(self):
        self.icons_menu.previous()
        self.names_menu.previous()

        self.__update_screen()
