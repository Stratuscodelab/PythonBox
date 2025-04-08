# Python Network Monitoring Tool

This repository contains Python scripts for monitoring network devices and managing metadata. The primary script, `wcheckadv.py`, provides a GUI-based tool to monitor network devices and alert users if any device goes offline.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Scripts Overview](#scripts-overview)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Network Device Monitoring**: Continuously monitors a list of devices (IP addresses or URLs) and alerts the user if a device is unreachable.
- **GUI Interface**: A user-friendly graphical interface built with `tkinter`.
- **Dark Theme**: A visually appealing dark theme for the GUI.
- **Device Management**: Add or remove devices from the monitoring list dynamically.
- **Real-Time Feedback**: Displays the status of devices, elapsed time, and a spinner animation during monitoring.

---

## Requirements

- Python 3.7 or higher
- Required Python libraries:
  - `ping3`
  - `tkinter` (comes pre-installed with Python)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Stratuscodelab/PythonBox.git
   cd PythonBox
