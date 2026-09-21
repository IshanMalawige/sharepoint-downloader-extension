# 🚀 High-Speed Automated Video Stream Downloader

A lightweight, automated background tool built using **Python Flask**, **yt-dlp**, and a custom **Chrome/Brave Browser Extension**. This project bypasses enterprise video stream rate-limits, captures active browser session cookies, and delivers up to **10x faster downloads** with automated FFmpeg audio-video merging.

---

## 📌 Project Architecture & Features

```text
[ Browser Extension ] 
       │
       ▼ (HTTP POST: Cookies + Manifest URL)
[ Local Flask Server (Port 5000) ] 
       │
       ▼ (Spawns Background CLI Job)
[ yt-dlp Engine (-N 10 Multi-threading) ]
       │
       ├──► Video Stream (.mp4)
       └──► Audio Stream (.m4a)
       │
       ▼
[ FFmpeg Multiplexing Engine ] 
       │
       ▼
[ Final Synchronized MP4 File ]

Zero-Click Background Startup: Automatically runs the Flask server silently on http://127.0.0.1:5000 via VBScript and Windows Batch scripts upon Windows login.

Session Cookie Interception: Captures active authenticated session cookies and .mpd/.m3u8 stream manifest URLs with a single extension click.

10x Download Speed Boost: Optimizes yt-dlp via multi-threaded concurrent fragment fetching (-N 10) and chunk-size adjustments, boosting speeds from ~200 KiB/s to ~2.5+ MiB/s.

Automated FFmpeg Multiplexing: Seamlessly merges separate DASH video (.mp4) and audio (.m4a) streams into a single, synchronized MP4 output without quality loss
📁 Repository Directory Structure
Plaintext
sharepoint-downloader-extension/
├── manifest.json       # Extension configurations & permissions
├── popup.html          # Extension UI Popup Display
├── popup.js            # Frontend logic (DOM, Cookie Fetching & API Call)
├── app.py              # Flask Backend Server & yt-dlp execution pipeline
├── run_server.bat      # Batch script to launch Flask app
└── run_hidden.vbs      # VBScript for silent background execution
🛠️ Quick Setup Guide
1. Browser Extension Setup
Open Google Chrome or Brave Browser and navigate to chrome://extensions/.

Enable Developer mode in the top right corner.

Click Load unpacked and select this repository folder.

2. Windows Startup Setup (shell:startup)
Press Win + R, type shell:startup, and press Enter.

Create a Shortcut of run_hidden.vbs.

Move the created shortcut file into the shell:startup folder.

🤖 AI Collaboration Acknowledgment
Note: This project was developed with technical support from Gemini (Google AI) for code optimization, multi-threaded CLI speed enhancement, and FFmpeg pipeline configuration.

⚠️ Disclaimer
This repository is built strictly for educational and technical demonstration purposes. Always adhere to the Terms of Service of the respective platforms when downloading content.
