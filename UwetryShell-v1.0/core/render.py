from .boostrap.get import get
import os
import colorama

def clear() -> None:
    """清屏"""
    system_name = get.System().system_name()
    if system_name == 'windows':
        os.system('cls')
    elif system_name in['linux', 'android', 'darwin']:
        os.system('clear')
    else:
        colorama.init()
        print("\033[2J\033[H", end="")