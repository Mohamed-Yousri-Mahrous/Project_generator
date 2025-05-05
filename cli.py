from ast import Return
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
from pathlib import Path


def pause():
    """
    Pause the program until the user presses Enter.
    """
    print(create_border())
    input("Press Enter to continue...")


def welcome(program_name, program_description, fun_list, border_size=80):
    """
    Display a welcome message.
    """
    message = [
        create_border(),
        f" Welcome to the {program_name} program! ".center(border_size, "="),
        f" {program_description} ".center(border_size, "="),
        create_border(),
        fun_list,
        create_border(),
    ]
    print("\n".join(message))


def clear_screen():
    """
    Clear the console screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def create_border(border_size=80):
    """
    Create a border.
    """
    return "=" * border_size


def select_folder(folder_title):
    app = Tk()
    app.withdraw()
    folder_name = askdirectory(title=folder_title)
    app.destroy()
    return Path(folder_name)


def init_WorkingDirectory(folder_title="Please Select Destination place"):
    destination_directory = select_folder(folder_title)
    os.chdir(destination_directory)
    print(f"The Destination place >> {Path.cwd()}", end="\n\n")


def check_name(file_name):
    """
    Check if a file name already exists or Not.
    return True if Valid and not exists.
    """
    return False if any(file == file_name for file in os.listdir()) else True
