# UwetryShell

A lightweight, cross-platform terminal shell written in pure Python.

## Features

- Cross-platform support: Windows, macOS, Linux, and Android
- Persistent configuration storage
- Built-in commands for daily terminal operations
- Extensible command structure

## Prerequisites

- Python 3.8 or higher
- `colorama` (for cross-platform color/clear support)

## Installation

```bash
git clone https://github.com/ColorFexe/UwetryShell.git
cd UwetryShell
pip install colorama
Usage
Run the shell:

bash
python main.py
Built-in Commands
Command	Description
help	Display the list of available commands
exit	Exit the shell
clear	Clear the console screen
cd <path>	Change the current working directory
ls	List contents of the current directory
Example Session
text
$ UwetryShell V1 ^
$ C:\Users> cd Documents
$ C:\Users\Documents> ls
Path: "C:\Users\Documents"
[Dir]  Projects
[File] readme.txt
$ C:\Users\Documents> exit
Configuration
UwetryShell stores its configuration files in platform-appropriate directories:

Platform	Config Path
Windows	%APPDATA%\UwetryShell\
macOS	~/Library/Application Support/UwetryShell/
Linux	~/.config/UwetryShell/
Android	EXTERNAL_STORAGE/UwetryShell/
Settings File
The main configuration is stored as JSON at:

text
UwetryShell/v{version}/config/setting.json
Example configuration:

json
{
  "language": "en-US",
  "default_path": "C:\\Users",
  "current_path": null
}
Project Structure
text
UwetryShell/
├── main.py                 # Entry point
├── core/
│   ├── bootstrap/          # Initialization and configuration
│   │   ├── get/           # System info and path utilities
│   │   ├── setup.py       # File/directory operations
│   │   └── start_init.py  # First-run setup
│   └── render.py          # Console rendering
└── shell/
    ├── Shell.py           # Command dispatcher
    └── commands/          # Individual command implementations
        ├── cd.py
        ├── clear.py
        ├── exit.py
        ├── help.py
        └── ls.py
License
This project is licensed under the GNU General Public License v3.0.

This means:

You can use, modify, and distribute this software

Any derivative work must also be open source under the same license

Commercial use is permitted, but source code must be disclosed

See the LICENSE file for full details.

Contributing
Contributions are welcome! Please ensure any pull request:

Maintains compatibility with all supported platforms

Follows the existing code structure

Author
ColorFexe

Acknowledgments
Built with Python's standard library

colorama for terminal control across platforms
