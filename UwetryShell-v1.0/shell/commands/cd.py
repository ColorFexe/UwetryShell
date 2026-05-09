from core.boostrap.setup import Write
from core.boostrap.get.program_get import Path
import re
import os


def main(data: str) -> None:
    try:
        args = data.split(' ', 1)[1].strip()
    except IndexError:
        print("usage: cd <path>")
        return
    if not args:
        print("usage: cd <path>")
        return
    path = _extract_path(args)
    if not path:
        print("cd Error: Path cannot be empty.")
        return
    _change_dir(path)

def _extract_path(args: str) -> str:
    match = re.match(r'''(["'])(.*?)\1''', args)
    if match:
        return match.group(2)
    return args

def _change_dir(path: str) -> None:
    expanded = os.path.expanduser(path)
    if not os.path.isabs(expanded):
        expanded = os.path.abspath(expanded)
    if not os.path.exists(expanded):
        print(f"cd Error: The path '{path}' does not exist.")
        return
    if not os.path.isdir(expanded):
        print(f"cd Error: The path '{path}' is not a directory.")
        return
    try:
        os.chdir(expanded)
    except PermissionError:
        print(f"cd Error: Permission denied: '{path}'.")
        return
    Write().Json(Path().path_json_setting()).update("current_path", expanded)