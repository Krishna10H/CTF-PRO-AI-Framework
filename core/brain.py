import os
from datetime import datetime

LOG_FILE = "logs/session.log"

def log(msg):
    """Saves every action to a log file for CTF documentation."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")

def ai_suggest(scan_results):
    """Simple logic to suggest next steps."""
    if "80" in scan_results or "443" in scan_results:
        return "Web Vulnerabilities Detected. Suggest: Module 2"
    return "No obvious web services. Suggest: Module 3"
