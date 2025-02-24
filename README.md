# Basic Macro Recorder made in Python.

  Learning python with the help of AI, Code might be laidout wrong or have/use unnecessary code.

# Feel free to use or modify :)


## Features

- **Record Mouse Clicks**: Start and stop recording mouse clicks with a simple button or hotkey.
- **Playback Macros**: Play back recorded mouse clicks with optional random delays.
- **Save and Load Macros**: Save recorded macros to JSON files and load them for playback later.
- **Current Loaded File List**: Lets you know what your current loaded file is.
- **Logging**: View a log of playback events, Displayed as Coords (+ Seconds if the delay is enabled).
- **Hotkey Support**: Use keyboard shortcuts to control recording, playback, saving, and loading of macros.
- **Playback Delay**:  Option: Enable or disable random delays during playback.

## Modules Used

- **pynput**: For listening to mouse events and recording clicks.
- **pyautogui**: For simulating mouse clicks during playback.
- **keyboard**: For handling hotkey functionality.
- **tkinter**: For creating the GUI.
- **customtkinter**: A custom version of tkinter for enhanced UI components.
- **json**: For saving and loading macro data in JSON format.
- **os**: For file path manipulations.
- **threading**: For running playback in a separate thread to keep the UI responsive.


## Usage

 - Start Recording: Click the "Rec" button or press the F1 key to start recording mouse clicks.
 - Stop Recording: Click the "Stop Rec" button or press the F2 key to stop recording.
 - Play Macro: Click the "Play" button. 
 - Save Macro: Click the "Save" button. 
 - Load Macro: Click the "Load" button.
 - Reset Macro: Click the "Reset" button. 
 
   
![screen](https://github.com/user-attachments/assets/432f7413-e0fc-4dc7-81bc-e43676d6d24d)
![2](https://github.com/user-attachments/assets/64a18dba-23b8-4323-9093-8813149e69b8)



