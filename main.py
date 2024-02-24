from Screen import Screen
from gpiozero import Button
from signal import pause


def main():

    # Pins dels bottons
    up_button = Button(17)
    ok_button = Button(19)
    down_button = Button(11)



    def ok_say():
        pass

    def down_say():
        pass



    screen = Screen()
    
    def up_say():
        print(1)
        screen.next()

    up_button.when_pressed = up_say
    ok_button.when_pressed = ok_say
    down_button.when_pressed = down_say

    pause()


if __name__ == '__main__':
    main()