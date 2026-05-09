from .commands import (help, exit, clear, cd, ls)

def process(data: str) -> bool:
    data_a = data.split(' ', 1)[0]
    if data_a == "help": help.main(); return True
    elif data_a == "exit": exit.main(); return True
    elif data_a == "clear": clear.main(); return True
    elif data_a == "cd": cd.main(data); return True
    elif data_a == "ls": ls.main(); return True
    else: return False

def cmd_list() -> list[str]:
    # "cat", "mkdir", "rm", "mv", "cp", "touch", "pwd"
    return [
        "help", "exit", "clear", "cd", "ls",
    ]

def cmd_dict() -> dict[str, str]:
    return {
        "help": "Instruction list.",
        "exit": "Exit the program.",
        "clear": "Clear the console.",
        "cd": "Change the current directory.",
        "ls": "List the contents of the current directory.",
    }