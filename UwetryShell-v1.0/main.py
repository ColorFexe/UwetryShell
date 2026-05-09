from pathlib import Path
import sys

project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from core.boostrap.get import default_config
from core.boostrap.get.program_get import JsonData
from core.boostrap.start_init import program_init
from shell.cmd_api import main as cmd_api

def main() -> None:
    print(f"^ UwetryShell V{int(default_config.Data().program_version())} ^")
    while True:
        command = input(f"$ {JsonData().setting()['current_path']}> ")
        cmd_api(command)

if __name__ == "__main__":
    program_init()
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)