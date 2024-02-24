from Screen import Screen
from gpiozero import Button
from signal import pause

screen = None
def main():
    global screen
    # Pins dels bottons
    up_button = Button(17)
    ok_button = Button(19)
    down_button = Button(11)



    def ok_say():
        pass

    def down_say():
        pass

    up_button.when_pressed = up_say
    ok_button.when_pressed = ok_say
    down_button.when_pressed = down_say

    screen = Screen()

    pause()
    
def up_say():
    global screen
    screen.next()       

if __name__ == '__main__':
    main()