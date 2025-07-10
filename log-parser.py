import re
import json
from tkinter import Tk, Label, Button, filedialog, messagebox

# Regex patterns
IP_REGEX = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
USERNAME_REGEX = r'Username:\s*(\w+)'
PASSWORD_REGEX = r'Password:\s*(\S+)'

# Detect log type
def detect_log_type(line):
    if "sshd" in line:
        return "SSH"
    elif "GET" in line or "POST" in line:
        return "Apache"
    elif re.search(r'\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}', line):
        return "Syslog"
    else:
        return "Unknown"

# Parse function
def parse_log(file_path):
    output = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                ip = re.search(IP_REGEX, line)
                log_type = detect_log_type(line)
                username = re.search(USERNAME_REGEX, line)
                password = re.search(PASSWORD_REGEX, line)

                log_entry = {
                    "line": line.strip(),
                    "log_type": log_type,
                    "ip_address": ip.group() if ip else None,
                    "username": username.group(1) if username else None,
                    "password": password.group(1) if password else None
                }
                output.append(log_entry)

        output_file = file_path + "_parsed.json"
        with open(output_file, 'w') as f:
            json.dump(output, f, indent=4)

        messagebox.showinfo("Success", f"Parsed output saved:\n{output_file}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
def browse_and_parse():
    file_path = filedialog.askopenfilename(title="Select Log File")
    if file_path:
        parse_log(file_path)

def launch_gui():
    root = Tk()
    root.title("Log Parser Final Tool")
    root.geometry("300x120")

    Label(root, text="Select a log file to parse:").pack(pady=10)
    Button(root, text="Browse Log File", command=browse_and_parse).pack()

    root.mainloop()

if __name__ == "__main__":
    launch_gui()
