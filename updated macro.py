import json
import time
from pynput import mouse
import customtkinter as ctk  # Import customtkinter
import pyautogui  # Make sure to install this library
import keyboard as kb  # For hotkey functionality
import tkinter as tk
from tkinter import filedialog
from CTkListbox import *
import os
import threading  # Import threading at the top of your file
import random

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        if self.tooltip_window is not None:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip_window, text=self.text, background="lightyellow", borderwidth=1, relief="solid")
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

class MouseClickRecorderUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Macro")
        self.recorder = MouseClickRecorder(self.log_click)  # Pass the logging function
        self.log_count = 0  # Initialize log count
        


        # Initialize recent_files as an empty list
        self.recent_files = []

        # Set the size of the main window
        self.master.geometry("235x375")  # Increased height for the checkbox

        # Start and Stop buttons in the first row
        self.record_button = ctk.CTkButton(master, text="Rec", command=self.start_recording, width=80)
        self.record_button.grid(row=4, column=0, sticky='w', padx=(25, 0), pady=(20, 10))
        ToolTip(self.record_button, "Hotkey: R")  # Add tooltip for record button

        self.stop_button = ctk.CTkButton(master, text="Stop Rec", command=self.stop_recording, width=80)
        self.stop_button.grid(row=4, column=1, sticky='e', padx=(25, 0), pady=(20, 10))
        ToolTip(self.stop_button, "Hotkey: S")  # Add tooltip for stop button

        # Play and Reset buttons in the third row
        self.play_button = ctk.CTkButton(master, text="Play", command=self.play_macro, width=80)
        self.play_button.grid(row=6, column=0, sticky='w', padx=(25, 0), pady=(20, 10))
        ToolTip(self.play_button, "Hotkey: P")  # Add tooltip for play button

        self.load_button = ctk.CTkButton(master, text="Load", command=self.load_macro, width=80)
        self.load_button.grid(row=6, column=1, sticky='e', padx=(25, 0), pady=(20, 10))
        ToolTip(self.load_button, "Hotkey: L")  # Add tooltip for load button

        # Save and Reset buttons in the second row
        self.save_button = ctk.CTkButton(master, text="Save", command=self.save_macro, width=80)
        self.save_button.grid(row=5, column=0, sticky='w', padx=(25, 0))
        ToolTip(self.save_button, "Hotkey: Z")  # Add tooltip for save button

        self.reset_button = ctk.CTkButton(master, text="Reset", command=self.reset_macro, width=80)
        self.reset_button.grid(row=5, column=1, sticky='e', padx=(25, 0))
        ToolTip(self.reset_button, "Hotkey: D")  # Add tooltip for reset button

        # Recently used macro files list box
        self.recent_files_listbox = CTkListbox(master, height=30)  # Use CTkListbox instead of CTkTextbox
        self.recent_files_listbox.grid(row=7, column=0, columnspan=2, padx=(25, 0), pady=(10, 10))

        # Checkbox for enabling/disabling random delay
        self.delay_var = tk.BooleanVar(value=False)  # Default to True (enabled)
        self.delay_checkbox = ctk.CTkCheckBox(master, text_color="lime", text="Playback Delay", variable=self.delay_var)
        self.delay_checkbox.grid(row=8, column=0, columnspan=2, padx=(25, 0), pady=(10, 10))

        # Logging Textbox
        self.log_textbox = ctk.CTkTextbox(master, height=50, width=175, state=tk.DISABLED)  # Set state to DISABLED
        self.log_textbox.grid(row=10, column=0, columnspan=2, padx=(20, 0), pady=(10, 10))

        # Set up hotkeys
        kb.add_hotkey('R', self.start_recording)  # Press F2 to start recording
        kb.add_hotkey('S', self.stop_recording)   # Press F3 to stop recording
        kb.add_hotkey('P', self.play_macro)       # Press F4 to play the recorded macro
        kb.add_hotkey('Z', self.save_macro)       # Press F5 to save the recorded macro
        kb.add_hotkey('L', self.load_macro)       # Press F6 to load a macro from a file
        kb.add_hotkey('D', self.reset_macro)      # Press F7 to reset the macro

        

        # Add this line in the __init__ method of MouseClickRecorderUI
        self.status_label = ctk.CTkLabel(master, text="Status: Idle", text_color="white")
        self.status_label.grid(row=9, column=0, columnspan=2, pady=(10, 0))

    def log_click(self, message):
        self.log_textbox.configure(state=tk.NORMAL)  # Enable the textbox for editing
        self.log_textbox.insert(tk.END, message + "\n")  # Insert log message into the textbox
        self.log_textbox.see(tk.END)  # Scroll to the end of the textbox
        self.log_textbox.configure(state=tk.DISABLED)  # Disable the textbox again

    def play_macro(self):
        if not self.master.winfo_exists():  # Check if the window still exists
            return  # Exit if the window is closed

        # Update status to "Playing..."
        self.status_label.configure(text="Status: Playing...", text_color="yellow")  # Change color to indicate playing

        # Start a new thread for playing the macro
        playback_thread = threading.Thread(target=self._play_macro_thread)
        playback_thread.start()

    def _play_macro_thread(self):
        self.recorder.play_macro(self.delay_var.get())  # Pass the delay option
        if self.master.winfo_exists():  # Check if the window still exists
            self.status_label.after(0, lambda: self.status_label.configure(text="Status: Finished", text_color="purple"))  # Reset status

    def start_recording(self):
        self.recorder.start_recording()
        self.status_label.configure(text="Status: Recording...", text_color="Green")  # Update status

    def stop_recording(self):
        self.recorder.stop_recording()
        self.status_label.configure(text="Status: Stopped", text_color="Red")  # Reset status

    def save_macro(self):
        # Create a hidden root window to use the file dialog
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            self.recorder.save_macro(filename)
            self.add_recent_file(filename)  # Add to recent files
            self.log_click("Saved Macro")  # Log the reset action

    def load_macro(self):
        # Create a hidden root window to use the file dialog
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filename:
            self.recorder.load_macro(filename)
            self.add_recent_file(filename)  # Add to recent files
            self.log_click("Loaded File")  # Log the reset action

    def load_recent_macro(self, event):
        # Get the selected index from the Listbox
        selected_index = self.recent_files_listbox.curselection()
        
        if selected_index:  # Check if an item is selected
            selected_file = self.recent_files_listbox.get(selected_index)  # Get the selected file
            self.recorder.load_macro(selected_file)  # Load the selected macro file

    def add_recent_file(self, filename):
        file_name_only = os.path.basename(filename)  # Get just the file name
        if file_name_only not in self.recent_files:
            self.recent_files.append(file_name_only)  # Store only the file name
            self.recent_files_listbox.insert(ctk.END, file_name_only)  # Insert into Listbox
        # Limit the number of recent files to 5
        if len(self.recent_files) > 1:  # Change to 5 to limit to 5 recent files
            removed_file = self.recent_files.pop(0)  # Remove the oldest
            self.recent_files_listbox.delete(0)  # Remove from Listbox

    def reset_macro(self):
        self.recorder.events = []  # Clear recorded events
        self.recent_files_listbox.delete(0, ctk.END)  # Clear the recent files listbox
        self.recent_files.clear()  # Clear the recent files list
        self.status_label.configure(text="Status: Reset", text_color="black")  # Reset status
        self.log_click("Reset macro")  # Log the reset action
        print("Macro reset.")  # Debug print

    def log_click(self, message):
        self.log_textbox.configure(state=tk.NORMAL)  # Enable the textbox for editing
        self.log_textbox.insert("1.0", message + "\n")  # Insert log message at the top
        
        # Limit the number of lines to 10
        lines = self.log_textbox.get("1.0", tk.END).splitlines()
        if len(lines) > 10:
            self.log_textbox.delete(f"{len(lines)}.0", tk.END)  # Remove the last line if more than 10
        
        self.log_textbox.see("1.0")  # Scroll to the top of the textbox
        self.log_textbox.configure(state=tk.DISABLED)  # Disable the textbox again
            
        self.log_count += 1  # Increment the log count
        
        # Clear logs if count exceeds 10
        if self.log_count > 10:
            self.log_textbox.configure(state=tk.NORMAL)  # Enable the textbox for editing
            self.log_textbox.delete(1.0, tk.END)  # Clear all text
            self.log_textbox.configure(state=tk.DISABLED)  # Disable the textbox again
            self.log_count = 0  # Reset the log count

            # Bind the close event to the cleanup method
            self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        # Stop the mouse listener if it's running
        if self.recorder.mouse_listener is not None:
            self.recorder.stop_recording()  # Ensure recording is stopped
        self.master.quit()  # Stop the main loop
        self.master.destroy()  # Close the application


