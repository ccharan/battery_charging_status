#!/usr/bin/env python
import PySimpleGUI as sg
import battery as bt
import time
import queue
import threading
from utils import get_percentage


ICON = b'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'
mac_button = b'iVBORw0KGgoAAAANSUhEUgAAANMAAAAVCAYAAADctttwAAAAp0lEQVR4Xu3coRHCQBRF0fSyhBkUGAyCcqIpg9oogw5ogMAPJqAgPHl25qjVd1a97brnaa0fVpvttbU2At97ddMP1dEU0np3vO1Pl/FwvgM/qG6qnymoKktIsFz1Ux119VR9XgK/qY7EBAFighAxQYiYIERMECImCBEThIgJQsQEIWKCEDFBiJggREwQIiYImWKyZ4L/zPZMlraw1NvS1h8QsNz8D4gHGbEQKb1NXMcAAAAASUVORK5CYII='
BG_COLOR = '#29272c'

sg.theme('Dark')
sg.set_options(element_padding=(0, 0))
gui_queue = queue.Queue()
STARTED = False
RUNNING = False

layout = [[sg.Text('Battery Percentage', background_color=BG_COLOR, pad=(0, 4))],
          [sg.ProgressBar(100, orientation='h', size=(50, 20), key='PBAR', bar_color=('green', '#c2f542')),
           sg.Text('', key='PCENT', enable_events=True, visible=True, background_color=BG_COLOR, pad=(5, 0))],
          [sg.Text('', background_color=BG_COLOR)],
          [sg.Button('Start', image_data=mac_button,  button_color=('white', BG_COLOR), mouseover_colors=('white', BG_COLOR),
                     key='START', pad=(0, 0), expand_x=True),
           sg.Button('Stop', image_data=mac_button,  button_color=('white', BG_COLOR), mouseover_colors=('white', BG_COLOR),
                     key='STOP', pad=(20, 0), expand_x=True)]]

window = sg.Window("Battery Charge Status", layout,
                   finalize=True,
                   background_color=BG_COLOR,
                   icon=ICON)


def long_operation_thread(gui_queue):
    bt.main()
    gui_queue.put(None)


def update_percentage_bar(gui_queue):
    global RUNNING
    while RUNNING:
        window['PBAR'].update(current_count=get_percentage())
        window['PCENT'].update(str(get_percentage()) + "%")
        time.sleep(150)
        gui_queue.put(None)


while True:
    event, values = window.Read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'START' and not STARTED:
        bt.RUNNING = True
        RUNNING = True
        threading.Thread(target=long_operation_thread, args=(gui_queue,), daemon=True).start()
        threading.Thread(target=update_percentage_bar, args=(gui_queue,), daemon=True).start()
        STARTED = True
        window['START'].update("Started")
        window['STOP'].update("Stop")
    elif event == 'STOP':
        bt.RUNNING = False
        STARTED = False
        window['START'].update("Start")
        window['STOP'].update("Stopped")

    try:
        message = gui_queue.get_nowait()
    except queue.Empty:
        message = None

    if message:
        print('Got a message back from the thread: ', message)

window.close()
