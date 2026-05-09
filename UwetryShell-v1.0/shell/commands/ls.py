from core.boostrap.get import program_get
import os

def main() -> None:
    path = program_get.JsonData().setting()['current_path']
    try:
        with os.scandir(path) as a:
            print(f'Path: "{path}"')
            for i in a:
                print('[Dir]', i.name) if i.is_dir() else print('[File]', i.name)
    except Exception as e:
        print(f"ls Error: {e}")