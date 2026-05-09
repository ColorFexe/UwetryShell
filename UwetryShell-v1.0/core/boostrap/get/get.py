import platform
import os

class System:
    """系统相关"""
    def __init__(self) -> None:
        self.system = platform.system() # 获取系统名
        self.kernel = os.name  # 获取内核名
        self.system_version = platform.version() # 系统版本
    
    def system_name(self) -> str | None:
        """获取详细系统名 Windows Android Linux Darwin"""
        if self.system.lower() in ['windows', 'darwin']:
            return self.system.lower()
        elif self.system.lower() == 'linux':
            if hasattr(platform, "android_ver") or self.system.lower() == 'android' or "ANDROID_STORAGE" in os.environ:
                return 'android'
            else:
                return 'linux'
        else:
            return None
    
    def kernel_name(self) -> str | None:
        """获取内核名 NT POSIX"""
        if self.kernel.lower() in ['nt', 'posix']:
            return self.kernel.lower()
        else:
            return None
    
    def system_version(self) -> str:
        """获取系统版本"""
        return self.system_version