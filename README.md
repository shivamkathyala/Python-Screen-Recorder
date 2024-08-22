# Python-Screen-Recorder

This project is a simple screen recorder built in Python that captures the screen and saves the recording as an MP4 file. It uses `numpy`, `pyautogui`, and `opencv` to handle the screen capturing and video encoding. Additionally, a standalone executable for Windows has been created using PyInstaller, so you can run the screen recorder without needing to install Python or any dependencies.

## Features
- Records the entire screen.
- Saves the video in MP4 format.
- Adjustable frame rate and resolution.
- Real-time display of the recording window.
- Standalone executable for Windows, no need for Python installation.

## Requirements
To run the script directly (without the executable), you'll need to have the following Python packages installed:
- `numpy`
- `pyautogui`
- `opencv-python`

You can install them using pip: 
- `pip install numpy pyautogui opencv-python`

## Creating the Standalone Executable

If you wish to create your own standalone executable, follow these steps:

1. **Install PyInstaller**:
-  `pip install pyinstaller`
2. **Create the Executable**:
-  `pyinstaller --onefile --windowed screenRecorder.py`
