from . import Shell

def main(data: str) -> None:
    result = Shell.process(data)
    if not result:
        data = data.split(' ', 1)[0]
        if data.strip() == "":
            return None
        if data.strip() not in Shell.cmd_list() or data.strip() not in Shell.cmd_list():
            print(f"Unknown command: '{data}'. Type 'help' for a list of commands.")