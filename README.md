🛠️ Step-by-Step Setup Guide
Step 1: Clone or Download this Repository
Download this repository and keep all project files in a single dedicated folder on your PC (e.g., C:\sharepoint-downloader-extension).

Ensure your folder contains the following files:

manifest.json

popup.html

popup.js

app.py

Step 2: Load the Extension into your Browser (Chrome / Brave / Edge)
Open your browser and go to the extensions management page:

Brave: brave://extensions/

Chrome: chrome://extensions/

Edge: edge://extensions/

Turn ON Developer mode (toggle switch at the top right corner).

Click on the Load unpacked button.

Select the project folder containing manifest.json.

The SharePoint Video Downloader extension icon will now appear in your browser toolbar!

Step 3: Auto-Start Python Backend with Windows Startup
To make the downloader work seamlessly without manually running py app.py every time, configure it to launch automatically when Windows boots up:

Inside your project folder, create a new batch file named run_server.bat with the following lines:

DOS
@echo off
title SharePoint Downloader Server
cd /d "%~dp0"
py app.py
pause
Press Win + R on your keyboard to open the Run dialog box.

Type shell:startup and hit Enter. (This opens the Windows Startup folder).

Copy your run_server.bat file (or create a shortcut for it) and Paste it inside this Startup folder.

💡 Result: Now, whenever your PC starts up, the background Python server starts automatically!

🎬 How to Download SharePoint Videos
Open Microsoft Edge, Brave, or Chrome and navigate to your SharePoint / Teams video recording page.

Sign in with your Microsoft account and ensure the video starts playing for a couple of seconds.

Click on the SharePoint Downloader extension icon in your browser extension toolbar.

Click the "Download Video" button.

A new Command Prompt (CMD) window will launch automatically, extracting session cookies and downloading the full 400MB+ MP4 video directly to your PC folder!

❓ Troubleshooting
Python execution error: Make sure you use py instead of python in your environment.

Browser cookie database locked: Ensure the backend script uses the exported active tab cookies or close background browser instances if using native extraction.