class MouseClickRecorder:
    def __init__(self, log_function):
        self.events = []
        self.recording = False
        self.mouse_listener = None
        self.start_time = None
        self.log_function = log_function  # Store the logging function

    def on_click(self, x, y, button, pressed):
        if self.recording:
            current_time = time.time() - self.start_time
            event = {
                'type': 'click',
                'x': x,
                'y': y,
                'button': str(button),
                'pressed': pressed,
                'time': current_time
            }
            self.events.append(event)
           

    def start_recording(self):
        if not self.recording:  # Prevent starting multiple recordings
            self.recording = True
            self.events = []
            self.start_time = time.time()  # Record the start time
            self.mouse_listener = mouse.Listener(on_click=self.on_click)
            self.mouse_listener.start()
            print("Recording started...")  # Debug print

    def stop_recording(self):
        if self.recording:  # Only stop if currently recording
            self.recording = False
            if self.mouse_listener:
                self.mouse_listener.stop()
            
            # Check if the last recorded event is a click event
            if self.events and self.events[-1]['type'] == 'click':
                self.events.pop()  # Remove the last click event
            
            print("Recording stopped.")  # Debug print

    def save_macro(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.events, f)
            print(f"Macro saved to {filename}")  # Debug print

    def load_macro(self, filename):
        with open(filename, 'r') as f:
            self.events = json.load(f)
            print(f"Macro loaded from {filename}")  # Debug print

    def play_macro(self, use_random_delay):
        if not self.events:
            self.log_function("No events to play.")  # Log if no events
            return

        start_time = time.time()
        for i, event in enumerate(self.events):
            if i > 0:
                # Calculate the time to wait based on the previous event
                wait_time = event['time'] - self.events[i - 1]['time']
                time.sleep(wait_time)

            if event['type'] == 'click':
                x, y = event['x'], event['y']
                if event['pressed']:
                    pyautogui.click(x, y)  # Simulate mouse click
                    
                    # Prepare the log message
                    log_message = f"({x}, {y})"
                    
                    # Introduce a random delay between 50ms to 300ms after each click if enabled
                    if use_random_delay:
                        random_delay = random.uniform(0.05, 0.3)  # Random delay between 0.05 and 0.3 seconds
                        time.sleep(random_delay)
                        
                        # Append the delay to the log message
                        log_message += f" + {random_delay:.3f} s"
                    
                    # Log the message
                    self.log_function(log_message)



if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Set the appearance mode to dark
    ctk.set_default_color_theme("green")  # Set the default color theme
    root = ctk.CTk()  # Create a CTk window
    app = MouseClickRecorderUI(root)
    root.resizable(False, False)  # Lock the application size
    root.mainloop()