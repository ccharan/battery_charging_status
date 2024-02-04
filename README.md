# Battery Charging Status

## Overview

This code monitors the battery charging status of your device and provides notifications when the battery level goes above 80% or drops below 40%. It utilizes both audio alerts and system notifications to keep the user informed about the battery status.

## Features

- **Real-time Monitoring:** Constantly checks the battery status to ensure timely notifications.
- **Audio Alerts:** Plays a sound when the battery level exceeds 80% or falls below 40%.
- **System Notifications:** Displays notifications on the screen for easy visibility.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ccharan/battery_charging_status.git
   cd battery-charging-status

2. **Install Dependencies:**
    ```bash
    pip install -r requirement.txt

## Run the Code
    python battery_status.py


## Configuration

You can customize the thresholds for battery notifications by modifying the following lines in the battery_status.py file:

    # Set the threshold for high battery level (in percentage)
    HIGH_BATTERY_THRESHOLD = 80

    # Set the threshold for low battery level (in percentage)
    LOW_BATTERY_THRESHOLD = 40

## Dependencies
   ```bash
    Python > 3.9.6
   ```
