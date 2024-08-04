# python\_security\_system

A Python-based security system for real-time motion detection and video storage.

## Features:
- REST API development using Python and Flask with multithreading
- Real-time motion detection using Python OpenCV
- Video storage in Google Cloud Object Storage
- A text notification system to send real-time text alerts upon detection of activity using Twilio
- Arming/Disarming functionalities
- Activity logs for detailed monitoring and analysis of security events

## Installation

Prerequisites:

- Python 3.9+
- Node.js
- ffmpeg
- Other python dependencies, you can install these by running: ``pip install -r requirements.txt`` from the root directory.
- Run ``cd src/frontend && npm install``

## Execution

- Running The Backend:
    ``cd src/backend && python main.py``

- Running The Frontend:
    ``cd src/frontend && npm start``