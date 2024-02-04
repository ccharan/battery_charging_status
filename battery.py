import psutil
import os
import time

RUNNING = None
HIGH_BATTERY_THRESHOLD = 80
LOW_BATTERY_THRESHOLD = 40


def get_battery_level():
    battery = psutil.sensors_battery()
    if battery is None:
        return "No battery detected"
    else:
        return battery.percent


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def main():
    global RUNNING
    while RUNNING:
        percentage = get_battery_level()
        if percentage >= HIGH_BATTERY_THRESHOLD:
            os.system(f'say "Battery reached {percentage}%"')
            notify("Title", f"Battery reached {percentage}%")
        elif percentage <= LOW_BATTERY_THRESHOLD:
            os.system(f'say "Battery reached {percentage}%"')
            notify("Title", f"Battery reached {percentage}%")
        time.sleep(150)
