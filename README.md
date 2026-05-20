# Ransomware Simulator + Defender

A SAFE educational cybersecurity desktop application built with Python and PyQt5.

This project demonstrates:

* ransomware-like behavior simulation inside a sandbox
* behavioral threat detection
* automated recovery
* real-time monitoring dashboard

The project is strictly educational and defensive.


# Features

## Desktop GUI

* Modern dark-themed PyQt5 interface
* Real-time activity logs
* Threat status indicators
* Alert popups
* Dashboard cards

## Safe Ransomware Simulation

* Sandbox-only operation
* Harmless Base64 transformation
* File renaming simulation
* Ransom note generation
* Automatic backup creation

## Defender System

* Real-time filesystem monitoring
* Suspicious activity detection
* Threat scoring engine
* Automatic recovery system
* SQLite event logging

## Recovery Engine

* Restores original files
* Removes simulated encrypted files
* Removes ransom notes
* Logs recovery operations

# Safety Notice

IMPORTANT:

This project is strictly for:

* cybersecurity education
* defensive security research
* sandbox demonstrations
* malware detection learning

The project:

* does NOT encrypt real user files
* does NOT spread across networks
* does NOT disable antivirus
* does NOT contain destructive ransomware functionality
* only operates inside a controlled sandbox folder


# Technologies Used

* Python
* PyQt5
* watchdog
* psutil
* SQLite



# Project Structure

text
app/
│
├── main.py
│
├── ui/
│   ├── dashboard.py
│   ├── styles.py
│   └── widgets.py
│
├── simulator/
│   ├── simulator.py
│   └── encryptor.py
│
├── defender/
│   ├── detector.py
│   ├── monitor.py
│   └── recovery.py
│
├── database/
│   ├── db.py
│   └── logs.db
│
├── sandbox/
├── backups/
└── logs/


# Installation

## Clone Repository

bash
git clone https://github.com/Lobaina-Ehsan/ransomware-simulator-defender.git


## Enter Project Folder

bash
cd ransomware-simulator-defender


## Install Dependencies

bash
pip install -r requirements.txt




# Running the Application

bash
cd app
python main.py



# How It Works

1. Start the defender monitor
2. Start the simulation
3. Sandbox files are transformed into `.demo`
4. Defender detects suspicious behavior
5. Recovery system restores original files
6. Events are logged into SQLite and GUI



# Threat Detection Logic

Threat score system:

| Event                | Score |
| -------------------- | ----- |
| File Modification    | +1    |
| File Rename          | +2    |
| Ransom Note Creation | +5    |

If the score exceeds the threshold:

* alert popup appears
* recovery process starts
* files are restored automatically



# Screenshots

Add screenshots here later.

Example:

* Dashboard
* Threat alert
* Recovery process
* Activity logs



# Future Improvements

Planned features:

* Multithreading with QThread
* Real-time charts
* SIEM-style dashboard
* Entropy analysis
* Export logs
* Machine learning detection
* Advanced statistics panel
* Process activity viewer



# License

This project is intended for educational and defensive cybersecurity purposes only.

Use responsibly and only inside isolated environments.


# Author

Name: Lobaina Ehsan
Email: lobaina401@gmail.com

