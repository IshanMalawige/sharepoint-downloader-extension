from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    video_url = data.get('url')
    cookies_data = data.get('cookies')

    if not video_url or not cookies_data:
        return jsonify({"status": "error", "message": "Missing URL or cookies"}), 400

    # Save cookies to cookies.txt
    cookie_file_path = os.path.join(os.getcwd(), "cookies.txt")
    with open(cookie_file_path, "w", encoding="utf-8") as f:
        f.write(cookies_data)

    # Run yt-dlp in a new CMD window
# Run yt-dlp in a new CMD window
    command = f'start cmd /k py -m yt_dlp --cookies cookies.txt "{video_url}"'
    subprocess.Popen(command, shell=True)

    return jsonify({"status": "success", "message": "Download initiated"})

if __name__ == '__main__':
    print("SharePoint Downloader Server Running on http://127.0.0.1:5000")
    app.run(port=5000)