import tkinter as tk
from tkinter import messagebox
import threading
import time
from ping3 import ping


# Small tool to monitor network devices and alert if they are down, opens a GUI window 



def check_device(ip):
    try:
        response = ping(ip, timeout=2)
        return response is not None
    except Exception:
        return False

def monitor_devices():
    while monitoring:
        for ip in list(devices):  # Use a copy of the list to avoid modification issues
            if ip not in devices:  # Skip devices that have been removed
                continue
            set_status(f"Checking {ip}...")
            start_counter()
            if not check_device(ip):
                messagebox.showerror("Device Down Alert", f"Device {ip} is down!")
            stop_counter()
        set_status("All devices are up to date.")
        time.sleep(interval)

def start_monitoring():
    global monitoring
    monitoring = True
    thread = threading.Thread(target=monitor_devices)
    thread.daemon = True
    thread.start()
    start_spinner()

def stop_monitoring():
    global monitoring
    monitoring = False

def add_device():
    ip = entry_ip.get()
    if ip:
        devices.add(ip)  # Add to set
        listbox_devices.insert(tk.END, ip)
        entry_ip.delete(0, tk.END)

def remove_device():
    selected_ip = listbox_devices.get(tk.ACTIVE)
    if selected_ip in devices:
        devices.remove(selected_ip)
        listbox_devices.delete(tk.ACTIVE)

def set_status(message):
    status_label.config(text=message)

def start_spinner():
    spinner_label.after(100, animate_spinner, 0)

def animate_spinner(index):
    spinner_label.config(text=spinner_frames[index % len(spinner_frames)])
    if monitoring:
        spinner_label.after(100, animate_spinner, index + 1)

def start_counter():
    global start_time
    start_time = time.time()
    update_counter()

def update_counter():
    elapsed_time = int(time.time() - start_time)
    counter_label.config(text=f"Elapsed Time: {elapsed_time} seconds")
    if monitoring:
        counter_label.after(1000, update_counter)

def stop_counter():
    counter_label.config(text="")

# List of devices to monitor
devices = set()

# Monitoring interval (in seconds)
interval = 60

# Spinner frames
spinner_frames = ['|', '/', '-', '\\']

# Create the main window
root = tk.Tk()
root.title("Network Device Monitoring Widget")

# Set dark theme colors
bg_color = "#333333"
fg_color = "#FFFFFF"
btn_bg_color = "#444444"
btn_fg_color = "#FFFFFF"
listbox_bg_color = "#222222"

# Apply dark theme to the main window
root.configure(bg=bg_color)

# Define grid configuration
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

# IP Entry
entry_ip = tk.Entry(root, width=50, bg=listbox_bg_color, fg=fg_color, insertbackground=fg_color)
entry_ip.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
entry_ip.insert(0, "Enter IP or URL")

# Add Button
btn_add = tk.Button(root, text="Add Device", command=add_device, bg=btn_bg_color, fg=btn_fg_color)
btn_add.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

# Remove Button
btn_remove = tk.Button(root, text="Remove Device", command=remove_device, bg=btn_bg_color, fg=btn_fg_color)
btn_remove.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Start Button
btn_start = tk.Button(root, text="Start Monitoring", command=start_monitoring, bg=btn_bg_color, fg=btn_fg_color)
btn_start.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

# Stop Button
btn_stop = tk.Button(root, text="Stop Monitoring", command=stop_monitoring, bg=btn_bg_color, fg=btn_fg_color)
btn_stop.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

# Device Listbox
listbox_devices = tk.Listbox(root, width=50, height=10, bg=listbox_bg_color, fg=fg_color, selectbackground=btn_bg_color)
listbox_devices.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Status Label
status_label = tk.Label(root, text="Waiting to start monitoring...", bg=bg_color, fg=fg_color)
status_label.grid(row=3, column=0, columnspan=3, pady=5)

# Spinner Label
spinner_label = tk.Label(root, text="", bg=bg_color, fg=fg_color)
spinner_label.grid(row=4, column=0, columnspan=3, pady=5)

# Counter Label
counter_label = tk.Label(root, text="", bg=bg_color, fg=fg_color)
counter_label.grid(row=5, column=0, columnspan=3, pady=5)

# Stop Button
btn_stop = tk.Button(root, text="Stop Monitoring", command=stop_monitoring, bg=btn_bg_color, fg=btn_fg_color)
btn_stop.grid(row=1, column=3, padx=5, pady=5)

# Start the main loop
root.mainloop()
