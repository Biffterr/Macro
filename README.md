# Basic Macro Recorder made in Python.

  Beginner coder and decided to start with python using the help of AI, Code might be laidout wrong or have/use unnecessary code.

# Feel free to use or modify :)


A simple mouse click recorder and macro player built with Python. This application allows users to record mouse clicks, save them as macros, and play them back at a later time. It features a user-friendly interface and supports hotkeys for quick access to functionalities.


## Features

- **Record Mouse Clicks**: Start and stop recording mouse clicks with a simple button or hotkey.
- **Playback Macros**: Play back recorded mouse clicks with the option to adjust timing.
- **Save and Load Macros**: Save recorded macros to a JSON file and load them back for playback.
- **Recent Files List**: Keep track of recently used macro files for quick access.
- **Hotkey Support**: Use keyboard shortcuts to control recording, playback, saving, and loading of macros.
- **User  Interface**: Built with `customtkinter` for a modern look and feel.

## Modules Used

- **pynput**: For listening to mouse events and recording clicks.
- **pyautogui**: For simulating mouse clicks during playback.
- **keyboard**: For handling hotkey functionality.
- **tkinter**: For creating the GUI.
- **customtkinter**: A custom version of tkinter for enhanced UI components.
- **json**: For saving and loading macro data in JSON format.
- **os**: For file path manipulations.
- **threading**: For running playback in a separate thread to keep the UI responsive.

## Installation

To run this application, you need to have Python installed on your machine. You can install the required modules using pip:


pip install pynput pyautogui keyboard customtkinter CTkListbox


## Usage
 - Run the Application: Execute the script to launch the application.

 - Start Recording: Click the "Rec" button or press the R key to start recording mouse clicks.
 - Stop Recording: Click the "Stop Rec" button or press the S key to stop recording.
 - Play Macro: Click the "Play" button or press the P key to play back the recorded clicks.
 - Save Macro: Click the "Save" button or press the Z key to save the recorded macro to a file.
 - Load Macro: Click the "Load" button or press the L key to load a previously saved macro.
 - Reset Macro: Click the "Reset" button or press the D key to clear the recorded events and reset the application.
 
   ![start](https://github.com/user-attachments/assets/9ac3514e-b8a5-42d4-bd5e-92aa107d457d)
   ![stop](https://github.com/user-attachments/assets/f8ed8aec-63dc-4ae0-8c73-4f7fbc240f7c)



