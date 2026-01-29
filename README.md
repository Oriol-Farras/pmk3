# Project Setup & Installation Guide

This guide describes how to set up the Raspberry Pi Zero 2 W and install the necessary software for this project.

## Hardware Requirements

*   **Raspberry Pi Zero 2 W**
*   MicroSD Card (8GB+ recommended)
*   Power Supply
*   Peripherals (SSD1306 OLED Display, etc.) connected via I2C

## 1. Operating System Installation

1.  Download and install the **Raspberry Pi Imager** on your computer.
2.  Insert your MicroSD card into your computer.
3.  Open Raspberry Pi Imager:
    *   **Choose Device:** Select `Raspberry Pi Zero 2 W`.
    *   **Choose OS:** Select `Raspberry Pi OS (other)` -> `Raspberry Pi OS Lite (64-bit)`.
    *   **Choose Storage:** Select your MicroSD card.
4.  **Important:** Click the **Settings** icon (gear) or press `Ctrl + Shift + X` to configure advanced options before writing:
    *   Set **Hostname**.
    *   Enable **SSH** (Use password authentication).
    *   Set **Username** and **Password**.
    *   Configure **Wireless LAN** (SSID and Password).
5.  Click **NEXT** and then **WRITE**.
6.  Once finished, insert the SD card into the Raspberry Pi and power it on.

## 2. System Configuration & I2C

Connect to your Raspberry Pi via SSH (e.g., `ssh user@hostname.local`).

1.  **Update the system:**
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```

2.  **Enable I2C Interface:**
    *   Run the configuration tool:
        ```bash
        sudo raspi-config
        ```
    *   Navigate to **Interface Options** -> **I2C**.
    *   Select **Yes** to enable the ARM I2C interface.
    *   Finish and reboot if prompted (or strictly optional for just I2C, but good practice).

3.  **Install System Dependencies:**
    Install Git, Python system tools, and libraries required for Pillow and hardware access:
    ```bash
    sudo apt install -y git python3-pip python3-venv i2c-tools libgpiod-dev python3-libgpiod libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7-dev
    ```

4.  **Verify I2C Connection (Optional):**
    If your hardware is connected, check if the device is detected:
    ```bash
    sudo i2cdetect -y 1
    ```
    (You should see a generic address like `3c` for SSD1306 displays).

## 3. Project Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Oriol-Farras/pmk3
    cd pmk3
    ```

2.  **Set up a Python Virtual Environment:**
    It is recommended (and often required) to use a virtual environment on Raspberry Pi OS.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Python Dependencies:**
    With the virtual environment active, install the requirements:
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
    *Note: This installs `Adafruit-Blinka`, `adafruit-circuitpython-ssd1306`, `Pillow`, `gpiozero`, and `RPi.GPIO`.*

## 4. Running the Application

Ensure you are inside the project folder and your virtual environment is active.

```bash
python main.py
```

### Auto-start on Boot (Optional)
To make the script run automatically on boot, you can add it to `rc.local` or create a systemd service.

**Example Systemd Service:**
1.  Create the service file:
    ```bash
    sudo nano /etc/systemd/system/pmk3.service
    ```
2.  Add the following content (adjust paths and user as needed):
    ```ini
    [Unit]
    Description=PMK3 Display Service
    After=network.target

    [Service]
    User=<YOUR_USERNAME>
    WorkingDirectory=/home/<YOUR_USERNAME>/pmk3
    ExecStart=/home/<YOUR_USERNAME>/pmk3/venv/bin/python main.py
    Restart=always

    [Install]
    WantedBy=multi-user.target
    ```
3.  Enable and start the service:
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable pmk3.service
    sudo systemctl start pmk3.service
    ```
