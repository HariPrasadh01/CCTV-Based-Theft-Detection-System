from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import os
import cv2
import smtplib
from PIL import Image
from email.message import EmailMessage

# Flask app initialization
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secure key

# Upload folder configuration
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Dummy credentials for login
USERNAME = "admin"
PASSWORD = "admin"

# Email configuration
EMAIL_ADDRESS = "hariparames515@gmail.com"
EMAIL_PASSWORD = "vurb eqav nvgr fuot"

# ---- ROUTES ----

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == USERNAME and password == PASSWORD:
            session["user"] = username
            return redirect(url_for("upload"))
    return render_template("index.html", page="login")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        if "video" not in request.files:
            return "No video uploaded", 400

        video = request.files["video"]
        email = request.form["email"]

        if video.filename == "":
            return "No selected file", 400

        video_path = os.path.join(app.config["UPLOAD_FOLDER"], video.filename)
        video.save(video_path)

        # Call theft detection function
        result, screenshot_path = detect_theft(video_path)

        if result:
            send_email(screenshot_path, email)
        
        return render_template("result.html", result=result)

    return render_template("upload.html")

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# ---- THEFT DETECTION FUNCTION ----

def detect_theft(video_path):
    print(f"Processing video: {video_path}")
    cap = cv2.VideoCapture(video_path)
    _, first_frame = cap.read()
    gray_first = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    gray_first = cv2.GaussianBlur(gray_first, (21, 21), 0)

    detected = False
    screenshot_path = "static/screenshot.jpg"

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        frame_diff = cv2.absdiff(gray_first, gray)
        _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 1000:
                print("Theft detected!")
                detected = True
                cv2.imwrite(screenshot_path, frame)  # Save screenshot
                break

        if detected:
            break

    cap.release()
    return detected, screenshot_path if detected else None

# ---- EMAIL SENDING FUNCTION ----

def send_email(image_path, recipient_email):
    msg = EmailMessage()
    msg["Subject"] = "Shoplifting Alert!"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient_email
    msg.set_content("A shoplifting incident has been detected. Please find the attached screenshot.")

    with open(image_path, "rb") as img:
        img_data = img.read()
        img_type = Image.open(image_path).format.lower()
        msg.add_attachment(img_data, maintype="image", subtype=img_type, filename="theft_screenshot.jpg")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Email sending failed: {e}")

# ---- RUN FLASK ----
if __name__ == "__main__":
    app.run(debug=True)
