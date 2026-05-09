from . import get
from . import default_config
import os
import json

"""获取程序根目录/配置文件等路径或数据"""

class CompatibilityError(Exception):
    """不兼容的操作系统异常"""
    pass

class Path:
    """路径类"""
    def __init__(self) -> None:
        self.system = get.System()
        self.user = str(os.getlogin())

    def system_user_name(self) -> str:
        """获取系统用户名"""
        return self.user

    def root_directory(self) -> str:
        """获取根目录"""
        if self.system.system_name() == 'windows':
            return str(os.path.join(os.getenv('APPDATA'), 'UwetryShell'))
        elif self.system.system_name() == 'darwin':
            return str(os.path.join(os.path.expanduser('~'), 'Library', 'Application Support', 'UwetryShell'))
        elif self.system.system_name() == 'linux':
            return str(os.path.join(os.path.expanduser('~'), '.config', 'UwetryShell'))
        elif self.system.system_name() == 'android':
            return str(os.path.join(os.getenv('EXTERNAL_STORAGE'), 'UwetryShell'))
        else:
            raise CompatibilityError("Incompatible operating system. UwetryShell only supports Windows, macOS, Linux and Android.")
    
    def root_directory_version(self) -> str:
        """获取根目录版本路径"""
        return str(os.path.join(self.root_directory(), f'v{default_config.Data().program_version()}'))
    
    def directory_config(self) -> str:
        """获取配置目录路径"""
        return str(os.path.join(self.root_directory_version(), 'config'))

    def path_json_setting(self) -> str:
        """获取配置文件路径"""
        return str(os.path.join(self.directory_config(), 'setting.json'))


class JsonData:
    """获取配置文件数据"""
    def __init__(self) -> None:
        pass

    def setting(self) -> dict:
        """读取设置文件"""
        with open(Path().path_json_setting(), "r", encoding="utf-8") as f:
            return json.load(f)