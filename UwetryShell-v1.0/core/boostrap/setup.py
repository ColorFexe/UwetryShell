from pathlib import Path
import os
import json

"""创建文件/目录或删除文件/目录"""

class Add:
    """创建类"""
    def __init__(self, path: str) -> None:
        self.path = path
    
    def dirs(self) -> None:
        """创建目录"""
        os.makedirs(self.path, exist_ok=True)
    
    def file(self) -> None:
        """创建文件"""
        Path(self.path).touch(exist_ok=True)


class Remove:
    """删除类"""
    def __init__(self, path: str) -> None:
        self.path = path
    
    def dirs(self) -> None:
        """删除目录"""
        if os.path.exists(self.path):
            os.rmdir(self.path)
    
    def file(self) -> None:
        """删除文件"""
        if os.path.exists(self.path):
            os.remove(self.path)


class Write:
    """写入类"""
    class Json:
        def __init__(self, path: str) -> None:
            self.path = path
        
        def write(self, data: dict) -> None:
            """写入json文件"""
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        
        def update(self, key: str, value: str) -> None:
            """更新json文件"""
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
            data[key] = value
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)