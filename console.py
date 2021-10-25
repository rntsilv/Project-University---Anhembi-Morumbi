import time, sys


def clearScreen():
    print("\x1b[H\x1b[2J")


def clearLine():
    print("\x1b[2K\r")


def animated(loading):
    chars = "|/—\|/—\|" 
    for char in chars:
        sys.stdout.write("\r" + loading + " " + char)
        time.sleep(0.3)
        sys.stdout.flush()
