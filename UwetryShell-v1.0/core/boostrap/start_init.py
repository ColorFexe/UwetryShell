from core.boostrap.get.program_get import Path
from core.boostrap.setup import Add
from core.boostrap.setup import Write
from core.boostrap.get import default_config
from core.boostrap.get.program_get import JsonData
import os

def program_init() -> None:
    """程序初始化"""
    """目录"""
    if not os.path.exists(Path().root_directory()): # /UwetryShell
        Add(Path().root_directory()).dirs()
    if not os.path.exists(Path().root_directory_version()): # /UwetryShell/Vx.x
        Add(Path().root_directory_version()).dirs()
    if not os.path.exists(Path().directory_config()): # /UwetryShell/Vx.x/config
        Add(Path().directory_config()).dirs()
    """文件"""
    if not os.path.exists(Path().path_json_setting()): # /UwetryShell/Vx.x/config/setting.json
        Add(Path().path_json_setting()).file()
        Write.Json(Path().path_json_setting()).write(default_config.JsonData().json_setting())
    
    Write.Json(Path().path_json_setting()).update("current_path", JsonData().setting()['default_path'])