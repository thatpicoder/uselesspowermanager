import ctypes
import platform
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

WINDOWS = platform.system() == "Windows"

if not WINDOWS:
    message = "This app is designed to run on Windows."
    print(message)
    sys.exit(1)


def run_shutdown_command(args):
    try:
        subprocess.run(["shutdown"] + args, check=True)
    except subprocess.CalledProcessError as ex:
        messagebox.showerror("Error", f"Command failed: {ex}")


def on_log_out():
    run_shutdown_command(["/l"])


def on_shutdown():
    run_shutdown_command(["/s", "/t", "0"])


def on_restart():
    run_shutdown_command(["/r", "/t", "0"])


def on_sleep():
    try:
        success = ctypes.windll.powrprof.SetSuspendState(False, True, True)
        if not success:
            raise OSError("SetSuspendState returned failure")
    except Exception:
        messagebox.showerror(
            "Error",
            "Unable to enter sleep mode. Run as administrator or try a different power setting."
        )


def create_ui():
    root = tk.Tk()
    root.title("useless power manager v1.0")
    root.resizable(False, False)

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    label = tk.Label(frame, text="made by bitetheapple", font=("Segoe UI", 12))
    label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    btn_logout = tk.Button(frame, text="Log out", width=15, command=on_log_out)
    btn_shutdown = tk.Button(frame, text="Shut down", width=15, command=on_shutdown)
    btn_restart = tk.Button(frame, text="Restart", width=15, command=on_restart)
    btn_sleep = tk.Button(frame, text="Sleep", width=15, command=on_sleep)

    btn_logout.grid(row=1, column=0, padx=5, pady=5)
    btn_shutdown.grid(row=1, column=1, padx=5, pady=5)
    btn_restart.grid(row=2, column=0, padx=5, pady=5)
    btn_sleep.grid(row=2, column=1, padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    create_ui()
