from pynput.keyboard import Key, Listener, KeyCode
from pynput import mouse

keys_pressed = -1
mouse_clicked = 0
results = []

def knappNed(key):
    global keys_pressed
    global results
    global mouse_clicked
    keys_pressed += 1
    if(key == Key.esc):
        print(results)
        exit()
    try:
        if(key.char == "+"):
            r = (keys_pressed, mouse_clicked)
            results.append(r)
            print(results)
            keys_pressed = -1
            mouse_clicked = 0
        if(key.char == "|"):
            results = []
            keys_pressed = 0
            mouse_clicked = 0
    except:
        pass

def musKlikk(x, y, button, pressed):
    global keys_pressed
    global mouse_clicked
    mouse_clicked += 0.5


listener = mouse.Listener(on_click=musKlikk)
listener.start()
with Listener(on_release=knappNed) as listener:
    listener.join()