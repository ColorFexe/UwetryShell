class Data:
    def __init__(self) -> None:
        self.name = "UwetryShell"
        self.version = 1.0

    def program_version(self) -> float:
        return self.version

    def program_name(self) -> str:
        return self.name


class JsonData:
    def __init__(self) -> None:
        self.program_version = Data().program_version()
        self.program_name = Data().program_name()
    
    def json_setting(self) -> dict:
        return {
            "language": "en-US",
            "default_path": "C:\\Users",
            "current_path": None,
        }