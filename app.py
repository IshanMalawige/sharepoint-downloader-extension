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

    current_dir = os.getcwd()
    
    # 🚀 SPEED BOOST OPTIONS:
    # -N 10 / --concurrent-fragments 10 : එක පාර fragments 10ක් parallel download කරයි
    # --buffer-size 16M : Download buffer එක වැඩි කරයි
    # --http-chunk-size 10M : Speed throttles නොවී එක දිගට chunk විශාලව ගනියි
    command = (
        f'start cmd /k "cd /d "{current_dir}" && '
        f'py -m yt_dlp -4 -N 10 --buffer-size 16M --http-chunk-size 10M '
        f'--force-overwrites --no-part '
        f'-f "bv*+ba/b/bestvideo+bestaudio/best" '
        f'--format-sort "res,ext:mp4:m4a" '
        f'--cookies cookies.txt "{video_url}""'
    )
    
    subprocess.Popen(command, shell=True)

    return jsonify({"status": "success", "message": "Download initiated"})

if __name__ == '__main__':
    print("SharePoint Downloader Server Running on http://127.0.0.1:5000")
    app.run(port=5000)