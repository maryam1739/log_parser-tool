==============================
Log Parser Tool - By Maryam Baloch
==============================

📌 DESCRIPTION:
This is a Python-based log parser tool with a simple GUI.
It detects IP addresses, log types (Apache, SSH, Syslog), usernames and passwords from log files,
and saves the extracted data as JSON.

🔧 FEATURES:
- GUI (Tkinter)
- Auto-detects Apache / SSH / Syslog log types
- Extracts IP addresses
- Extracts usernames and passwords (if present)
- Outputs to JSON file
- Cross-platform (Windows + Linux supported)

==============================
💻 HOW TO USE ON WINDOWS:
==============================
1. Make sure Python is installed: https://www.python.org/downloads/
2. Double-click the file: gui_log_parser_final.py
   OR open Command Prompt in this folder and run:
      python gui_log_parser_final.py
3. A GUI window will open → Click "Browse Log File"
4. Select any log file (e.g., from 'sample_logs' folder)
5. Output will be saved as: [filename]_parsed.json

==============================
🐧 HOW TO USE ON LINUX (Kali, Ubuntu):
==============================
1. Make sure Python 3 is installed:
      python3 --version
2. Install Tkinter GUI module:
      sudo apt update
      sudo apt install python3-tk
3. In terminal, navigate to this folder and run:
      python3 gui_log_parser_final.py
4. Select a log file using the GUI → Output JSON will be saved.

==============================
📁 SAMPLE LOG FILES INCLUDED:
==============================
Folder: sample_logs/

- apache.log
- ssh.log
- syslog.log

These can be used to test the parser and check the output.

==============================
📦 CREATED BY:
==============================
Maryam Baloch  
Cybersecurity Student  
Government College University, Hyderabad  
Supervisor: Sir Muhammad Rizwan Shahid

==============================
✅ GITHUB LINK (optional):
https://github.com/maryam1739/log-parser-tool
(Replace with your actual GitHub URL after uploading)
