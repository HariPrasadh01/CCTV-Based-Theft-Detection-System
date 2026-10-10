CCTV-Based Theft Detection and Alert System

📌 Project Overview

The CCTV-Based Theft Detection and Alert System is a Python-based application designed to help shop owners monitor suspicious activities using CCTV video footage.

The system uses OpenCV for video processing and Flask to provide a web-based application. It analyzes CCTV footage to detect suspected shoplifting activities and automatically sends email alerts through Gmail when theft is detected.

Each alert includes a screenshot captured from the video footage to help users review the detected incident.

The system sends an email only when suspected shoplifting is detected. If no theft is detected, no alert email is sent.

✨ Features

🎥 CCTV Video Analysis: Analyzes video footage using OpenCV.

🔍 Shoplifting Detection: Identifies suspected shoplifting activities based on the implemented detection logic.

📧 Automated Email Alerts: Sends Gmail notifications when suspected theft is detected.

📸 Evidence Screenshot: Attaches a screenshot of the detected incident to the alert email.

🚫 No Unnecessary Alerts: Does not send alert emails when no suspected theft is detected.

🌐 Flask Web Application: Uses Flask to provide the application's web interface and functionality.

🛠️ Technologies Used

Technology

Purpose

Python

Core programming language

Flask

Web application framework

OpenCV

Video processing and analysis

Gmail SMTP

Sending email alerts

HTML/CSS

Web interface, if implemented

⚙️ How It Works

Video Input: The system receives CCTV video footage for analysis.

Video Processing: OpenCV processes the video frames.

Activity Detection: The implemented detection logic checks for suspected shoplifting.

Screenshot Capture: When suspected theft is detected, the system captures a screenshot of the relevant video frame.

Email Notification: The system sends an alert through Gmail with the screenshot attached.

Normal Monitoring: If no suspected theft is detected, no alert email is sent.

📋 Prerequisites

Before running the project, ensure you have installed:

Python 3

pip (Python package manager)

A Gmail account for sending notifications

🚀 Installation and Setup

Step 1: Clone the Repository

git clone https://github.com/HariPrasadh01/CCTV---Based-Theft-Detection-System.git

Navigate to the project directory:

cd CCTV---Based-Theft-Detection-System

Step 2: Create a Virtual Environment

python -m venv venv

Activate the virtual environment.

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate

Step 3: Install Dependencies

If your project contains a requirements.txt file, run:

pip install -r requirements.txt

Otherwise, install the required packages used by your project:

pip install flask opencv-python

Install any additional dependencies required by your implementation.

Step 4: Configure Gmail Alerts

Configure the sender email address, recipient email address, and Gmail authentication according to your application's implementation.

For Gmail SMTP authentication, use a Google App Password if your account supports it and two-step verification is enabled.

Security note: Never upload Gmail passwords, App Passwords, API keys, or other secrets to GitHub. Store sensitive configuration in environment variables or a local .env file, and exclude that file from version control.

Step 5: Run the Application

If your Flask application entry point is app.py, run:

python app.py

Alternatively, if your application uses Flask's command-line interface:

flask --app app run

Open the local address displayed in your terminal to access the application, if it provides a web interface.

Note: The entry-point filename and video input configuration may differ depending on your project structure.

📧 Example Alert

When suspected shoplifting is detected, the system sends an email containing a notification similar to:

Subject: Shoplifting Detected!

Message:

Suspected shoplifting activity has been detected in the CCTV footage. Please review the attached screenshot for further investigation.

Attachment: Screenshot of the detected incident.

No email notification is sent when no suspected theft is detected.

🔐 Security and Privacy

Keep Gmail credentials secure.

Never commit passwords or secret configuration files to a public repository.

Use CCTV footage responsibly and comply with applicable privacy laws.

Review detected incidents manually before concluding that theft has occurred.

🔮 Future Enhancements

Potential improvements include:

Integrating a machine learning model for more accurate shoplifting detection.

Supporting live CCTV camera feeds.

Adding a dashboard to view detected incidents.

Maintaining a history of detection events.

Supporting multiple CCTV cameras.

Adding configurable email recipients and alert settings.

👨‍💻 Author

Hari Prasadh 

GitHub: https://github.com/HariPrasadh01

Linkedin: https://www.linkedin.com/in/hari-prasadh01
