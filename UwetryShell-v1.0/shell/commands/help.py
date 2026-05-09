from .. import Shell

def main() -> None:
    print("Available commands:")
    for cmd in Shell.cmd_list():
        print(f"- {cmd}: {Shell.cmd_dict()[cmd]}")